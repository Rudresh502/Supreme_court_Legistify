import requests
import urllib3
urllib3.disable_warnings()

def FetchandSavetoFile(url,path):
    r = requests.get(url,verify=False)
    with open(path, "w", encoding="utf-8") as fp:
        fp.write(r.text)
        fp.close()

url = "https://main.sci.gov.in/causelist"
FetchandSavetoFile(url, "Supreme_court_causelist.html")

