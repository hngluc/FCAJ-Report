---
title: "Architecture & Design"
date: 2026-07-20
weight: 2
chapter: false
pre: " <b> 8.2. </b> "
---

# Architecture & Design

### System Architecture

The Smart Image Platform follows a **Serverless & Event-Driven Architecture** on AWS. This approach eliminates the need to manage servers, provides automatic scaling, and ensures cost efficiency (pay-per-use).

```
User → Amplify (React Frontend) → API Gateway → Lambda → DynamoDB
                                                    ↓
                                            S3 (Image Storage)
                                                    ↓
                                        S3 Event Notification
                                                    ↓
                                        Lambda (Image Processing)
                                                    ↓
                                        Rekognition (AI Classification)
                                                    ↓
                                        DynamoDB (Store Results)
```

### Architecture Components

#### 1. Frontend Layer
- **AWS Amplify**: Hosts the React.js web application
- Provides CI/CD pipeline with auto-deployment from GitHub
- Custom domain support and SSL certificate management

#### 2. Authentication Layer
- **Amazon Cognito**: Manages user registration, login, and session management
- Supports email verification and password policies
- JWT tokens for API authentication

#### 3. API Layer
- **Amazon API Gateway**: RESTful API endpoints
- Integrated with Cognito Authorizer for secure access
- CORS configuration for frontend communication

#### 4. Compute Layer
- **AWS Lambda**: Serverless functions written in Python
  - `uploadImage`: Handles image upload requests, generates pre-signed URLs
  - `processImage`: Triggered by S3 events, resizes images and creates thumbnails
  - `classifyImage`: Calls Rekognition API for AI-based image classification
  - `getImages`: Retrieves image metadata and classification results

#### 5. Storage Layer
- **Amazon S3**: Object storage for original images, thumbnails, and processed images
- Bucket policies and CORS configuration
- Event notifications to trigger Lambda functions

#### 6. Database Layer
- **Amazon DynamoDB**: NoSQL database for image metadata
- Stores: image ID, upload timestamp, S3 key, classification labels, confidence scores

#### 7. AI/ML Layer
- **Amazon Rekognition**: Pre-trained AI service for image analysis
- Detects labels, objects, scenes, and activities in images
- Returns confidence scores for each detected label

### Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Architecture | Serverless | No server management, auto-scaling, cost-efficient |
| Database | DynamoDB | Low-latency, scalable NoSQL for metadata |
| AI Service | Rekognition | Pre-trained, no ML expertise needed |
| Frontend Hosting | Amplify | Integrated CI/CD, easy deployment |
| Language | Python 3.12 | Rich AWS SDK support, Lambda-friendly |

> The architecture was designed with scalability, cost-efficiency, and maintainability in mind, following AWS Well-Architected Framework principles.
