# uploadfile-site-demo

## demo function
  - upload file via a web portal to s3 bucket
  - send message to email address when there is file uploaded to s3 bucket

## architecture diagram

## deployment guidance
  - 1. create two s3 bucket, one is for static s3 website (e.g. website-bucket-shiyang), one is file uploading destination (e.g. upload-destination-bucket-shiyang).
  - 2. **Permissions Tab**

       config the two s3 buckets' Block Public Access to **off** as per snapshot shown below.
       <img width="1213" alt="Screenshot 2025-03-08 at 14 52 52" src="https://github.com/user-attachments/assets/9d676233-2e8b-46ce-bb5b-05b9e7065da7" />
  - 3. **Permissions Tab**

       config bucket website-bucket-shiyang's bucket policy per below json.
        ```json
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "PublicReadGetObject",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::website-bucket-shiyang/*"
                }
            ]
        }
        ```
        config bucket upload-destination-bucket-shiyang's bucket policy per below json
        ```json
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "AllowPutObject",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:PutObject",
                    "Resource": "arn:aws:s3:::upload-destination-bucket-shiyang/*"
                }
            ]
        }
        ```
        config bucket upload-destination-bucket-shiyang's Cross-origin resource sharing (CORS) per below json
        ```json
        [
            {
                "AllowedHeaders": [
                    "*"
                ],
                "AllowedMethods": [
                    "PUT",
                    "POST",
                    "GET",
                    "HEAD"
                ],
                "AllowedOrigins": [
                    "*"
                ],
                "ExposeHeaders": [
                    "ETag"
                ]
            }
        ]
        ```        

        
  - 4. **Properties Tab**

       enable bucket website-bucket-shiyang's Static Web Hosting
       <img width="1208" alt="Screenshot 2025-03-08 at 14 59 50" src="https://github.com/user-attachments/assets/d7a4ce4a-6b98-4b59-a496-a693e59a97a9" />
  - 5. create lambda using Python, the code per
       [lambda.py](https://github.com/symeta/uploadfile-site-demo/blob/main/lambda.py)

       - config lambda permissions, attach inline policy to the default lambda IAM role
          ```json
          {
          	"Version": "2012-10-17",
          	"Statement": [
          		{
          			"Effect": "Allow",
          			"Action": [
          				"s3:PutObject",
          				"s3:GetObject"
          			],
          			"Resource": [
          				"arn:aws:s3:::upload-destination-bucket-shiyang/*"
          			]
          		}
          	]
          }
          ```
  - 6. create api gateway
       - Create a new REST API
       - Create POST method
       - Integrate Lambda function
       - Enable CORS
       - Deploy API to stage
      


## demo video
