---
title: "Tổng quan dự án"
date: 2026-07-20
weight: 1
chapter: false
pre: " <b> 8.1. </b> "
---

# Tổng quan dự án

### Tên dự án
**Smart Image Platform Demo**

### Vấn đề cần giải quyết

Trong nhiều tình huống thực tế, việc quản lý và phân loại khối lượng lớn hình ảnh thủ công rất tốn thời gian và dễ xảy ra sai sót. Dự án demo này giải quyết vấn đề đó bằng cách xây dựng một giải pháp serverless tự động, tận dụng các dịch vụ AI của AWS để phân loại hình ảnh thông minh.

### Mục tiêu

- Xây dựng một ứng dụng hoàn toàn serverless trên AWS
- Triển khai xử lý ảnh tự động (thay đổi kích thước, tạo thumbnail)
- Tích hợp phân loại ảnh bằng AI sử dụng Amazon Rekognition
- Thực hành các nguyên tắc Infrastructure as Code (IaC)
- Chứng minh kỹ năng phát triển ứng dụng cloud end-to-end

### Công nghệ & Dịch vụ AWS sử dụng

| Danh mục | Công nghệ / Dịch vụ |
|----------|---------------------|
| **Frontend** | React.js, HTML5, CSS3 |
| **Hosting** | AWS Amplify |
| **Xác thực** | Amazon Cognito |
| **Lưu trữ** | Amazon S3 |
| **Compute** | AWS Lambda (Python 3.12) |
| **API** | Amazon API Gateway (REST) |
| **Cơ sở dữ liệu** | Amazon DynamoDB |
| **AI/ML** | Amazon Rekognition |
| **Giám sát** | Amazon CloudWatch |
| **CI/CD** | AWS Amplify (auto-deploy từ GitHub) |

### Tiến độ dự án

| Giai đoạn | Thời gian | Công việc |
|-----------|-----------|-----------|
| Lập kế hoạch & Thiết kế | Ngày 1-2 | Thu thập yêu cầu, thiết kế kiến trúc |
| Thiết lập Backend | Ngày 3-5 | S3, DynamoDB, Lambda functions |
| Xác thực & API | Ngày 6-7 | Cấu hình Cognito, API Gateway |
| Frontend | Ngày 8-10 | Phát triển React app, triển khai Amplify |
| Tích hợp AI | Ngày 11-12 | Tích hợp Rekognition, kiểm thử |
| Kiểm thử & Hoàn thiện | Ngày 13-14 | Kiểm thử end-to-end, viết tài liệu |

> Dự án này được thiết kế như một minh chứng toàn diện cho các kỹ năng đã học trong quá trình thực tập, bao gồm từ kiến trúc cloud đến phát triển frontend và tích hợp AI.
