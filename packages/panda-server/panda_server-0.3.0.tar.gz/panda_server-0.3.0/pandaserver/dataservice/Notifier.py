"""
notifier

"""

import datetime
import re
import smtplib
import sys
import time
import traceback
import uuid
from urllib.parse import urlencode

import pandaserver.taskbuffer.ErrorCode
from pandacommon.pandalogger.PandaLogger import PandaLogger
from pandaserver.config import panda_config
from pandaserver.dataservice.DDM import rucioAPI
from pandaserver.taskbuffer.OraDBProxy import DBProxy

# logger
_logger = PandaLogger().getLogger("Notifier")

# ignored DN
_ignoreList = [
    "Nurcan Ozturk",
    "Xin Zhao",
    "Dietrich Liko",
]

# NG words in email address
_ngWordsInMailAddr = [
    "support",
    "system",
    "stuff",
    "service",
    "secretariat",
    "club",
    "user",
    "admin",
    "cvs",
    "grid",
    "librarian",
    "svn",
    "atlas",
    "cms",
    "lhcb",
    "alice",
    "alaelp",
]

# port for SMTP server
smtpPortList = [25, 587]


def initLogger(pLogger):
    # redirect logging to parent as it doesn't work in nested threads
    global _logger
    _logger = pLogger


# wrapper to patch smtplib.stderr to send debug info to logger
class StderrLogger(object):
    def __init__(self, token):
        self.token = token

    def write(self, message):
        message = message.strip()
        if message != "":
            _logger.debug(f"{self.token} {message}")


