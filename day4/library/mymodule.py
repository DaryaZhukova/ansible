#!/usr/bin/python

DOCUMENTATION = '''
---
module: mymodule
version_added: historical
short_description: Simple Ansible Module written on Python

description:
    - This module tests jenkins and httpd
autor:
    - "Darya Zhukova"
'''

EXAMPLES = """
# ansible webservers -inventory -m mymodule -a "procname=httpd"
- returns port listened by httpd
  
"""


from ansible.module_utils.basic import AnsibleModule
import psutil
import json
import requests


def checkuser(user, procname):
    flag = False
    for proc in psutil.process_iter(attrs=['name', 'username']):
        if proc.info['name'] == procname:
            if proc.info['username'] == user:
                flag = True
    if flag == True:
        print(json.dumps({"proper user started": procname}))


def getport(procname):
    orig = dict()
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == procname:
            p = psutil.Process(proc.info['pid'])
            for con in p.connections():
                orig["port"] = con.laddr[1]


            print(json.dumps(orig))
            break

def findcontext(myurl, cont):
    r = requests.get(myurl)
    if cont in r.text:
        print(json.dumps({"finded": cont}))


def findserver(myurl, cont):
    r = requests.get(myurl)
    if cont in r.text:
        print(json.dumps({"finded": cont}))


module = AnsibleModule(
    argument_spec=dict(
        myurl=dict(required=False, type=str, default=None),
        cont=dict(required=False, type=str, default=None),
        headcont=dict(required=False, type=str, Default=None),
        procname=dict(required=False, type=str, Default=None),
        user=dict(required=False, type=str, Default=None)
    )
)
if module.params['user'] != None and module.params['procname'] != None:
    checkuser(module.params['user'], module.params['procname'])
if module.params['user'] == None and module.params['procname'] != None:
    getport(module.params['procname'])
if module.params['myurl'] != None and module.params['cont'] != None:
    findcontext(module.params['myurl'], module.params['cont'])
if module.params['myurl'] != None and module.params['headcont'] != None:
    findcontext(module.params['myurl'], module.params['headcont'])
