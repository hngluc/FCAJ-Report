---
title: "Results & Lessons Learned"
date: 2026-07-20
weight: 4
chapter: false
pre: " <b> 8.4. </b> "
---

# Results & Lessons Learned

### Project Results

#### ✅ Completed Features

| Feature | Status | Description |
|---------|--------|-------------|
| User Authentication | ✅ Done | Sign up, login, email verification via Cognito |
| Image Upload | ✅ Done | Pre-signed URL upload to S3 with drag-and-drop UI |
| Image Processing | ✅ Done | Auto-resize and thumbnail generation via Lambda |
| AI Classification | ✅ Done | Label detection using Amazon Rekognition |
| Image Gallery | ✅ Done | Dashboard with thumbnails and search/filter |
| Responsive UI | ✅ Done | Mobile-friendly React frontend on Amplify |

#### 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| Average upload time | ~2 seconds |
| Image processing time | ~3-5 seconds |
| AI classification accuracy | >90% (for common objects) |
| Cold start (Lambda) | ~1-2 seconds |
| Monthly cost (dev environment) | ~$2-5 USD |

### Challenges & Solutions

#### Challenge 1: Lambda Cold Start
- **Problem:** First invocation of Lambda functions had noticeable latency (~3-5 seconds)
- **Solution:** Used Provisioned Concurrency for critical functions and optimized package size by using Lambda Layers for shared dependencies

#### Challenge 2: CORS Configuration
- **Problem:** Frontend could not communicate with API Gateway due to CORS errors
- **Solution:** Configured CORS headers at both API Gateway level and Lambda response headers. Learned the importance of including `Access-Control-Allow-Origin`, `Access-Control-Allow-Headers`, and `Access-Control-Allow-Methods`

#### Challenge 3: Large Image Handling
- **Problem:** Uploading images larger than 6MB through API Gateway was rejected (payload limit)
- **Solution:** Implemented pre-signed URL pattern — the frontend uploads directly to S3, bypassing API Gateway size limits

#### Challenge 4: DynamoDB Query Patterns
- **Problem:** Needed to query images by userId but DynamoDB only supports query on partition key
- **Solution:** Created a Global Secondary Index (GSI) on `userId` to efficiently query all images for a specific user

### Lessons Learned

#### Technical Skills
- **Serverless Architecture**: Learned how to design and implement a complete serverless application, understanding the benefits (no server management, auto-scaling) and trade-offs (cold starts, debugging complexity)
- **Event-Driven Design**: Understood how to use S3 event notifications to trigger downstream processing, creating a loosely-coupled system
- **AWS IAM Best Practices**: Applied the principle of least privilege when creating IAM roles for Lambda functions
- **Infrastructure as Code**: Gained appreciation for the importance of documenting and automating infrastructure setup

#### Soft Skills
- **Problem-Solving**: Each challenge required research, experimentation, and iteration to find the right solution
- **Documentation**: Writing clear documentation (this report) helped solidify understanding and will help future reference
- **Time Management**: Breaking the project into phases with clear milestones helped stay on track

#### What I Would Do Differently
- Start with Infrastructure as Code (CloudFormation/CDK) from the beginning instead of manual console setup
- Implement automated testing earlier in the development process
- Use structured logging from day one for easier debugging
- Consider using Step Functions for orchestrating the image processing pipeline

### Conclusion

Building the Smart Image Platform demo was an invaluable experience that brought together many of the concepts and services learned during the internship. It demonstrated that with AWS serverless services, it's possible to build a production-quality application without managing any servers, while leveraging powerful AI capabilities.

> The project source code and detailed documentation are available on GitHub for reference. This demo project serves as both a learning exercise and a portfolio piece demonstrating practical cloud development skills.
