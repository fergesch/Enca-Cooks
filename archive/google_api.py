from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = [
    # 'https://www.googleapis.com/auth/drive.metadata.readonly',
    'https://www.googleapis.com/auth/drive',
    #   'https://www.googleapis.com/auth/documents.readonly',
    'https://www.googleapis.com/auth/documents'
]


def check_token():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return(creds)


def get_recipe_folder():
    try:
        creds = check_token()
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
            recipe_folder = items[0]['id']
            # print('The Recipe Folder ID is', recipe_folder)
            return(recipe_folder)
        else:
            raise Exception()
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


def get_recipes(recipe_folder):
    try:
        creds = check_token()
    # Get items within Recipe folder
        service = build('drive', 'v3', credentials=creds)

        pageSize = 10
        items = []
        nextPageToken = None
        while nextPageToken != 'Failure':
            results = service.files().list(
                # This line will list items in folder with ID recipe_id in drive
                pageSize=pageSize,
                pageToken=nextPageToken,
                fields="nextPageToken, files(id, name)",
                q=f"'{recipe_folder}' in parents")\
                .execute()

            items += results.get('files', [])
            nextPageToken = results.get('nextPageToken', 'Failure')

        # Print recipes if they exist
        if not items:
            raise Exception('No files found')
        return(items)
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


def get_recipe(recipe_id):
    try:
        creds = check_token()
        service = build('docs', 'v1', credentials=creds)

        # Retrieve the documents contents from the Docs service.
        document = service.documents().get(documentId=recipe_id).execute()

        recipe_dict = {
            'ingredients': [],
            'instructions': []
        }
        section = None
        for i in document.get('body').get('content')[1:]:
            l = ''.join([j.get('textRun', {}).get('content')
                        for j in i.get('paragraph', {}).get('elements')]).rstrip()
            if l.lower() in recipe_dict.keys():
                section = l.lower()
            elif section and len(l) > 0:
                recipe_dict[section].append(l)

        return(recipe_dict)
        # print('The title of the document is: {}'.format(document.get('title')))
    except HttpError as err:
        print(err)


def get_all_recipes():
    recipe_folder = get_recipe_folder()
    recipes = get_recipes(recipe_folder)
    return(recipes)


def create_recipe(recipe_folder: str, title: str):
    creds = check_token()
    service = build('docs', 'v1', credentials=creds)

    document = service.documents().create(body={'title': title}).execute()

    service = build('drive', 'v3', credentials=creds)
    service.files().update(
        fileId=document['documentId'], addParents=recipe_folder).execute()

    return(document['documentId'])


def fill_recipe(document_id, recipe_dict):
    creds = check_token()
    service = build('docs', 'v1', credentials=creds)

    bullet_dict = {
        'ingredients': 'BULLET_DISC_CIRCLE_SQUARE',
        'instructions': 'NUMBERED_DECIMAL_ALPHA_ROMAN'
    }

    body_dict = {
        'requests': []
    }
    index = 1
    for key in recipe_dict.keys():
        val = f"{key.capitalize()}\n"
        body_dict['requests'].append(
            {"insertText": {"endOfSegmentLocation": {}, "text": val}}
        )
        index += len(val)

        start_index = index
        for i in recipe_dict[key]:
            val = f"{i.capitalize()}\n"
            index += len(val)
            body_dict['requests'].append(
                {"insertText": {"endOfSegmentLocation": {}, "text": val}}
            )
        body_dict['requests'].append(
            {
                "createParagraphBullets": {
                    "range": {"startIndex": start_index, "endIndex": index},
                    "bulletPreset": bullet_dict[key]
                }
            }
        )
    service.documents().batchUpdate(documentId=document_id, body=body_dict).execute()


def main():
    recipe_folder = get_recipe_folder()
    print('The Recipe Folder ID is', recipe_folder)

    recipes = get_recipes(recipe_folder)
    for i in recipes:
        print(i)

    recipe = get_recipe(recipes[0]['id'])
    print(recipe)

    new_recipe = create_recipe(recipe_folder, 'python food')
    print('New recipe', new_recipe)

    recipe_dict = {
        'ingredients': [
            '1 cup sugar',
            '1/2 cup cocoa powder',
            '1 stick butter'
        ],
        'instructions': [
            'melt some stuff',
            'mix a thing',
            'bake it baby'
        ]
    }
    fill_recipe(new_recipe, recipe_dict)


if __name__ == '__main__':
    main()
