import json
import boto3
import base64
from PIL import Image
import io
import uuid

s3 = boto3.client('s3')
S3_BUCKET = 'S3-backet'  # ここにS3バケット名を入力
CLOUDFRONT_DOMAIN = 'your-cloudfront-domain'  # ここにCloudFrontのドメイン名を入力（例：d1234abcd.cloudfront.net）

def lambda_handler(event, context):
    # TODO implement
    try:
        # リクエストボディから画像データを取得
        image_data = event['image_data']  # Base64エンコードされた画像データ
        if image_data.startswith('data:image'):
            image_data = image_data.split(',')[1]

        # 画像データをデコード
        image_bytes = base64.b64decode(image_data)

        # ユニークなファイル名を生成
        filename = f"{uuid.uuid4()}.jpg"

        # S3に画像をアップロード
        s3.upload_fileobj(
            image_bytes,
            S3_BUCKET,
            filename,
            ExtraArgs={
                'ContentType': 'image/jpeg',
                'ACL': 'private'  # オブジェクトを非公開に設定
            }
        )

        # 画像のCloudFront経由のURLを作成
        image_url = f"https://{CLOUDFRONT_DOMAIN}/{filename}"

        return {
            'statusCode': 200,
            'body': json.dumps({'image_url': image_url})
        }

    except Exception as error:
        return {
            'statusCode': 400,
            'error': str(error),
        }
