---
title: "Worklog Tuần 7"
date: 01 - 06 - 2026
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu tuần 7:
* Áp dụng nguyên tắc phòng thủ chiều sâu (Defense in Depth) và cấp quyền tối thiểu (Least Privilege).
* Làm chủ hệ thống quản lý danh tính, chứng chỉ số và bảo vệ an toàn các thông tin mật.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nghiên cứu tổng quan lợi ích an ninh thông tin, tuân thủ tiêu chuẩn quốc tế (ISO, PCI DSS).<br>- Tìm hiểu dịch vụ ứng dụng AI giám sát luồng log để phát hiện mối đe dọa ẩn Amazon GuardDuty. | 01/06/2026 | 01/06/2026 | <https://000098.awsstudygroup.com/vi/> |
| 3 | - Nghiên cứu phân hệ xác thực, đăng nhập và quản lý danh tính người dùng ứng dụng Amazon Cognito.<br>- Tìm hiểu cơ chế tích hợp định danh doanh nghiệp tập trung qua AWS SSO và Directory Services. | 02/06/2026 | 02/06/2026 | <https://000141.awsstudygroup.com/vi/> |
| 4 | - Tìm hiểu dịch vụ mã hóa dữ liệu tĩnh AWS KMS, thiết bị mã hóa phần cứng an toàn CloudHSM.<br>- Nghiên cứu cách tạo lập, quản lý và gia hạn chứng chỉ số mã hóa HTTPS qua AWS Certificate Manager (ACM). | 03/06/2026 | 03/06/2026 | <https://000033.awsstudygroup.com/vi/> |
| 5 | - Học cách quản lý cấu hình và chuỗi bảo mật bí mật: Systems Manager Parameter Store.<br>- Nghiên cứu giải pháp quản lý mật khẩu kết nối core DB an toàn nâng cao bằng AWS Secrets Manager (tự động xoay vòng khóa). | 04/06/2026 | 04/06/2026 | <https://000031.awsstudygroup.com/vi/> |
| 6 | - Nghiên cứu công cụ tự động đánh giá lỗ hổng ứng dụng AWS Inspector, Trusted Advisor và tải báo cáo qua AWS Artifact.<br>- **Thực hành:** Thiết lập Parameter Store/Secrets Manager để mã hóa chuỗi kết nối và gọi ra an toàn từ Lambda. | 05/06/2026 | 05/06/2026 | <https://000031.awsstudygroup.com/vi/3-patchmanager/> |

### Kết quả đạt được tuần 7:
* Loại bỏ hoàn toàn nợ kỹ thuật liên quan đến việc viết cứng (hardcode) mật khẩu cấu hình nhạy cảm trong mã nguồn.
* Nắm rõ cách xây dựng một phân hệ xác thực người dùng chuẩn bảo mật an toàn cho sản phẩm (Amazon Cognito).
* Hiểu cách vận dụng mã hóa KMS kết hợp tường lửa WAF/Shield tạo lớp lá chắn kiên cố cho hệ thống Web API.