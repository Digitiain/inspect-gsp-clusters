# inspect-gsp-clusters

A Flask app that displays information about [GSP](https://github.com/alphagov/gsp-teams) clusters running at [GDS](https://github.com/alphagov).

## Getting started

### Pre-requisites

- Python 3 (latest)
- Obtain a GitHub token with "read" permissions for repos

### Installation

1. Clone the repo

2. You may wish to set up a virtual environment:

  `python3 -m venv <virtual environment name>`

3. Activate the environment

  `source <virtual env name>/bin/activate`

4. Install requirements:

  `pip install -r requirements.txt`
  
  This installs Flask, PyGithub, PyYaml and their dependencies.
  
### Running the application

1. Activate you're virtual environment (if applicable):

  `source <virtual env name>/bin/activate`

2. Export environment variables:

```
 export GITHUB_TOKEN="<your github token>"
export FLASK_APP=main.py
export FLASK_ENVIRONMENT=development # don't do this in production!
```

3. Run the application

`flask run`\s
