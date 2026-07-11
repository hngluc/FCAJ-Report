---
title: "Worklog Tuần 6"
date: 25 - 05 - 2026
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Mục tiêu tuần 6:
* Hiểu sâu kiến trúc Hồ dữ liệu (Data Lake) và Kho dữ liệu (Data Warehouse) phục vụ xử lý Big Data.
* Xây dựng và tự động hóa các luồng xử lý, trích xuất, biến đổi dữ liệu (Data Pipeline ETL).

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nghiên cứu quy trình thu thập dữ liệu thô (Data Ingestion) qua Amazon S3.<br>- Tìm hiểu giải pháp hứng luồng luân chuyển dữ liệu liên tục thời gian thực Amazon Kinesis Data Streams. | 25/05/2026 | 25/05/2026 | <https://000070.awsstudygroup.com/vi/3-ingestglue/> |
| 3 | - Tìm hiểu dịch vụ biến đổi dữ liệu cốt lõi AWS Glue (ETL - Extract, Transform, Load).<br>- Nghiên cứu giải pháp di chuyển dữ liệu AWS Data Pipeline và cụm tính toán phân tán lớn Amazon EMR (Hadoop/Spark). | 26/05/2026 | 26/05/2026 | <https://000040.awsstudygroup.com/vi/1-introduce/> |
| 4 | - Nghiên cứu phân hệ quản trị dữ liệu tập trung an toàn với AWS Lake Formation.<br>- Tìm hiểu cách kết hợp kiểm soát bảo mật qua IAM, CloudTrail và quét dữ liệu nhạy cảm PII bằng Amazon Macie. | 27/05/2026 | 27/05/2026 | <https://000037.awsstudygroup.com/vi/4-cloudformationadvance/> |
| 5 | - Nghiên cứu giải pháp điều phối tác vụ (Orchestration): AWS Step Functions để lập lịch trạng thái công việc.<br>- Tìm hiểu dịch vụ quản lý luồng tự động phức tạp doanh nghiệp Amazon MWAA (Managed Apache Airflow). | 28/05/2026 | 28/05/2026 | <hhttps://aws.amazon.com/vi/managed-workflows-for-apache-airflow/> |
| 6 | - **Thực hành:** Cấu hình lập lịch chạy một AWS Glue Crawler quét tệp dữ liệu mẫu trên S3.<br>- Phân tích cấu trúc tự động (Schema Discovery) và lưu trữ kết quả cấu phần thành công vào Data Catalog. | 29/05/2026 | 29/05/2026 | <https://000070.awsstudygroup.com/vi/3-ingestglue/3.2-catalog/> |

### Kết quả đạt được tuần 6:
* Nắm trọn mô hình kiến trúc vòng đời dữ liệu lớn từ lưu trữ thô đến tầng xử lý thông minh sẵn sàng phân tích.
* Thành thạo cách lập lịch điều phối tự động các tác vụ công việc ngầm bằng giải pháp không máy chủ AWS Glue.
* Hiểu rõ tư duy quản trị bảo mật an toàn dữ liệu, chống rò rỉ thông tin định danh cá nhân nhạy cảm nhờ Amazon Macie.