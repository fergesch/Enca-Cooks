# Data Sync

Possibly use a Functions component to sync data between Firestore and Google Drive

### Setting up local backend
- Change directory to `./backend`
- Run `./env_config.sh`
- To activate virtual environment `source ./.venv/bin/activate`

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
