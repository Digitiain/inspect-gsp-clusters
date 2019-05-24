#!/usr/bin/env python3
import base64
import requests

baseurl = 'https://api.github.com/repos/alphagov/gsp-teams/tree/master/clusters'


def get-gsp-clusters():

	# get all of the contents of all of the files in the repo

	req = requests.get(baseurl)
	if req.status_code == requests.codes.ok:
	    req = req.json()  # the response is a JSON
	    # req is now a dict with keys: name, encoding, url, size ...
	    # and content. But it is encoded with base64.
	    content = base64.decodestring(req['content'])
	else:
	    print('Content was not found.')

	# iterate through files 
	# if they end .yaml, add them to a list

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


	# iterate through list of yaml file names
	# append name to GitHub API GET request
	# go through content and find cluster-name
	# add cluster-name to list

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

	
	# for now, just print out the names of the clusters
