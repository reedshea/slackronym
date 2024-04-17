import json
from urllib.parse import parse_qs

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    Lambda Function URL Output Format: dict

    """
    print('Received event')
    print(event)
    json_string = json.dumps(event)
    print(json_string)
    
    try:
        post_data = event.get('body', '')
        
        if event.get('isBase64Encoded', False):
            import base64
            post_data = base64.b64decode(post_data).decode('utf-8')
        
        parsed_data = parse_qs(post_data)


        return {
            "statusCode": 200,
            "body": json.dumps(parsed_data)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error processing form data',
                'error': str(e)
            })
        }