import json
import boto3

def lambda_handler(event, context):
    email = event.get('email')
    confirmation_code = event.get('confirmation_code')

    if not (email and confirmation_code):
        return {
            'statuscode': 400,
            'message': 'Email and confirmation code are required'
        }

    cognito_idp_client = boto3.client('cognito-idp')
    client_id = '5j2mq7t78sbp2lh3uoj5ne4j0s'

    try:
        # Confirm the user's account
        response = cognito_idp_client.confirm_sign_up(
            ClientId=client_id,
            Username=email,
            ConfirmationCode=confirmation_code
        )

        return {
            'statuscode': 200,
            'message': 'Account confirmed successfully'
        }

    except Exception as error:
        return {
            'statuscode': 400,
            'message': str(error)
        }
