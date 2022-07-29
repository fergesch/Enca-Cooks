# Enca-Cooks

# Goals
- List files from drive
- Read and render contents of files on site
- Make a site (flask template)
- Create/upload recipes to drive
- From site, add recipe ingredients to list (probably todoist)

# Create environment
- `conda env create -f environment.yml --prefix ./.venv`
- `conda activate /Users/michaelferguson/Github/Enca-Cooks/.venv` or `conda activate ./.venv`

# Flask App
- `/templates`
  - input template html files are 
- `app.py` 
  - routes for website

## To run locally
```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```


# Local Credentials
- Local credentials must be added to a `credentials.json` file which can be generated or downloaded here https://console.cloud.google.com/apis/credentials?project=enca-cooks
- Test users must be added to OAuth test users https://console.cloud.google.com/apis/credentials/consent?project=enca-cooks

# Important Links
| Link | Comment |
| - | - |
| https://developers.google.com/drive/api/v3/reference/files/list | Documentation for Google Drive list files/folders endpoint |
| https://developers.google.com/docs/api/reference/rest | Google docs rest api reference |
| https://developers.google.com/docs/api/reference/rest/v1/documents/get | Google docs get documentation |
| https://developers.google.com/docs/api/reference/rest/v1/documents/create | Google docs create documentation |
| https://github.com/googleapis/google-api-python-client | Google API github page |
| https://googleapis.github.io/google-api-python-client/docs/dyn/drive_v3.html | ugly google api docs |
