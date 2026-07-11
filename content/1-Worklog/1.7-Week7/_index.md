---
title: "Worklog Week 7"
date: 01 - 06 - 2026
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Objectives for Week 7:
* Enforce rigorous Defense-in-Depth policies and Least-Privilege IAM boundaries across cloud ecosystems.
* Control application identities, digital cryptography lifecycles, and credential storage architectures securely.

### Tasks to Implement This Week:
| Day | Tasks | Start Date | Completion Date | Resource Link |
| --- | --- | --- | --- | --- |
| Mon | - Study core pillars of AWS security posture and international data compliance certifications (ISO, PCI DSS).<br>- Investigate threat detection systems using machine-learning log collectors in Amazon GuardDuty. | 01/06/2026 | 01/06/2026 | <https://000098.awsstudygroup.com/>  |
| Tue | - Research application identity providers, customer user directories, and multi-factor authentication (MFA) via Amazon Cognito.<br>- Study enterprise single sign-on federation through AWS IAM Identity Center and Directory Services. | 02/06/2026 | 02/06/2026 | <https://000141.awsstudygroup.com/> |
| Wed | - Investigate symmetric and asymmetric envelope data cryptography using AWS KMS keys.<br>- Learn hardware-backed key protection via CloudHSM and programmatic SSL/TLS public key lifecycles with AWS Certificate Manager (ACM). | 03/06/2026 | 03/06/2026 | <https://000033.awsstudygroup.com/> |
| Thu | - Study methods to eliminate plain-text credential leaks by leveraging AWS Systems Manager Parameter Store.<br>- Research secret isolation, parameter versioning, and auto-rotation frameworks using AWS Secrets Manager. | 04/06/2026 | 04/06/2026 | <https://000031.awsstudygroup.com/>|
| Fri | - Study automated posture assessment tooling via AWS Inspector and best practice checks with AWS Trusted Advisor.<br>- **Hands-on Task:** Inject encrypted secrets into AWS Secrets Manager and safely extract them dynamically during runtime execution inside AWS Lambda functions. | 05/06/2026 | 05/06/2026 | <https://000031.awsstudygroup.com/3-patchmanager/>|

### Key Achievements for Week 7:
* Eliminated application code security risks by shifting configuration values and third-party keys out of raw repositories into secured param stores.
* Designed user registration and login token validation components utilizing Amazon Cognito directories.
* Applied envelope encryption models with AWS KMS to protect objects stored in relational and object data backends.