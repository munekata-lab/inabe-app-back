import json
import boto3

def lambda_handler(event):
    token=event.get('session')
    print('token : ',token)
    if token is None:
        return {
            'statusCode': 400,
            'body': json.dumps('No token provided')
        }
    
    cognitoIdp=boto3.client('cognito-idp')

    try:
        response=cognitoIdp.global_sign_out(
            AccessToken=token
        )
        return {
        'statusCode': 200,
        'body': json.dumps('Logged out')
        }

    except Exception as e:
        print(e)
        return {
            'statusCode': 400,
            'body': json.dumps('Error logging out')
        }

    

if __name__ == '__main__':    
    lambda_handler({'session':'1234'})