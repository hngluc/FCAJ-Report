---
title: "Triển khai"
date: 2026-07-20
weight: 3
chapter: false
pre: " <b> 8.3. </b> "
---

# Triển khai

### Bước 1: Thiết lập S3 Buckets

Tạo hai S3 buckets cho ứng dụng:
- `smart-image-platform-uploads` — cho ảnh gốc được tải lên
- `smart-image-platform-thumbnails` — cho ảnh thumbnail đã xử lý

**Các cấu hình chính:**
- Bật versioning để bảo vệ dữ liệu
- Cấu hình CORS cho frontend truy cập
- Thiết lập event notifications để kích hoạt Lambda khi `s3:ObjectCreated:*`

### Bước 2: Tạo DynamoDB Table

Tạo bảng DynamoDB tên `ImageMetadata`:

| Thuộc tính | Loại | Mô tả |
|-----------|------|-------|
| `imageId` (PK) | String | Định danh duy nhất cho mỗi ảnh |
| `userId` | String | Cognito user ID của người tải lên |
| `s3Key` | String | S3 object key cho ảnh gốc |
| `thumbnailKey` | String | S3 object key cho thumbnail |
| `uploadedAt` | String | Thời gian ISO 8601 |
| `labels` | List | Nhãn AI từ Rekognition |
| `status` | String | Trạng thái xử lý (UPLOADED, PROCESSING, COMPLETED) |

### Bước 3: Lambda Functions

#### Xử lý tải lên (`uploadImage`)
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
    
    # Tạo pre-signed URL để tải ảnh trực tiếp
    presigned_url = s3_client.generate_presigned_url(
        'put_object',
        Params={
            'Bucket': 'smart-image-platform-uploads',
            'Key': s3_key,
            'ContentType': 'image/jpeg'
        },
        ExpiresIn=300
    )
    
    # Lưu metadata
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

#### Xử lý ảnh (`processImage`)
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
    
    # Tải ảnh gốc
    response = s3_client.get_object(Bucket=bucket, Key=key)
    image_data = response['Body'].read()
    
    # Tạo thumbnail
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
    
    # Phân loại AI với Rekognition
    labels_response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        MaxLabels=10,
        MinConfidence=70
    )
    
    labels = [
        {'name': label['Name'], 'confidence': str(label['Confidence'])}
        for label in labels_response['Labels']
    ]
    
    # Cập nhật DynamoDB
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
    
    return {'statusCode': 200, 'body': 'Xử lý hoàn tất'}
```

### Bước 4: Thiết lập API Gateway

Tạo REST API với các endpoint sau:

| Method | Path | Lambda | Xác thực |
|--------|------|--------|----------|
| POST | `/images/upload` | `uploadImage` | Cognito |
| GET | `/images` | `getImages` | Cognito |
| GET | `/images/{imageId}` | `getImageDetail` | Cognito |

### Bước 5: Cấu hình Cognito

- Tạo User Pool với đăng ký bằng email
- Cấu hình chính sách mật khẩu (tối thiểu 8 ký tự, yêu cầu số)
- Thiết lập App Client cho React frontend
- Bật xác minh email

### Bước 6: Frontend với React & Amplify

Ứng dụng React bao gồm:
- **Trang Đăng nhập/Đăng ký** kết nối với Cognito
- **Dashboard** hiển thị ảnh đã tải lên với thumbnail
- **Trang tải ảnh** với chức năng kéo-thả
- **Trang chi tiết ảnh** hiển thị kết quả phân loại AI

> Tất cả mã nguồn mẫu ở trên được đơn giản hóa cho mục đích demo. Phiên bản triển khai thực tế bao gồm xử lý lỗi, kiểm tra đầu vào và các best practices về bảo mật.
