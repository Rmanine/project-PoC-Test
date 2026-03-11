import boto3
import os
from AwsDynamoApi import AwsDynamoApi

def lambda_handler(event, context):
    is_local = os.environ.get("AWS_SAM_LOCAL")
    
    dynamodb = boto3.resource(
        "dynamodb",
        endpoint_url="http://172.17.0.1:8000" if is_local else None,
        region_name="eu-north-1"
    )
    
    table = dynamodb.Table(os.environ["TABLE_NAME"])
    db = AwsDynamoApi(table)

    db =  AwsDynamoApi(table)

    route = event.get("routeKey")

    if route == "PUT /contacts":
        return db.add_contact(event)
    elif route == "GET /contacts/{contact_id}":
        return db.get_contact(event)
    elif route == "DELETE /contacts/{contact_id}":
        return db.delete_contact(event)
    elif route == "GET /contacts":
        return db.list_contacts(event)

    return {
        "statusCode": 400,
        "body": "Unsupported route"
    }
