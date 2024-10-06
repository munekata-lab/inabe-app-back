import json
import boto3

def lambda_handler(event, context):
  '''
  メールアドレスでの登録APIの実装
  '''

  user_email = event.get('email')
  password = event.get('password')

  if not (user_email and password):
    return {
      'status code' : 400,
      'message': 'failed to create user'
    }

  cognito_idp_client = boto3.client('cognito-idp')

  try:
    kwargs = {
      #cognitoのclientID
      'ClientId' : 'your_client_id',
      'Username' : user_email,
      'Password' : password,
      'UserAttributes' : [{'Name': 'email', 'Value': user_email}]
    }

    response = cognito_idp_client.sign_up(**kwargs)

    return {
      'statuscode' : 200,
      'session' : 'jwt',
      'message' : 'complete create user'
    }

  except Exception as error:
    return {
      'statuscode': 400,
      'message' : str(error)
    }
