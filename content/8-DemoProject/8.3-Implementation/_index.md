---
title: "Implementation"
date: 2026-07-20
weight: 3
chapter: false
pre: " <b> 8.3. </b> "
---

# Implementation

### Step 1: Setting Up S3 Buckets

Create two S3 buckets for the application:
- `smart-image-platform-uploads` — for original uploaded images
- `smart-image-platform-thumbnails` — for processed thumbnails

**Key configurations:**
- Enable versioning for data protection
- Configure CORS for frontend access
- Set up event notifications to trigger Lambda on `s3:ObjectCreated:*`

### Step 2: Creating DynamoDB Table

Create a DynamoDB table named `ImageMetadata`:

| Attribute | Type | Description |
|-----------|------|-------------|
| `imageId` (PK) | String | Unique identifier for each image |
| `userId` | String | Cognito user ID of the uploader |
| `s3Key` | String | S3 object key for the original image |
| `thumbnailKey` | String | S3 object key for the thumbnail |
| `uploadedAt` | String | ISO 8601 timestamp |
| `labels` | List | AI-detected labels from Rekognition |
| `status` | String | Processing status (UPLOADED, PROCESSING, COMPLETED) |

### Step 3: Lambda Functions

#### Upload Handler (`uploadImage`)
```python
import json
import boto3
import uuid
from datetime import datetime

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageMetadata')

def lambda_handler(event, context):
    user_id = event['requestContext']['authorizer']['claims']['sub']
    image_id = str(uuid.uuid4())
    s3_key = f"uploads/{user_id}/{image_id}.jpg"
    
    # Generate pre-signed URL for direct upload
    presigned_url = s3_client.generate_presigned_url(
        'put_object',
        Params={
            'Bucket': 'smart-image-platform-uploads',
            'Key': s3_key,
            'ContentType': 'image/jpeg'
        },
        ExpiresIn=300
    )
    
    # Save metadata
    table.put_item(Item={
        'imageId': image_id,
        'userId': user_id,
        's3Key': s3_key,
        'uploadedAt': datetime.utcnow().isoformat(),
        'status': 'UPLOADED'
    })
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'imageId': image_id,
            'uploadUrl': presigned_url
        })
    }
```

#### Image Processor (`processImage`)
```python
import boto3
from PIL import Image
import io

s3_client = boto3.client('s3')
rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageMetadata')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Download original image
    response = s3_client.get_object(Bucket=bucket, Key=key)
    image_data = response['Body'].read()
    
    # Create thumbnail
    image = Image.open(io.BytesIO(image_data))
    image.thumbnail((200, 200))
    
    thumb_buffer = io.BytesIO()
    image.save(thumb_buffer, 'JPEG')
    thumb_buffer.seek(0)
    
    thumb_key = key.replace('uploads/', 'thumbnails/')
    s3_client.put_object(
        Bucket='smart-image-platform-thumbnails',
        Key=thumb_key,
        Body=thumb_buffer,
        ContentType='image/jpeg'
    )
    
    # AI Classification with Rekognition
    labels_response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        MaxLabels=10,
        MinConfidence=70
    )
    
    labels = [
        {'name': label['Name'], 'confidence': str(label['Confidence'])}
        for label in labels_response['Labels']
    ]
    
    # Update DynamoDB
    image_id = key.split('/')[-1].replace('.jpg', '')
    table.update_item(
        Key={'imageId': image_id},
        UpdateExpression='SET #s = :s, thumbnailKey = :tk, labels = :l',
        ExpressionAttributeNames={'#s': 'status'},
        ExpressionAttributeValues={
            ':s': 'COMPLETED',
            ':tk': thumb_key,
            ':l': labels
        }
    )
    
    return {'statusCode': 200, 'body': 'Processing complete'}
```

### Step 4: API Gateway Setup

Create a REST API with the following endpoints:

| Method | Path | Lambda | Auth |
|--------|------|--------|------|
| POST | `/images/upload` | `uploadImage` | Cognito |
| GET | `/images` | `getImages` | Cognito |
| GET | `/images/{imageId}` | `getImageDetail` | Cognito |

### Step 5: Cognito Configuration

- Create a User Pool with email sign-up
- Configure password policy (minimum 8 characters, require numbers)
- Set up App Client for the React frontend
- Enable email verification

### Step 6: Frontend with React & Amplify

The React application includes:
- **Login/Register pages** connected to Cognito
- **Dashboard** showing uploaded images with thumbnails
- **Upload page** with drag-and-drop functionality
- **Image detail page** displaying AI classification results

> All code samples above are simplified for demonstration purposes. The actual implementation includes error handling, input validation, and security best practices.
