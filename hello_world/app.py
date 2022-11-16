import json

# import requests


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
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
            "statusCode": 200,
            "body": "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\" /><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" /><link rel=\"stylesheet\" href=\"style.css\" /><title>Proyecto Integrador</title></head><body><h1>Proyecto Integrador: Uso de GitHub Actions para implementar aplicaciones serverless</h1><p>En esta página se puede comprobar que se realizó el deployment del código.</p><img src=\"https://media.tenor.com/mhKBv0wFQQ0AAAAC/happy-dwight.gif\" alt=\"Happy Dwight\"></body></html>",
            "headers": {
                'Content-Type': 'text/html',
            }
    }
