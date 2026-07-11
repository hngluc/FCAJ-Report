---
title: "Worklog Week 6"
date: 25 - 05 - 2026
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Objectives for Week 6:
* Understand the architecture of enterprise-scale Data Lakes and Data Warehouses for Big Data engineering.
* Construct and automate end-to-end serverless data extraction, transformation, and loading (ETL) pipelines.

### Tasks to Implement This Week:
| Day | Tasks | Start Date | Completion Date | Resource Link |
| --- | --- | --- | --- | --- |
| Mon | - Study raw data ingestion architectural options over centralized Amazon S3 Data Lakes.<br>- Research real-time massive streaming data capture pipelines using Amazon Kinesis Data Streams. | 25/05/2026 | 25/05/2026 | <https://000070.awsstudygroup.com/3-ingestglue/> |
| Tue | - Investigate serverless ETL orchestration using AWS Glue metadata catalogs and transformation scripts.<br>- Research data pipeline movements using AWS Data Pipeline and managed big data MapReduce processing via Amazon EMR (Hadoop/Spark). | 26/05/2026 | 26/05/2026 | <https://000040.awsstudygroup.com/1-introduce/>  |
| Wed | - Research structural data access controls and governance boundaries using AWS Lake Formation.<br>- Study audit trail monitoring through CloudTrail and automated PII sensitive data discovery using Amazon Macie. | 27/05/2026 | 27/05/2026 | <https://000037.awsstudygroup.com/4-cloudformationadvance/> |
| Thu | - Research distributed workflow orchestration state machines using AWS Step Functions.<br>- Study enterprise-grade open-source DAG workflow management with Amazon MWAA (Managed Apache Airflow). | 28/05/2026 | 28/05/2026 | <https://aws.amazon.com/managed-workflows-for-apache-airflow/> |
| Fri | - **Hands-on Task:** Deploy and execute an AWS Glue Crawler targeting raw unstructured object stores inside Amazon S3.<br>- Automate schema discovery patterns and systematically parse discovered partitions into the central AWS Glue Data Catalog. | 29/05/2026 | 29/05/2026 | <https://000070.awsstudygroup.com/vi/3-ingestglue/3.2-catalog/> |

### Key Achievements for Week 6:
* Mastered big data lifecycle flows stretching across raw stream captures, serverless cataloging, and data warehouse partitioning.
* Built serverless metadata crawlers utilizing AWS Glue to maintain updated corporate data directory schemas.
* Understood how to prevent accidentally leaking personally identifiable information (PII) into analysis clusters via Amazon Macie patterns.