import boto3
import json
from botocore.config import Config

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    
    # 从请求体获取文件信息
    body = json.loads(event['body'])
    file_name = body['fileName']
    file_type = body['fileType']
    print(f"file_name: {str(file_name)}")
    print(f"file_name: {str(file_type)}")


    # 生成预签名URL
    presigned_url = s3_client.generate_presigned_url(
        'put_object',
        Params={
            'Bucket': 'upload-destination-bucket-shiyang',
            'Key': file_name,
            'ContentType': file_type
        },
        ExpiresIn=3600  # URL有效期1小时
    )
    print(f"presigned_url: {str(presigned_url)}")
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'uploadURL': presigned_url
        })
    }
