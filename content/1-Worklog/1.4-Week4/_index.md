---
title: "Worklog Week 4"
date: 11 - 05 - 2026
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Objectives for Week 4:
* Evaluate and implement appropriate storage solutions (Object, Block, File) based on cloud workload needs.
* Establish automated backup retention windows and dynamic storage cost optimization strategies.

### Tasks to Implement This Week:
| Day | Tasks | Start Date | Completion Date | Resource Link |
| --- | --- | --- | --- | --- |
| Mon | - Explore object storage with Amazon S3 and archival storage with S3 Glacier.<br>- Investigate advanced data security control structures: S3 Versioning, Lifecycle policies, and Bucket policies. | 11/05/2026 | 11/05/2026 | <https://000078.awsstudygroup.com/> |
| Tue | - Research block storage architectures with Amazon EBS (SSD/HDD variants, performance tiers, snapshots).<br>- Study ephemeral Instance Store volumes and shared network file systems (Amazon EFS/FSx). | 12/05/2026 | 12/05/2026 | <https://100000.awsstudygroup.com/1-intro/> |
| Wed | - Study hybrid data integration bridging on-premises environments and AWS using AWS Storage Gateway.<br>- Research centralized backup policy orchestration using AWS Backup. | 13/05/2026 | 13/05/2026 | <https://000024.awsstudygroup.com/2-useawsstoragegw/> |
| Thu | - **Hands-on Task:** Create and secure an Amazon S3 Bucket.<br>- Enforce explicit Bucket Policies and design automated S3 Lifecycle rules to migrate data segments across storage tiers. | 14/05/2026 | 14/05/2026 | <https://000078.awsstudygroup.com/2-resize-image-function/2-2-create-s3-bucket/> |
| Fri | - **Hands-on Task:** Create point-in-time snapshots of live EBS volumes and perform volume restoration validations.<br>- Configure backup schedules and retention rules across cloud resources via AWS Backup. | 15/05/2026 | 15/05/2026 | <https://100000.awsstudygroup.com/11-postgresql-restore-configuration/> |

### Key Achievements for Week 4:
* Developed production-ready S3 asset ingestion pipelines optimized with rule-based cost allocation tiers.
* Mastered disk snapshot lifecycle patterns on EBS volumes to minimize recovery time objective (RTO) and recovery point objective (RPO) metrics.
* Enforced compliance boundaries across active cloud assets by configuring unified backup strategies under AWS Backup.