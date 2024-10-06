import json
import boto3

def lambda_handler(event, contxt):
    email=event.get('email')
    token=event.get('session')
    newPassword=event.get('newPassword')

    if email is None or token is None:
        return {
            'statusCode': 400,
            'body': json.dumps('No token provided')
        }
    
    cognitoIdp=boto3.client('cognito-idp')

    try:
        response=cognitoIdp.admin_set_user_password(
            UserPoolId='ap-northeast-1_Esw3Y4ZGN',
            Username=email,
            Password=newPassword,
            Permanent=True
        )

        return {
                'statusCode': 200,
                'body': json.dumps({
                'session': token,
                'message': 'complete change password'
                })
        }

    except Exception as e:
        print(e)
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Error changing password',
                'error': str(e)
            })
        }