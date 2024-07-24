import boto3
import uuid

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Generate a new GUID (UUID) for the id field
    new_id = str(uuid.uuid4())

    # Extract data from the event (assuming it's coming from an API Gateway)
    data = event['body']
    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject')
    message = data.get('message')

    # Define the DynamoDB table name
    table_name = 'YourTableName'

    # Create a new item to add to DynamoDB
    item = {
        'id': {'S': new_id},
        'name': {'S': name},
        'email': {'S': email},
        'subject': {'S': subject},
        'message': {'S': message}
    }

    # Add the item to DynamoDB
    try:
        response = dynamodb.put_item(
            TableName=table_name,
            Item=item
        )
        return {
            'statusCode': 200,
            'body': 'Record added to DynamoDB successfully'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': 'Error adding record to DynamoDB: ' + str(e)
        }
