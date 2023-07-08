import json

def lambda_handler(event, context):
    http_method = event['httpMethod']
    path = event['path']
    
    if http_method == 'GET' and path == '/':
        return {
            'statusCode': 200,
            'body': json.dumps('Hello, World!')
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('Rota não encontrada.')
        }
