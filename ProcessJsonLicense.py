#!/usr/bin/env python
"""
Given the output of npm ll --json, of a node package, uses npm view to gather license information
of third-party transitive dependencies.  Outputs a .csv for submission to EMC legal.  Gathers information
from the following 3 sources. Higher number overrides a lower:

1. an optional supplementary license file
2. the specified npm_list_json_file
3. npm view <package name>

Usage:
    RavenNodeLicenseReport.py <npm_list_json_file> <output_csv_file> [--dev-team=Ibis] [--license-data=foo.json]

Arguments:
    npm_list_json_file          The output of running npm ll --json on a project
    output_csv_file             Specify an output file, like license-report.csv

Options:
    -h --help                   show this
    -ld --license-data=<file>   specify a .json file of supplementary license data when we can't get it from npm
    -dt --dev-team=<name>       include your team name in the license report's Dev Team column


License Data:
    The supplementary license data file should be one JSON object where keys are package names like "express", and
    values are json objects with properties you want merged in, like "license", "url", etc.
"""

__author__ = 'cparker'

import json, subprocess, sys, csv
from docopt import docopt
import collections
from collections import defaultdict
import string
from string import Formatter


l = "license"
ls = "licenses"

ignoreDepNames = [
    # these are EMC npm packages, so they shouldn't be a part of the report
    "node-commons",
    "emc-base-server",
    "emc-rest-login",
    "raven-shared-types",
    "emc-shared-types"
]


def dumpObj(d):
    print(json.dumps(d, sort_keys=True, indent=2))


def easyToString(x):
    if type(x) is dict or type(x) is list:
        return json.dumps(x, sort_keys=True)
    else:
        return unicode(x)


class BlankFormatter(string.Formatter):
    def __init__(self, default=''):
        self.default = default

    def get_value(self, key, args, kwds):
        if isinstance(key, str):
            return kwds.get(key, self.default)
        else:
            Formatter.get_value(key, args, kwds)


fmt = BlankFormatter()


def extractDotKey(rec, key, default=''):
    value = rec
    for name in key.split("."):
        if name in value:
            value = value[name]
        else:
            return default
    return value


def beautifyLicense(license):
    if type(license) is str or type(license) is unicode:
        return license.strip()
    elif license is None:
        return ""
    elif type(license) is dict:
        return fmt.format("{type}:{url}", **license).strip()
    elif type(license) is list:
        return ":".join(map(beautifyLicense, license)).strip()

finalLicenses = {}


# recursively process specified npm json
def digDependencies(recWithDependencies, supplementaryLicenseData):
    for key in recWithDependencies.keys():
        itemInfo = {}

        if type(recWithDependencies[key]) is dict:
            localRec = recWithDependencies[key]
        else:
            localRec = {}

        name = localRec.get('name', key)
        checkEmcLicense = localRec.get('license', '')

        # skip over certain packages, namely our own EMC dependencies
        if name in ignoreDepNames or checkEmcLicense == 'EMC':
            continue

        # use npm view to search the interwebs
        try:
            npmViewData = json.loads(subprocess.check_output(["npm", "view", "--json", name]))
        except:
            print("npm view failed for " + name)
            npmViewData = {}

        # merge the data together from three sources, RIGHT MOST wins
        thisRec = dict(supplementaryLicenseData.get(name, {}).items() + localRec.items() + npmViewData.items())

        version = thisRec.get('version')
        finalLicenseMapKey = name + version

        fieldsToKeep = [
            "version",
            "name",
            "licenses",
            "license",
            "author",
            "homepage",
            "repository.url",
            "description"
        ]

        for field in fieldsToKeep:
            itemInfo[field] = extractDotKey(thisRec, field)

        prettyLicense = beautifyLicense(itemInfo.get('license'))
        prettyLicenses = beautifyLicense(itemInfo.get('licenses'))

        itemInfo['license'] = (prettyLicense + " " + prettyLicenses).strip()
        itemInfo['licenses'] = ""

        finalLicenses[finalLicenseMapKey] = itemInfo

        if (type(thisRec) is collections.defaultdict or type(thisRec) is dict) and 'dependencies' in thisRec:
            digDependencies(thisRec['dependencies'], supplementaryLicenseData)

    return finalLicenses


def concatMapFieldsAsString(dict, *fields):
    res = ""
    for field in fields:
        if dict.get(field) is not None:
            res += easyToString(dict.get(field, '')) + " "
    return res.encode('ascii','replace').strip()


def outputCSVrow(dependencyMap, dictWriter, devTeam=''):
    dumpObj(dependencyMap)
    outMap = {}
    outMap[headers[0]] = concatMapFieldsAsString(dependencyMap, 'repository.url', 'homepage')
    outMap[headers[1]] = dependencyMap.get('name', '').encode('ascii','replace')
    outMap[headers[2]] = dependencyMap.get('version', '').encode('ascii','replace')
    outMap[headers[3]] = concatMapFieldsAsString(dependencyMap, 'licenses', 'license')
    outMap[headers[4]] = dependencyMap.get('description', '').encode('ascii','replace')
    outMap[headers[5]] = concatMapFieldsAsString(dependencyMap, 'description', 'author')
    outMap[headers[6]] = 'n'
    outMap[headers[7]] = 'y'
    outMap[headers[8]] = 'javascript'
    outMap[headers[9]] = 'y'
    outMap[headers[10]] = 'dynamic'
    outMap[headers[11]] = 'n/a'
    outMap[headers[12]] = ''
    outMap[headers[13]] = devTeam

    dictWriter.writerow(outMap)


# main processing begins here
# handle command-line options
headers = [
    'URL',
    'NAME',
    'VERSION',
    'LICENSE',
    'DESCRIBE USE',
    'DETAILED DESCRIPTION',
    'MODIFYING',
    'DISTRIBUTING',
    'LANGUAGE',
    'LINKING WITH EMC CODE',
    'TYPE OF LINKING',
    'HOW USED',
    'EMC LEVEL',
    'DEV TEAM'
]

cli = docopt(__doc__)

licenceFile = open(cli['<npm_list_json_file>'])
npmLicenseJson = json.loads(licenceFile.read())


# read in supplementary license data, or setup an empty hash
if '--license-data' in cli:
    f = open(cli['--license-data'], "r")
    supplementaryLicenseData = json.loads(f.read())
    f.close()
else:
    supplementaryLicenseData = {}

finalLicenseMap = digDependencies(npmLicenseJson['dependencies'], supplementaryLicenseData)
outputFile = open(cli['<output_csv_file>'], "w")
dWriter = csv.DictWriter(outputFile, fieldnames=headers, extrasaction="ignore")
dWriter.writeheader()

for k, v in finalLicenseMap.items():
    outputCSVrow(v, dWriter, cli.get('--dev-team', ''))

outputFile.close()

# now examine our map and report missing license info:
def findMissingLicenses(tuple):
    mapValue = tuple[1]
    dumpObj(mapValue)
    if easyToString(mapValue.get('license', '')) + easyToString(mapValue.get('licenses', '')) == '':
        return True
    else:
        return False


missingLicenses = filter(findMissingLicenses, finalLicenseMap.items())

if len(missingLicenses) > 0:
    for mis in missingLicenses:
        print(fmt.format("missing license for {name} {url} {homepage}", **mis[1]))
    sys.exit(1)





