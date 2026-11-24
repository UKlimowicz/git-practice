import os, sys
import requests
import urllib.parse


print("Number of arguments: ", len(sys.argv) )
print("Arguments list: ", sys.argv)

url = "https://python.org"
if len(sys.argv) > 1:
    url = sys.argv[1]

print("Website do download:", url)



scriptDir = os.path.dirname(__file__) 
print("Current working dir: ", os.getcwd())
print("Script directory: ", scriptDir)
print(scriptDir)


if not os.path.exists("./websites"):
    os.mkdir("websites")
    print(os.path.exists("./websites"))

response = requests.get(url)
print(response.text)


parsedUrl = urllib.parse.urlparse(url)
print(parsedUrl)
print(parsedUrl.netloc)

websitesDir = os.path.join(scriptDir, "websites")

if not os.path.exists(websitesDir):
    os.mkdir(websitesDir)

fh = open(
    os.path.join(websitesDir, "python-org.html"),
      "w", 
      encoding="utf-8"
      )

fh.write(response.text)
fh.close()



