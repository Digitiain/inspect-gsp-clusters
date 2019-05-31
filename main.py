#!/usr/bin/env python3
import base64
import requests
import yaml
from github import Github

# Github setup
token = [bash variable]
g = Github(token)

repo = g.get_repo("https://api.github.com/repos/alphagov/gsp-teams/tree/master/clusters")

def yaml_filenames():
	# Get name of yaml files in repo

	yaml-files = []

	# Get all contents/files from repo
	contents = repo.get_contents("")

	# Get name of each file ending .yaml
	for content_file in contents:
		if ".yaml" or ".yml" in content_file:
			yaml-files.append(content_file)

	return yaml-files

def cluster_name(yaml-files):
	# Return all cluster names

	clusters = ()

	for file in yaml-files:
		file-content = yaml.load(file.content) # Might be base64 encoded
		cluster-name = file-content["cluster-name"]
		clusters.append(cluster-name)

	return clusters

def current_clusters(clusters):
	for i in clusters:
		print ("Cluster name: " & i) # Might need to be made string

# https://developer.github.com/v3/repos/contents/#get-contents
# GitHub API response for directory:

# [
#   {
#     "type": "file",
#     "size": 625,
#     "name": "octokit.rb",
#     "path": "lib/octokit.rb",
#     "sha": "fff6fe3a23bf1c8ea0692b4a883af99bee26fd3b",
#     "url": "https://api.github.com/repos/octokit/octokit.rb/contents/lib/octokit.rb",
#     "git_url": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/fff6fe3a23bf1c8ea0692b4a883af99bee26fd3b",
#     "html_url": "https://github.com/octokit/octokit.rb/blob/master/lib/octokit.rb",
#     "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/lib/octokit.rb",
#     "_links": {
#       "self": "https://api.github.com/repos/octokit/octokit.rb/contents/lib/octokit.rb",
#       "git": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/fff6fe3a23bf1c8ea0692b4a883af99bee26fd3b",
#       "html": "https://github.com/octokit/octokit.rb/blob/master/lib/octokit.rb"
#     }
#   },
#   {
#     "type": "dir",
#     "size": 0,
#     "name": "octokit",
#     "path": "lib/octokit",
#     "sha": "a84d88e7554fc1fa21bcbc4efae3c782a70d2b9d",
#     "url": "https://api.github.com/repos/octokit/octokit.rb/contents/lib/octokit",
#     "git_url": "https://api.github.com/repos/octokit/octokit.rb/git/trees/a84d88e7554fc1fa21bcbc4efae3c782a70d2b9d",
#     "html_url": "https://github.com/octokit/octokit.rb/tree/master/lib/octokit",
#     "download_url": null,
#     "_links": {
#       "self": "https://api.github.com/repos/octokit/octokit.rb/contents/lib/octokit",
#       "git": "https://api.github.com/repos/octokit/octokit.rb/git/trees/a84d88e7554fc1fa21bcbc4efae3c782a70d2b9d",
#       "html": "https://github.com/octokit/octokit.rb/tree/master/lib/octokit"
#     }
#   }
# ]

# GitHub API response for file:

# {
#   "type": "file",
#   "encoding": "base64",
#   "size": 5362,
#   "name": "README.md",
#   "path": "README.md",
#   "content": "encoded content ...",
#   "sha": "3d21ec53a331a6f037a91c368710b99387d012c1",
#   "url": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
#   "git_url": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
#   "html_url": "https://github.com/octokit/octokit.rb/blob/master/README.md",
#   "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md",
#   "_links": {
#     "git": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
#     "self": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
#     "html": "https://github.com/octokit/octokit.rb/blob/master/README.md"
#   }
# }