class Notifier:
    # constructor
    def __init__(self, taskBuffer, job, datasets, summary={}, mailFile=None, mailFileName=""):
        self.job = job
        self.datasets = datasets
        self.taskBuffer = taskBuffer
        self.summary = summary
        self.mailFile = mailFile
        self.mailFileName = mailFileName

    # main
    def run(self):
        if self.mailFile is None:
            _logger.debug(f"{self.job.PandaID} start")
            try:
                # check job type
                if self.job.prodSourceLabel != "user" and self.job.prodSourceLabel != "panda":
                    _logger.error(f"Invalid job type : {self.job.prodSourceLabel}")
                    _logger.debug(f"{self.job.PandaID} end")
                    return
                # ignore some DNs to avoid mail storm
                for igName in _ignoreList:
                    if re.search(igName, self.job.prodUserID) is not None:
                        _logger.debug(f"Ignore DN : {self.job.prodUserID}")
                        _logger.debug(f"{self.job.PandaID} end")
                        return
                # get e-mail address
                mailAddr = self.getEmail(self.job.prodUserID)
                if mailAddr == "":
                    _logger.error(f"could not find email address for {self.job.prodUserID}")
                    _logger.debug(f"{self.job.PandaID} end")
                    return
                # not send
                if mailAddr in ["notsend", "", None] or (mailAddr is not None and mailAddr.startswith("notsend")):
                    _logger.debug(f"not send to {self.job.prodUserID}")
                    _logger.debug(f"{self.job.PandaID} end")
                    return
                # use all datasets
                if self.summary != {}:
                    self.datasets = []
                    for tmpJobID in self.summary:
                        tmpDsList = self.summary[tmpJobID]
                        if tmpDsList == []:
                            continue
                        self.datasets += tmpDsList
                # get full jobSpec including metadata
                self.job = self.taskBuffer.peekJobs(
                    [self.job.PandaID],
                    fromDefined=False,
                    fromActive=False,
                    fromWaiting=False,
                )[0]
                if self.job is None:
                    _logger.error(f"{self.job.PandaID} : not found in DB")
                    _logger.debug(f"{self.job.PandaID} end")
                    return
                # get IDs
                ids = []
                # from active tables
                tmpIDs = self.taskBuffer.queryPandaIDwithDataset(self.datasets)
                for tmpID in tmpIDs:
                    if tmpID not in ids:
                        ids.append(tmpID)
                # from archived table
                if self.job.jobsetID in [0, "NULL", None]:
                    tmpIDs = self.taskBuffer.getPandIDsWithIdInArch(self.job.prodUserName, self.job.jobDefinitionID, False)
                else:
                    tmpIDs = self.taskBuffer.getPandIDsWithIdInArch(self.job.prodUserName, self.job.jobsetID, True)
                for tmpID in tmpIDs:
                    if tmpID not in ids:
                        ids.append(tmpID)
                _logger.debug(f"{self.job.PandaID} IDs: {ids}")
                if len(ids) != 0:
                    # get jobs
                    jobs = self.taskBuffer.getFullJobStatus(
                        ids,
                        fromDefined=False,
                        fromActive=False,
                        fromWaiting=False,
                        forAnal=False,
                    )
                    # statistics
                    nTotal = 0
                    nSucceeded = 0
                    nFailed = 0
                    nPartial = 0
                    nCancel = 0
                    # time info
                    creationTime = self.job.creationTime
                    endTime = self.job.modificationTime
                    if isinstance(endTime, datetime.datetime):
                        endTime = endTime.strftime("%Y-%m-%d %H:%M:%S")
                    # datasets
                    iDSList = []
                    oDSList = []
                    siteMap = {}
                    logDS = None
                    for tmpJob in jobs:
                        if tmpJob.jobDefinitionID not in siteMap:
                            siteMap[tmpJob.jobDefinitionID] = tmpJob.computingSite
                        for file in tmpJob.Files:
                            if file.type == "input":
                                if file.dataset not in iDSList:
                                    iDSList.append(file.dataset)
                            else:
                                if file.dataset not in oDSList:
                                    oDSList.append(file.dataset)
                                if file.type == "log":
                                    logDS = file.dataset
                    # job/jobset IDs and site
                    if self.summary == {}:
                        jobIDsite = f"{self.job.jobDefinitionID}/{self.job.computingSite}"
                        jobsetID = self.job.jobDefinitionID
                        jobDefIDList = [self.job.jobDefinitionID]
                    else:
                        jobDefIDList = sorted(self.summary)
                        jobIDsite = ""
                        tmpIndent = "             "
                        for tmpJobID in jobDefIDList:
                            jobIDsite += f"{tmpJobID}/{siteMap[tmpJobID]}\n{tmpIndent}"
                        remCount = len(tmpIndent) + 1
                        jobIDsite = jobIDsite[:-remCount]
                        jobsetID = self.job.jobsetID
                    # count
                    for job in jobs:
                        if job is None:
                            continue
                        # ignore pilot-retried job
                        if job.taskBufferErrorCode in [pandaserver.taskbuffer.ErrorCode.EC_PilotRetried]:
                            continue
                        # total
                        nTotal += 1
                        # count per job status
                        if job.jobStatus == "finished":
                            # check all files were used
                            allUses = True
                            for file in job.Files:
                                if file.type == "input" and file.status in ["skipped"]:
                                    allUses = False
                                    break
                            if allUses:
                                nSucceeded += 1
                            else:
                                nPartial += 1
                        elif job.jobStatus == "failed":
                            nFailed += 1
                        elif job.jobStatus == "cancelled":
                            nCancel += 1
                    # make message
                    if nSucceeded == nTotal:
                        finalStatInSub = "(All Succeeded)"
                    else:
                        finalStatInSub = f"({nSucceeded}/{nTotal} Succeeded)"
                    fromadd = panda_config.emailSender
                    if self.job.jobsetID in [0, "NULL", None]:
                        message = f"""Subject: PANDA notification for JobID : {self.job.jobDefinitionID}  {finalStatInSub}
                            From: {fromadd}
                            To: {mailAddr}

                            Summary of JobID : {self.job.jobDefinitionID}

                            Site : {self.job.computingSite}"""
                    else:
                        message = f"""Subject: PANDA notification for JobsetID : {jobsetID}  {finalStatInSub}
                            From: {fromadd}
                            To: {mailAddr}

                            Summary of JobsetID : {jobsetID}

                            JobID/Site : {jobIDsite}"""
                    message += f"""

                        Created : {creationTime} (UTC)
                        Ended   : {endTime} (UTC)

                        Total Number of Jobs : {nTotal}
                                   Succeeded : {nSucceeded}
                                   Partial   : {nPartial}
                                   Failed    : {nFailed}
                                   Cancelled : {nCancel}
                        """
                    # input datasets
                    for iDS in iDSList:
                        message += f"""
                            In  : {iDS}"""
                    # output datasets
                    for oDS in oDSList:
                        message += f"""
                            Out : {oDS}"""
                    # command
                    if self.job.metadata not in ["", "NULL", None]:
                        message += f"""

                            Parameters : {self.job.metadata}"""
                    # URLs to PandaMon
                    if self.job.jobsetID in [0, "NULL", None]:
                        for tmpIdx, tmpJobID in enumerate(jobDefIDList):
                            urlData = {}
                            urlData["job"] = "*"
                            urlData["jobDefinitionID"] = tmpJobID
                            urlData["user"] = self.job.prodUserName
                            urlData["at"] = (str(creationTime)).split()[0]
                            if tmpIdx == 0:
                                message += f"""

                                    PandaMonURL : http://panda.cern.ch/server/pandamon/query?{urlencode(urlData)}"""
                            else:
                                message += f"""
                                                  http://panda.cern.ch/server/pandamon/query?{urlencode(urlData)}"""
                    else:
                        urlData = {}
                        urlData["job"] = "*"
                        urlData["jobsetID"] = self.job.jobsetID
                        urlData["user"] = self.job.prodUserName
                        urlData["at"] = (str(creationTime)).split()[0]
                        newUrlData = {}
                        newUrlData["jobtype"] = "analysis"
                        newUrlData["jobsetID"] = self.job.jobsetID
                        newUrlData["prodUserName"] = self.job.prodUserName
                        newUrlData["hours"] = 71
                        message += f"""

                            PandaMonURL : http://panda.cern.ch/server/pandamon/query?{urlencode(urlData)}"""
                        if logDS is not None:
                            message += f"""
                                TaskMonitorURL : https://dashb-atlas-task.cern.ch/templates/task-analysis/#task={logDS}"""
                        message += f"""
                            NewPandaMonURL : https://pandamon.cern.ch/jobinfo?{urlencode(newUrlData)}"""

                    # tailer
                    message += """


                        Report Panda problems of any sort to

                          the eGroup for help request
                            hn-atlas-dist-analysis-help@cern.ch

                          the Panda JIRA for software bug
                            https://its.cern.ch/jira/browse/ATLASPANDA
                        """

                    # send mail
                    self.sendMail(self.job.PandaID, fromadd, mailAddr, message, 1, True)
            except Exception:
                errType, errValue = sys.exc_info()[:2]
                _logger.error(f"{self.job.PandaID} {errType} {errValue}")
            _logger.debug(f"{self.job.PandaID} end")
        else:
            try:
                _logger.debug(f"start recovery for {self.mailFileName}")
                # read from file
                pandaID = self.mailFile.readline()[:-1]
                fromadd = self.mailFile.readline()[:-1]
                mailAddr = self.mailFile.readline()[:-1]
                message = self.mailFile.read()
                _logger.debug(f"{pandaID} start recovery")
                if message != "":
                    self.sendMail(pandaID, fromadd, mailAddr, message, 5, False)
            except Exception:
                errType, errValue = sys.exc_info()[:2]
                _logger.error(f"{self.mailFileName} {errType} {errValue}")
            _logger.debug(f"end recovery for {self.mailFileName}")

    # send mail
    def sendMail(self, pandaID, fromadd, mailAddr, message, nTry, fileBackUp):
        _logger.debug(f"{pandaID} send to {mailAddr}\n{message}")
        for iTry in range(nTry):
            try:
                smtpPort = smtpPortList[iTry % len(smtpPortList)]
                server = smtplib.SMTP(panda_config.emailSMTPsrv, smtpPort)
                server.set_debuglevel(1)
                server.ehlo()
                server.starttls()
                # server.login(panda_config.emailLogin,panda_config.emailPass)
                out = server.sendmail(fromadd, mailAddr, message)
                _logger.debug(f"{pandaID} {str(out)}")
                server.quit()
                break
            except Exception:
                errType, errValue = sys.exc_info()[:2]
                if iTry + 1 < nTry:
                    # sleep for retry
                    _logger.debug(f"{pandaID} sleep {iTry} due to {errType} {errValue}")
                    time.sleep(30)
                else:
                    _logger.error(f"{pandaID} {errType} {errValue}")
                    if fileBackUp:
                        # write to file which is processed in add.py
                        mailFile = f"{panda_config.logdir}/mail_{self.job.PandaID}_{str(uuid.uuid4())}"
                        oMail = open(mailFile, "w")
                        oMail.write(str(self.job.PandaID) + "\n" + fromadd + "\n" + mailAddr + "\n" + message)
                        oMail.close()

    # get email
    def getEmail(self, dn):
        # get DN
        _logger.debug(f"getDN for {dn}")
        dbProxy = DBProxy()
        distinguishedName = dbProxy.cleanUserID(dn)
        _logger.debug(f"DN = {distinguishedName}")
        if distinguishedName == "":
            _logger.error(f"cannot get DN for {dn}")
            return ""
        # get email from MetaDB
        mailAddrInDB, dbUptime = self.taskBuffer.getEmailAddr(distinguishedName, withUpTime=True)
        _logger.debug(f"email in MetaDB : '{mailAddrInDB}'")
        notSendMail = False
        if mailAddrInDB not in [None, ""]:
            # email mortification is suppressed
            if mailAddrInDB.split(":")[0] == "notsend":
                notSendMail = True
        # avoid too frequently lookup
        if dbUptime is not None and datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) - dbUptime < datetime.timedelta(hours=1):
            _logger.debug("no lookup")
            if notSendMail or mailAddrInDB in [None, ""]:
                return "notsend"
            else:
                return mailAddrInDB.split(":")[-1]
        # get email from DQ2
        try:
            tmpStatus, userInfo = rucioAPI.finger(dn)
            if tmpStatus:
                mailAddr = userInfo["email"]
                _logger.debug(f"email from DDM : '{mailAddr}'")
            else:
                mailAddr = None
                _logger.error(f"failed to get email from DDM : {userInfo}")
            if mailAddr is None:
                mailAddr = ""
            # make email field to update DB
            mailAddrToDB = ""
            if notSendMail:
                mailAddrToDB += "notsend:"
            mailAddrToDB += mailAddr
            # update database
            _logger.debug(f"update email for {distinguishedName} to {mailAddrToDB}")
            self.taskBuffer.setEmailAddr(distinguishedName, mailAddrToDB)
            if notSendMail:
                return "notsend"
            return mailAddr
        except Exception as e:
            _logger.error(f"getEmail failed with {str(e)} {traceback.format_exc()}")
        return ""
