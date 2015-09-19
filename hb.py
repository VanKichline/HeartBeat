#!/usr/bin/python
import time, httplib,logging

apiHost = 'kichline-heartbeat.azurewebsites.net'
apiPort = 80
apiPath = '/api/heartbeat'
apiQuery= 'group=Kichline.Kirkland&device=BB1&service=uptime&status='
logLevel = logging.INFO

def setup_logger():
  global logLevel
  logger = logging.getLogger('heartbeat')
  hdlr = logging.FileHandler('/var/tmp/heartbeat.log')
  formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
  hdlr.setFormatter(formatter)
  logger.addHandler(hdlr)
  logger.setLevel(logLevel)
  return logger

def hb(stat):
  conn = httplib.HTTPConnection(apiHost, apiPort)
  conn.connect()
  conn.set_debuglevel(0)
  msg = apiPath+'?'+apiQuery+stat
  request = conn.putrequest('POST', msg)
  headers = {}
  headers['Content-Length'] = "0"
  headers['Accept'] = '*/*'
  for k in headers:
    conn.putheader(k, headers[k])
  conn.endheaders()
  
  conn.send('')
  logger.info(msg)
  resp = conn.getresponse()
  conn.close()

startTime = time.time()
logger = setup_logger()
while True:
  interval = int(time.time() - startTime)
  hb(str(interval))
  time.sleep(300)
