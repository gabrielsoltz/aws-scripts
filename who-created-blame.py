''' Find the Cloudtrail Create event for a speficic ResourceName '''

import boto3

ResourceName=""

client = boto3.client('cloudtrail')

response = client.lookup_events(
    LookupAttributes=[
        {
            'AttributeKey': 'ResourceName',
            'AttributeValue': ResourceName
        },
    ],
)

for event in response['Events']:
    if event['EventName'].startswith("Create"):
        print (event['EventName'], event['Username'], event['EventTime'])