from websites_class import *
import os, sys
import threading, time
import requests

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

websites = Websites("websites.txt")
#print(websites.getNextWebsiteToCheck())
#websites.putWebsiteData({"index":0, "website": "duckduckgo.com", "statusCode": 200})
#websites.saveReport()



dataLock = threading.Lock()

class Worker(threading.Thread):
    def __init__(self, threadName, websites, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.websites = websites
        self.sleepTime = sleepTime

    def run(self):
        while True:
            dataLock.acquire()
            websiteToCheck = self.websites.getNextWebsiteToCheck()
            dataLock.release()
             
            if not websiteToCheck:
                break

            url = websiteToCheck['website']
            response = requests.get(url)
            print(response.status_code)
            websiteToCheck["statusCode"] = response.status_code
            self.websites.putWebsiteData(websiteToCheck)
            print(self.websites.reportList)

            print(websiteToCheck)
            time.sleep(self.sleepTime)

        print((self.threadName, "ended"))

       

Worker1 = Worker("Worker1", websites, 0.1)
Worker2 = Worker("Worker2", websites, 0.3)
Worker3 = Worker("Worker3", websites, 0.5)

Worker1.start()
Worker2.start()
Worker3.start()

Worker1.join()
Worker2.join()
Worker3.join()



