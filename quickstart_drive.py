from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token_drive.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token_drive.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token_drive.json'):
        creds = Credentials.from_authorized_user_file('token_drive.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token_drive.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        # Get the ID for recipe folder
        results = service.files().list(
            # This line will list folders in drive
            pageSize=10,
            fields="nextPageToken, files(id, name)",
            q="mimeType = 'application/vnd.google-apps.folder' and name = 'Recipes'")\
                .execute()
            # This line will list folders in folder '0B3VD078tlYCcOFJUOWtUQ1JGSDg' which is 'Recipes' ID
            # pageSize=pageSize, pageToken=nextPageToken, fields="nextPageToken, files(id, name)", q="'0B3VD078tlYCcOFJUOWtUQ1JGSDg' in parents").execute()
        items = results.get('files', [])
        # print(results.get('nextPageToken', 'BUTTS'))

        if len(items) == 1:
            recipe_id = items[0]['id']
            print('The Recipes ID is', recipe_id)
        else:
            raise Exception()
        
        # Get items within Recipe folder
        pageSize = 10
        items = []
        nextPageToken = None
        while nextPageToken != 'Failure':
            results = service.files().list(
                # This line will list items in folder with ID recipe_id in drive
                pageSize=pageSize,
                pageToken=nextPageToken,
                fields="nextPageToken, files(id, name)",
                q=f"'{recipe_id}' in parents")\
                    .execute()

            items += results.get('files', [])
            nextPageToken = results.get('nextPageToken', 'Failure')

        # Print recipes if they exist
        if not items:
            print('No files found.')
            return
        print('Files:')
        for index, item in enumerate(items):
            print(f"{index}, {item['name']}, {item['id']}")
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()