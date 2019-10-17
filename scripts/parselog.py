#!/usr/bin/python3

import json
import yaml

dumpme = {"errorips": []}

## open files/log.example
## pares files/log.exaple for ERROR and collect second item in the line (IP)
## store in dictionary  {'errorips': [list of IPs]}

with open("/home/student/ans/files/log.example") as lef:
    for line in lef:
        if "ERROR" in line:
            loggedip = line.split()[1]
            dumpme['errorips'].append(loggedip)

## dump (print) collected IPs out as json

#print(json.dumps(dumpme))
#print(yaml.dump(dumpme))
#print(dumpme)

with open("/home/student/ans/files/parsed.ips", "w") as iif:
    iif.write(yaml.dump(dumpme))
