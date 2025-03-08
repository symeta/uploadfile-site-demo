# uploadfile-site-demo

## demo function
  - upload file via a web portal to s3 bucket
  - send message to email address when there is file uploaded to s3 bucket

## architecture diagram

## deployment guidance
  - 1. create two s3 bucket, one is for static s3 website (e.g. website-bucket-shiyang), one is file uploading destination (e.g. upload-destination-bucket-shiyang).
  - 2. config the two s3 buckets' Block Public Access to **off** as per snapshot shown below.
       <img width="1213" alt="Screenshot 2025-03-08 at 14 52 52" src="https://github.com/user-attachments/assets/9d676233-2e8b-46ce-bb5b-05b9e7065da7" />
  - 3. config bucket website-bucket-shiyang's bucket policy per below json.
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

## demo video
