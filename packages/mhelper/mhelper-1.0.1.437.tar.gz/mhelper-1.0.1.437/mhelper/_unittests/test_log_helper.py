from mhelper import log_helper


log = log_helper.MLog("my.log")
log.attach_to_console()

log("this is a log")

with log.action("this is an action") as action:
    pass

with log.time("this is a timer" ) as timer:
    pass

