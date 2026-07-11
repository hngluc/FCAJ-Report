---
title: "Worklog Tuần 12"
date: 06 - 07 - 2026
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

### Mục tiêu tuần 12:
* Hoàn thiện toàn bộ hệ thống xử lý ảnh ngầm bất đồng bộ và tự động hóa quy trình phân tích hình ảnh bằng Học máy (Machine Learning).
* Tiến hành kiểm thử tích hợp toàn diện, dọn dẹp tối ưu mã nguồn hạ tầng và hoàn thành file báo cáo nhật ký tổng kết.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Khởi tạo hai S3 Bucket cô lập chuyên trách (`raw-store` chứa ảnh thô và `processed-store` chứa ảnh đích); cấu hình sự kiện Object Created để kích hoạt trigger Lambda. | 06/07/2026 | 06/07/2026 | <https://cloudjourney.awsstudygroup.com/vi/1.12-project-p2/s3-events/> |
| 3 | - Viết code và tối ưu hàm 'Image Processor Lambda', sử dụng các thư viện xử lý ảnh chuyên dụng trong Python để tự động nén và resize hình ảnh ngầm. | 07/07/2026 | 07/07/2026 | <https://cloudjourney.awsstudygroup.com/vi/1.12-project-p2/image-lambda/> |
| 4 | - Khởi tạo bảng dữ liệu lưu trữ metadata trên Amazon DynamoDB và kích hoạt tính năng DynamoDB Streams để theo dõi, bắt các sự kiện thay đổi dữ liệu tĩnh. | 08/07/2026 | 08/07/2026 | <https://cloudjourney.awsstudygroup.com/vi/1.12-project-p2/dynamodb-streams/> |
| 5 | - Lập trình hàm 'AI Analyzer Lambda' nhận dữ liệu stream, thực hiện gọi SDK đến Amazon Rekognition để nhận diện vật thể, tự động gán nhãn và ghi ngược kết quả vào database. | 09/07/2026 | 09/07/2026 | <https://cloudjourney.awsstudygroup.com/vi/1.12-project-p2/rekognition-lambda/> |
| 6 | - Tiến hành kiểm thử end-to-end toàn hệ thống thông qua giao diện React App cục bộ; kiểm tra độ trễ, dọn dẹp tài nguyên rác và thực hiện đẩy kho mã nguồn sạch lên GitHub. | 10/07/2026 | 10/07/2026 | <https://cloudjourney.awsstudygroup.com/vi/1.12-project-p2/testing/> |

### Kết quả đạt được tuần 12:
* Xây dựng thành công hệ thống xử lý hình ảnh hướng sự kiện (Event-Driven) chạy ngầm hoàn toàn bất đồng bộ, giúp giải phóng băng thông tối đa cho client.
* Tích hợp thành công dịch vụ AI (Amazon Rekognition) để tự động hóa 100% quy trình phân loại nhãn ảnh, kiểm duyệt nội dung và cập nhật metadata vào NoSQL DB theo thời gian thực.
* Đóng gói dự án và đẩy thành công Repo mã nguồn hoàn chỉnh có kèm file hướng dẫn cài đặt (README.md) chi tiết lên GitHub cá nhân.