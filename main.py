#!/usr/bin/env python3
import os
import base64
import yaml
from github import Github

# Github setup
token = os.environ['GITHUB_TOKEN']
g = Github(token)

repo = g.get_repo("alphagov/gsp-teams")
contents = repo.get_contents("clusters")

for file in contents:
	decoded = base64.b64decode(file.content)
	yamled = yaml.safe_load(decoded)
	print(yamled["cluster-name"])
