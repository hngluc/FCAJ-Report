---
title: "Worklog Tuần 11"
date: 29 - 06 - 2026
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Mục tiêu tuần 11:
* Hiện thực hóa sơ đồ lý thuyết của Smart Image Platform thành các tài nguyên thực tế trên AWS Management Console.
* Thiết lập các lớp lá chắn bảo mật tầng biên, cấu hình định tuyến API và thiết lập ranh giới định danh người dùng.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tham gia buổi workshop chuyên sâu cùng Mentor để tiếp thu các kinh nghiệm thực tế về mô hình upload tệp tin an toàn và cơ chế quản lý Token API. | 29/06/2026 | 29/06/2026 | <https://cloudjourney.awsstudygroup.com/vi/1.11-project-p1/> |
| 3 | - Khởi tạo và cấu hình Amazon Cognito User Pool, thiết lập các trường thuộc tính tùy chỉnh (Custom Attributes) và quy tắc xác thực mật khẩu an toàn. | 30/06/2026 | 30/06/2026 | <https://cloudjourney.awsstudygroup.com/vi/1.11-project-p1/cognito/> |
| 4 | - Xây dựng các route định tuyến HTTP bên trong Amazon API Gateway; tích hợp bộ xác thực Cognito User Pool Authorizer để khóa chặt các cổng API backend. | 01/07/2026 | 01/07/2026 | <https://cloudjourney.awsstudygroup.com/vi/1.11-project-p1/apigateway/> |
| 5 | - Triển khai cấu hình tường lửa AWS WAF (Web Application Firewall) đứng chặn trực tiếp trước API Gateway để ngăn chặn các lỗ hổng bảo mật web phổ biến. | 02/07/2026 | 02/07/2026 | <https://cloudjourney.awsstudygroup.com/vi/1.11-project-p1/waf/> |
| 6 | - Lập trình logic cốt lõi bằng Python/Node.js cho hàm 'API Handler Lambda', hiện thực hóa tính năng sinh mã S3 Presigned URL an toàn trả về cho Client. | 03/07/2026 | 03/07/2026 | <https://cloudjourney.awsstudygroup.com/vi/1.11-project-p1/lambda-handler/> |

### Kết quả đạt được tuần 11:
* Triển khai thành công hệ thống API Gateway được bảo vệ nghiêm ngặt bằng hai lớp bảo mật ở tầng biên (AWS WAF kết hợp Cognito Authorizer).
* Phát triển thành công mã nguồn cấp quyền bằng S3 Presigned URL, giúp client frontend có thể upload trực tiếp dữ liệu lên đám mây mà không cần mở public quyền ghi của bucket.