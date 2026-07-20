---
title: "Kết quả & Bài học"
date: 2026-07-20
weight: 4
chapter: false
pre: " <b> 8.4. </b> "
---

# Kết quả & Bài học

### Kết quả dự án

#### Các tính năng đã hoàn thành

| Tính năng | Trạng thái | Mô tả |
|-----------|-----------|-------|
| Xác thực người dùng | ✅ Xong | Đăng ký, đăng nhập, xác minh email qua Cognito |
| Tải ảnh lên | ✅ Xong | Tải lên S3 bằng pre-signed URL với giao diện kéo-thả |
| Xử lý ảnh | ✅ Xong | Tự động thay đổi kích thước và tạo thumbnail qua Lambda |
| Phân loại AI | ✅ Xong | Phát hiện nhãn sử dụng Amazon Rekognition |
| Thư viện ảnh | ✅ Xong | Dashboard với thumbnails và tìm kiếm/lọc |
| Giao diện Responsive | ✅ Xong | Frontend React thân thiện di động trên Amplify |

#### Chỉ số hiệu suất

| Chỉ số | Giá trị |
|--------|---------|
| Thời gian tải ảnh trung bình | ~2 giây |
| Thời gian xử lý ảnh | ~3-5 giây |
| Độ chính xác phân loại AI | >90% (cho các đối tượng phổ biến) |
| Cold start (Lambda) | ~1-2 giây |
| Chi phí hàng tháng (môi trường dev) | ~$2-5 USD |

### Thách thức & Giải pháp

#### Thách thức 1: Lambda Cold Start
- **Vấn đề:** Lần gọi đầu tiên của Lambda functions có độ trễ đáng kể (~3-5 giây)
- **Giải pháp:** Sử dụng Provisioned Concurrency cho các functions quan trọng và tối ưu kích thước package bằng Lambda Layers cho các dependencies dùng chung

#### Thách thức 2: Cấu hình CORS
- **Vấn đề:** Frontend không thể giao tiếp với API Gateway do lỗi CORS
- **Giải pháp:** Cấu hình CORS headers ở cả API Gateway và Lambda response headers. Học được tầm quan trọng của việc bao gồm `Access-Control-Allow-Origin`, `Access-Control-Allow-Headers`, và `Access-Control-Allow-Methods`

#### Thách thức 3: Xử lý ảnh lớn
- **Vấn đề:** Tải ảnh lớn hơn 6MB qua API Gateway bị từ chối (giới hạn payload)
- **Giải pháp:** Triển khai mô hình pre-signed URL — frontend tải trực tiếp lên S3, bỏ qua giới hạn kích thước của API Gateway

#### Thách thức 4: Query Patterns trong DynamoDB
- **Vấn đề:** Cần truy vấn ảnh theo userId nhưng DynamoDB chỉ hỗ trợ query trên partition key
- **Giải pháp:** Tạo Global Secondary Index (GSI) trên `userId` để truy vấn hiệu quả tất cả ảnh của một người dùng cụ thể

### Bài học kinh nghiệm

#### Kỹ năng kỹ thuật
- **Kiến trúc Serverless**: Học cách thiết kế và triển khai ứng dụng serverless hoàn chỉnh, hiểu được lợi ích (không cần quản lý server, tự động mở rộng) và đánh đổi (cold starts, độ phức tạp debug)
- **Thiết kế hướng sự kiện**: Hiểu cách sử dụng S3 event notifications để kích hoạt xử lý downstream, tạo hệ thống loosely-coupled
- **AWS IAM Best Practices**: Áp dụng nguyên tắc least privilege khi tạo IAM roles cho Lambda functions
- **Infrastructure as Code**: Nhận thức được tầm quan trọng của việc tài liệu hóa và tự động hóa thiết lập hạ tầng

#### Kỹ năng mềm
- **Giải quyết vấn đề**: Mỗi thách thức đều cần nghiên cứu, thử nghiệm và lặp lại để tìm giải pháp đúng
- **Viết tài liệu**: Viết tài liệu rõ ràng (báo cáo này) giúp củng cố kiến thức và là tài liệu tham khảo sau này
- **Quản lý thời gian**: Chia dự án thành các giai đoạn với mốc rõ ràng giúp đi đúng tiến độ

#### Những điều sẽ làm khác
- Bắt đầu với Infrastructure as Code (CloudFormation/CDK) ngay từ đầu thay vì thiết lập thủ công trên console
- Triển khai automated testing sớm hơn trong quá trình phát triển
- Sử dụng structured logging ngay từ ngày đầu để debug dễ dàng hơn
- Cân nhắc sử dụng Step Functions để điều phối pipeline xử lý ảnh

### Kết luận

Xây dựng dự án demo Smart Image Platform là một trải nghiệm vô cùng quý giá, kết hợp nhiều khái niệm và dịch vụ đã học trong quá trình thực tập. Dự án chứng minh rằng với các dịch vụ serverless của AWS, hoàn toàn có thể xây dựng ứng dụng chất lượng production mà không cần quản lý bất kỳ máy chủ nào, đồng thời tận dụng các khả năng AI mạnh mẽ.

> Mã nguồn dự án và tài liệu chi tiết có sẵn trên GitHub để tham khảo. Dự án demo này vừa là bài tập học tập, vừa là portfolio thể hiện kỹ năng phát triển cloud thực tế.
