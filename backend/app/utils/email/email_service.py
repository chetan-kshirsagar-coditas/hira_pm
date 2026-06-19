import boto3
from app.core.config.config import settings
from fastapi import HTTPException, status


ses_client = boto3.client(
    'ses',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.REGION
)

class EmailService:
    
    @staticmethod
    def send_mail(receiever_address: str, subject: str, body: str):
        try:
            response = ses_client.send_email(
            Source=f'Team HIRA <{settings.SES_SENDER_MAIL}>',
            Destination={'ToAddresses': [receiever_address]},
            Message={
                'Subject': {'Data': subject},
                'Body': {
                    'Text': {'Data': body}
                    }
                }
            )
        except Exception as e:
            raise HTTPException(
                detail= f"Error occured while sending otp verification email.\n {e}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        return response