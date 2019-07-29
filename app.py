#!/usr/bin/env python
import json
import os

from aws_cdk import core

from deploy.deploy_stack import DeployStack

# generated from local-deploy.sh
stackname_file = 'stackname.json'
stackname = None
if os.path.exists(stackname_file):
    with open(stackname_file) as json_file:
        stackname = json.load(json_file)["stackname"]

# use user generated stackname or create one
if stackname is None:
    homedir = os.path.expanduser("~")  # /home/<username>
    cwd = os.getcwd()  # /my/path/to/projects
    owner = os.path.basename(os.path.normpath(homedir))
    project = os.path.basename(os.path.normpath(cwd))
    stackname = owner + "_" + project

# run it!
app = core.App()
DeployStack(app, stackname)

app.synth()
