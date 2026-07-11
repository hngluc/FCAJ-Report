---
title: "Worklog Tuần 2"
date: 27 - 04 - 2026
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Mục tiêu tuần 2:
* Hiểu cách thiết kế hạ tầng mạng ảo độc lập, an toàn trên AWS.
* Nắm vững các giải pháp điều hướng lưu lượng, cân bằng tải và bảo mật lớp mạng biên.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nghiên cứu cấu trúc kiến trúc Mạng biên đám mây.<br>- Tìm hiểu cơ chế phân giải tên miền của Amazon Route 53.<br>- Nghiên cứu giải pháp phân phối nội dung tăng tốc toàn cầu Amazon CloudFront. | 27/04/2026 | 27/04/2026 | <https://000094.awsstudygroup.com/vi/>|
| 3 | - Tìm hiểu nguyên lý hoạt động và phân loại của Elastic Load Balancing (ALB, NLB).<br>- Nghiên cứu vai trò và cách quản lý cổng kết nối API Gateway. | 28/04/2026 | 28/04/2026 | <https://000004.awsstudygroup.com/vi/> |
| 4 | - Học lý thuyết kết nối mạng nâng cao trong doanh nghiệp: VPC Peering, PrivateLink.<br>- Nghiên cứu giải pháp mạng Hybrid: AWS Transit Gateway, Site-to-Site VPN và AWS Direct Connect. | 29/04/2026 | 29/04/2026 | <https://000003.awsstudygroup.com/vi/5-vpnsitetosite/><https://000019.awsstudygroup.com/vi/> |
| 5 | - Nghiên cứu bảo mật tầng mạng: cấu hình AWS WAF chống tấn công lớp ứng dụng và AWS Shield giảm thiểu tấn công DDoS.<br>- Phân biệt phạm vi hoạt động của Security Groups (Stateful) và Network ACLs (Stateless).<br>- Tìm hiểu cách quản lý chứng chỉ số SSL/TLS thông qua AWS Certificate Manager (ACM). | 30/04/2026 | 30/04/2026 | <https://000026.awsstudygroup.com/vi/> |
| 6 | - Tìm hiểu hệ thống giám sát và nhật ký lưu lượng: VPC Flow Logs, CloudWatch, CloudTrail.<br>- **Thực hành:** Cấu hình tạo VPC, chia Subnets, thiết lập bộ cân bằng tải ALB và chẩn đoán lỗi mạng bằng Reachability Analyzer. | 01/05/2026 | 01/05/2026 | <https://000074.awsstudygroup.com/vi/><https://000029.awsstudygroup.com/vi/> |

### Kết quả đạt được tuần 2:
* Thành thạo tư duy phân hoạch vùng mạng và thiết lập các quy tắc tường lửa đa tầng bảo vệ tài nguyên Private Subnet.
* Nắm vững cơ chế hoạt động của bộ cân bằng tải ALB để phân phối lưu lượng bất đồng bộ cho ứng dụng.
* Hiểu cách áp dụng AWS WAF và bảo mật HTTPS (SSL/TLS) biên thông qua ACM để đóng gói ứng dụng an toàn.
* Biết cách đọc nhật ký giám sát lưu lượng bằng VPC Flow Logs để phục vụ công tác rà soát lỗi hạ tầng mạng.