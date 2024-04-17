import base64
import csv
import json
import os
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
    print('### Received event')
    

    try:
        post_data = event.get('body', '')
        
        if event.get('isBase64Encoded', False):
            post_data = base64.b64decode(post_data).decode('utf-8')
        
        parsed_data = parse_qs(post_data)
        
        # The values in parsed_data are lists, convert them to single values
        parsed_data = {k: v[0] for k, v in parsed_data.items()}
        
        lookup_value = parsed_data.get('text', '').lower()

        if 'AWS_EXECUTION_ENV' in os.environ:
            # On AWS Lambda, the file is in the same directory as this script
            csv_file_path = 'acronyms.csv'
        else:
            # On your local machine, the file is in the project root directory
            csv_file_path = os.path.join(os.path.dirname(__file__), 'acronyms.csv')
        
        with open(csv_file_path, mode='r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            
            # Iterate over the rows in the CSV
            for row in csv_reader:
                acronym = row['Acronym'].lower()
                
                # Check if the lookup value matches the 'Acronym' column
                if acronym == lookup_value:
                    # If a match is found, retrieve the definition and description
                    definition = row['Definition']
                    description = row['Description']
                    
                    # Handle the case where the description might be blank
                    if not description:
                        description = ' '
                    
                    # Return the result in the desired JSON format
                    return {
                        'statusCode': 200,
                        'body': json.dumps({
                            'blocks': [
                                {
                                    'type': 'section',
                                    'text': {
                                        'type': 'mrkdwn',
                                        'text': f'*{definition}*'
                                    }
                                },
                                {
                                    'type': 'section',
                                    'text': {
                                        'type': 'mrkdwn',
                                        'text': f'_{row["Acronym"].upper()}_'
                                    }
                                },
                                {
                                    'type': 'section',
                                    'text': {
                                        'type': 'mrkdwn',
                                        'text': description
                                    }
                                }
                            ]
                        }),
                        'headers': {
                            'Content-Type': 'application/json'
                        }
                    }
            
            # If no match is found after iterating all rows
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'blocks': [
                        {
                            'type': 'section',
                            'text': {
                                'type': 'mrkdwn',
                                'text': "That's a new one!"
                            }
                        }
                    ]
                }),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error processing form data',
                'error': str(e)
            })
        }
    