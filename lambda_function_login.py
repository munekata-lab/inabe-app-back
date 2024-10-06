import json
import boto3

def lambda_handler(event, context):
  '''
  ログインAPIの実装
  '''
  email = event.get('email')
  password = event.get('password')

  if not (email and password):
    return {
      'status code' : 400,
      'message': 'failed to create user'
    }

  cognito_idp_client = boto3.client('cognito-idp')
  #cognitoのclientID
  client_id = 'your_client_id'

  try:
    response = cognito_idp_client.initiate_auth(
      AuthFlow = 'USER_PASSWORD_AUTH',
      AuthParameters = {
        'USERNAME' : email,
        'PASSWORD' : password
      },
      ClientId = client_id
    )

    jwt = response['AuthenticationResult']['AccessToken']
    return {
      'statuscode' : 200,
      'session' : jwt,
      'message' : 'complete create user'
    }

  except Exception as error:
    return {
      'statuscode': 400,
      'message' : str(error)
    }

