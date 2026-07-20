---
title: "Kiến trúc & Thiết kế"
date: 2026-07-20
weight: 2
chapter: false
pre: " <b> 8.2. </b> "
---

# Kiến trúc & Thiết kế

### Kiến trúc hệ thống

Smart Image Platform sử dụng **Kiến trúc Serverless & Hướng sự kiện (Event-Driven)** trên AWS. Cách tiếp cận này loại bỏ nhu cầu quản lý máy chủ, cung cấp khả năng tự động mở rộng và đảm bảo hiệu quả chi phí (trả theo mức sử dụng).

```
Người dùng → Amplify (React Frontend) → API Gateway → Lambda → DynamoDB
                                                          ↓
                                                  S3 (Lưu trữ ảnh)
                                                          ↓
                                              S3 Event Notification
                                                          ↓
                                              Lambda (Xử lý ảnh)
                                                          ↓
                                              Rekognition (Phân loại AI)
                                                          ↓
                                              DynamoDB (Lưu kết quả)
```

### Các thành phần kiến trúc

#### 1. Tầng Frontend
- **AWS Amplify**: Hosting ứng dụng web React.js
- Cung cấp pipeline CI/CD với auto-deploy từ GitHub
- Hỗ trợ tên miền tùy chỉnh và quản lý chứng chỉ SSL

#### 2. Tầng Xác thực
- **Amazon Cognito**: Quản lý đăng ký, đăng nhập và quản lý phiên người dùng
- Hỗ trợ xác minh email và chính sách mật khẩu
- JWT tokens cho xác thực API

#### 3. Tầng API
- **Amazon API Gateway**: Các endpoint RESTful API
- Tích hợp Cognito Authorizer để bảo mật truy cập
- Cấu hình CORS cho giao tiếp frontend

#### 4. Tầng Compute
- **AWS Lambda**: Các hàm serverless viết bằng Python
  - `uploadImage`: Xử lý yêu cầu tải ảnh, tạo pre-signed URLs
  - `processImage`: Kích hoạt bởi sự kiện S3, thay đổi kích thước ảnh và tạo thumbnail
  - `classifyImage`: Gọi Rekognition API để phân loại ảnh bằng AI
  - `getImages`: Lấy metadata ảnh và kết quả phân loại

#### 5. Tầng Lưu trữ
- **Amazon S3**: Lưu trữ đối tượng cho ảnh gốc, thumbnail và ảnh đã xử lý
- Bucket policies và cấu hình CORS
- Event notifications để kích hoạt Lambda functions

#### 6. Tầng Cơ sở dữ liệu
- **Amazon DynamoDB**: Cơ sở dữ liệu NoSQL cho metadata ảnh
- Lưu trữ: image ID, thời gian tải lên, S3 key, nhãn phân loại, điểm tin cậy

#### 7. Tầng AI/ML
- **Amazon Rekognition**: Dịch vụ AI đã được huấn luyện sẵn cho phân tích ảnh
- Phát hiện nhãn, đối tượng, cảnh vật và hoạt động trong ảnh
- Trả về điểm tin cậy cho mỗi nhãn được phát hiện

### Các quyết định thiết kế

| Quyết định | Lựa chọn | Lý do |
|------------|----------|-------|
| Kiến trúc | Serverless | Không cần quản lý server, tự động mở rộng, tiết kiệm chi phí |
| Cơ sở dữ liệu | DynamoDB | Độ trễ thấp, NoSQL có khả năng mở rộng cho metadata |
| Dịch vụ AI | Rekognition | Đã huấn luyện sẵn, không cần chuyên môn ML |
| Frontend Hosting | Amplify | CI/CD tích hợp, triển khai dễ dàng |
| Ngôn ngữ | Python 3.12 | Hỗ trợ AWS SDK phong phú, phù hợp Lambda |

> Kiến trúc được thiết kế với mục tiêu khả năng mở rộng, hiệu quả chi phí và dễ bảo trì, tuân theo các nguyên tắc AWS Well-Architected Framework.
