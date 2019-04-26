# Add a slide at index 1 using the predefined 'TITLE_AND_TWO_COLUMNS' layout and
# the ID page_id.

from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


# Setup the Drive v3 API
#SCOPES = 'https://www.googleapis.com/auth/drive'

                                                                                  
SCOPES = 'https://www.googleapis.com/auth/presentations.readonly'

store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('drive', 'v3', http=creds.authorize(Http()))


PRESENTATION_ID = '1WhfjnD7YdxlMnIp0cMNgjFFq-y_KC8uqPSxAa1bz_9g'
page_id = 'g2a34597858_0_29'

presentation = service.presentations().get(presentationId=PRESENTATION_ID).execute()
slides = presentation.get('slides')

requests = [
    {
        'createSlide': {
            'objectId': page_id,
            'insertionIndex': '1',
            'slideLayoutReference': {
                'predefinedLayout': 'TITLE_AND_TWO_COLUMNS'
            }
        }
    }
]


print ('The presentation contains {} slides:'.format(len(slides)))
for i, slide in enumerate(slides):
    print('- Slide #{} contains {} elements.'.format(i + 1,
                                                     len(slide.get('pageElements'))))


# If you wish to populate the slide with elements, add element create requests here,
# using the page_id.

# Execute the request.
#body = {
#    'requests': requests
#}
#response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
#                                                      body=body).execute()
#create_slide_response = response.get('replies')[0].get('createSlide')

#print('Created slide with ID: {0}'.format(create_slide_response.get('objectId')))

