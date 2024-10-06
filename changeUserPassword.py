import json
import boto3

def lambda_handler(event, contxt):
    email=event.get('email')
    token=event.get('session')
    prePassword=event.get('prePassword')
    newPassword=event.get('newPassword')

    if email is None or token is None:
        return {
            'statusCode': 400,
            'body': json.dumps('No token provided')
        }
    
    cognitoIdp=boto3.client('cognito-idp')

    try:
        response=cognitoIdp.change_password(
            PreviousPassword=prePassword,
            ProposedPassword=newPassword,
            AccessToken=token
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
            'statuscode': 400,
            'body': json.dumps({
                'message': 'Error changing password',
                'error': str(e)
            })
        }