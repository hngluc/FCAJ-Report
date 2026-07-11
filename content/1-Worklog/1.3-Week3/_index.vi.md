---
title: "Worklog Tuần 3"
date: 04 - 05 - 2026
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

### Mục tiêu tuần 3:
* Nắm vững hệ sinh thái các dịch vụ tính toán, xử lý logic (Compute) trên AWS.
* Phân biệt và làm chủ 3 mô hình: Máy chủ ảo, Container và Serverless.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nghiên cứu chuyên sâu về máy chủ ảo Amazon EC2 (Instance types, cấu hình cấu phần phần cứng).<br>- Tìm hiểu giải pháp triển khai đóng gói tinh gọn Amazon Lightsail. | 04/05/2026 | 04/05/2026 | <https://000003.awsstudygroup.com/vi/><https://000045.awsstudygroup.com/vi/> |
| 3 | - Tìm hiểu kiến thức cốt lõi về Containerization: Amazon ECS, Amazon EKS.<br>- Nghiên cứu hạ tầng Serverless cho container AWS Fargate và kho lưu trữ hình ảnh Docker Amazon ECR. | 05/05/2026 | 05/05/2026 | <https://000016.awsstudygroup.com/vi/1-introduction/><https://000126.awsstudygroup.com/vi/> |
| 4 | - Nghiên cứu giải pháp tính toán không máy chủ (Serverless) với AWS Lambda.<br>- Tìm hiểu cơ chế trigger hướng sự kiện (Event-driven) và công cụ tự động hóa AWS Elastic Beanstalk.<br>- Nghiên cứu mô hình cam kết tiết kiệm ngân sách AWS Savings Plan. | 06/05/2026 | 06/05/2026 | <https://000078.awsstudygroup.com/vi/> |
| 5 | - **Thực hành Bài tập 1 & 2:** Khởi tạo, cấu hình hệ điều hành cho Amazon EC2 instance.<br>- Triển khai trực tiếp và vận hành một ứng dụng Web tĩnh/động chạy trên nền tảng EC2. | 07/05/2026 | 07/05/2026 | <https://000003.awsstudygroup.com/vi/4-createec2server/4.1-createec2/> |
| 6 | - **Thực hành Bài tập 3 & 4:** Đóng gói ứng dụng backend thành Docker Image, đẩy lên Amazon ECR.<br>- Khởi chạy ứng dụng container hóa trên cụm ECS Fargate và viết hàm xử lý logic tự động với AWS Lambda. | 08/05/2026 | 08/05/2026 | <https://000015.awsstudygroup.com/vi/6-docker-image/> |

### Kết quả đạt được tuần 3:
* Làm chủ kỹ năng quản trị và cấu hình vòng đời của máy chủ ảo Amazon EC2.
* Đóng gói thành thạo ứng dụng phần mềm thành Docker Image và vận hành mượt mà trên môi trường cụm container Amazon ECS Fargate.
* Xây dựng thành công tư duy xử lý logic bất đồng bộ hướng sự kiện thông qua việc viết mã nguồn cho AWS Lambda.