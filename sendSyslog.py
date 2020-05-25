#! /usr/bin/env python
# -*- coding:utf-8 -*-
_author_ = "liurui"

import sys
#import logging
import logging.handlers
myfacility = sys.argv[1]
syslogHandler = logging.handlers.SysLogHandler(address=('10.175.255.253', 514), facility='local6')
formatter = logging.Formatter("Fortree-Server %(levelname)s : %(message)s")
syslogHandler.setFormatter(formatter)
logging.getLogger("").handlers = []
logging.getLogger("").addHandler(syslogHandler)
logger = logging.getLogger("")
if myfacility == 'warning':
  logger.warning("This is a warning message")
elif myfacility == 'error':
  logger.error("This is a error message")
elif myfacility == 'critical':
  logger.critical("This is a critical message")
