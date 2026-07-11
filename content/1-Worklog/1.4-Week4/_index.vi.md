---
title: "Worklog Tuần 4"
date: 11 - 05 - 2026
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu tuần 4:
* Phân loại và ứng dụng chính xác các giải pháp lưu trữ dữ liệu (Object, Block, File) trên Cloud.
* Thiết lập quy trình tự động sao lưu và tối ưu hóa chi phí không gian lưu trữ.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu giải pháp lưu trữ đối tượng Amazon S3, phân lớp dữ liệu nguội S3 Glacier.<br>- Nghiên cứu các cơ chế bảo mật nâng cao: Versioning, Lifecycle policies, Bucket policies trên S3. | 11/05/2026 | 11/05/2026 | <https://000078.awsstudygroup.com/vi/>|
| 3 | - Nghiên cứu lưu trữ khối Amazon EBS (General Purpose SSD, Provisioned IOPS, HDD).<br>- Tìm hiểu cơ chế lưu trữ tạm thời Instance Store Volumes và hệ thống tệp tin dùng chung Amazon EFS/FSx. | 12/05/2026 | 12/05/2026 | <https://100000.awsstudygroup.com/vi/1-intro/> |
| 4 | - Nghiên cứu kiến trúc cầu nối lưu trữ Hybrid đám mây với AWS Storage Gateway.<br>- Tìm hiểu giải pháp quản lý sao lưu tập trung toàn diện AWS Backup. | 13/05/2026 | 13/05/2026 | <https://000024.awsstudygroup.com/vi/2-useawsstoragegw/> |
| 5 | - **Thực hành:** Tạo lập và quản lý không gian lưu trữ trên Amazon S3.<br>- Cấu hình chính sách bảo mật Bucket Policy và thiết lập Lifecycle policy chuyển đổi dữ liệu tự động. | 14/05/2026 | 14/05/2026 | <https://000078.awsstudygroup.com/vi/2-resize-image-function/2-2-create-s3-bucket/>  |
| 6 | - **Thực hành:** Tạo snapshot lưu trữ và thực hiện restore khôi phục dữ liệu cho ổ đĩa EBS.<br>- Thiết lập cấu hình AWS Backup lên lịch trình tự động sao lưu an toàn cho tài nguyên tính toán EC2. | 15/05/2026 | 15/05/2026 | <https://100000.awsstudygroup.com/vi/11-postgresql-restore-configuration/> |

### Kết quả đạt được tuần 4:
* Sử dụng thành thạo Amazon S3 để lưu trữ tài nguyên tĩnh, tối ưu hóa băng thông bằng phân lớp lưu trữ tự động.
* Làm chủ kỹ năng quản trị hệ thống ổ đĩa máy chủ EBS, biết cách tạo và khôi phục snapshot phòng chống thảm họa mất dữ liệu.
* Vận hành hệ thống sao lưu tự động cho tài nguyên hạ tầng thông qua AWS Backup tuân thủ tiêu chuẩn doanh nghiệp.