from uptime_kuma_api import UptimeKumaApi, MonitorType
import urllib.parse
from itertools import groupby
import tldextract
import os
from dotenv import load_dotenv

load_dotenv()

# If set to true, the Script will add the domains in abbreviated form, taking the initials, middle and 
nsfw_check = False


# function for domain name digest for some NSFW check
def urlclean(domain):
    url_clean = tldextract.extract(domain)
    re = url_clean.domain
    resx = ''
    if len(re) > 6:
        resx = re[0] + re[1] + re[2] + re[3] + re[4] + re[len(re) // 2] + re[-1]
    else:
        resx = re[0] + re[len(re) // 2] + re[-1]
    return resx.upper()


print("Connecting to Uptime Kuma on: "+os.getenv('UPTIME_KUMA_URL'))
api = UptimeKumaApi(os.getenv('UPTIME_KUMA_URL'))
api.login(os.getenv('UPTIME_KUMA_USER'), os.getenv('UPTIME_KUMA_PASSWORD'))

with open('urls.txt', 'r') as f:
    for line in f:
        parsedUrl = urllib.parse.urlparse(line)
        if nsfw_check:
            checkName = urlclean(parsedUrl.netloc)
        else:
            checkName = parsedUrl.netloc

        urlCheck = line

        print("Working On: ", checkName)
        api.add_monitor(
            type=MonitorType.HTTP,
            name=checkName,
            description=parsedUrl.netloc,
            url=urlCheck,
            expiryNotification=True,
            headers={"cache-control": "no-cache"},
            interval=120,

        )
        print('-----------------------------------')

api.disconnect()
