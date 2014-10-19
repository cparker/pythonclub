import json,subprocess

res2 = subprocess.Popen(["npm", "la", "--parseable"],stdout=subprocess.PIPE)
output,error = res2.communicate()

lines = output.split('\n')

cleanLines = filter(lambda l: ':' in l,lines)

trimmed = [line.split(':')[1] for line in cleanLines]

finalMap = {}
for nameVer in trimmed:
    finalMap[nameVer] = ''

print(len(finalMap.items()))

for item in sorted(finalMap):
    print(item)




