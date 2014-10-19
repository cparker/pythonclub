__author__ = 'cparker'

import json,requests


urlText = requests.get(
    "http://ucas-build.lss.emc.com/jenkins/view/Raven%20-%20server/job/raven-launcher/api/json?pretty=true")
print(urlText)
