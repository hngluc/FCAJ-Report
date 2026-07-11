---
title: "Worklog Tuần 5"
date: 18 - 05 - 2026
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Mục tiêu tuần 5:
* Làm chủ tư duy lựa chọn, cấu hình và thiết kế các hệ thống cơ sở dữ liệu chuyên biệt trên Cloud.
* Tích hợp các giải pháp bộ nhớ đệm (Caching) và kho lưu trữ lớn phục vụ tối ưu hiệu năng.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nghiên cứu hệ quản trị cơ sở dữ liệu quan hệ Amazon RDS (MySQL, PostgreSQL, MariaDB...).<br>- Tìm hiểu giải pháp DB tối ưu riêng cho đám mây Amazon Aurora (hiệu năng cao, tự động khôi phục). | 18/05/2026 | 18/05/2026 | <https://000005.awsstudygroup.com/vi/> |
| 3 | - Tìm hiểu sâu về cơ sở dữ liệu NoSQL tốc độ cao Amazon DynamoDB.<br>- Nghiên cứu tư duy thiết kế khóa (Partition Key, Sort Key) và cơ chế tự động mở rộng quy mô. | 19/05/2026 | 19/05/2026 | <https://000078.awsstudygroup.com/vi/3-write-data-to-dynaomodb/> |
| 4 | - Nghiên cứu giải pháp tăng tốc độ truy xuất dữ liệu bằng bộ nhớ đệm Amazon ElastiCache (Redis/Memcached).<br>- Tìm hiểu kiến trúc kho dữ liệu phân tích tập trung quy mô lớn Amazon Redshift. | 20/05/2026 | 20/05/2026 | <https://000061.awsstudygroup.com/vi/> |
| 5 | - **Thực hành:** Tạo lập một DB instance MySQL dựa trên nền tảng dịch vụ Amazon RDS.<br>- Thiết lập các thông số bảo mật, phân quyền truy cập mạng và thực thi kịch bản sao lưu, khôi phục dữ liệu. | 21/05/2026 | 21/05/2026 | <https://000133.awsstudygroup.com/vi/1-create-dynamodb-table/> |
| 6 | - **Thực hành:** Khởi tạo bảng, nạp cấu phần dữ liệu và truy vấn trên Amazon DynamoDB.<br>- Cấu hình cụm Redis trên ElastiCache và thiết lập cụm kho Redshift phục vụ nạp dữ liệu phân tích từ S3. | 22/05/2026 | 22/05/2026 | <https://000133.awsstudygroup.com/vi/1-create-dynamodb-table/> |

### Kết quả đạt được tuần 5:
* Thành thạo kỹ năng triển khai, vận hành và phân quyền bảo mật cho hệ quản trị dữ liệu quan hệ Amazon RDS.
* Nắm vững tư duy lưu trữ NoSQL với DynamoDB để xử lý các tập dữ liệu phi cấu trúc độ trễ thấp.
* Biết cách tối ưu hóa phản hồi ứng dụng bằng tầng đệm ElastiCache Redis, giảm tải áp lực truy vấn cho tầng Database cốt lõi.