# Financial Market Intelligence Platform

A production-grade Financial Market Intelligence Platform built on Google Cloud Platform.

## Goals

- Ingest live financial market data
- Validate incoming datasets
- Build a Medallion Architecture
- Load analytics-ready data into BigQuery
- Create business dashboards
- Generate AI-powered executive reports

## Tech Stack

- Python
- Apache Airflow
- Google Cloud Platform
- Google Cloud Storage
- BigQuery
- Docker
- Terraform

Financial Market Intelligence Platform project architecture
                    Configuration
                          │
                          ▼
                     Logging
                          │
                          ▼
                    Exceptions
                          │
                          ▼
                 Base HTTP Client
                          │
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
    CoinGecko      AlphaVantage      News API
          │               │                │
          └───────────────┼────────────────┘
                          ▼
                    Bronze Layer (GCS)
                          ▼
                  Validation (Pandera)
                          ▼
                    Silver Layer
                          ▼
                  BigQuery Warehouse
                          ▼
                 Looker Studio Dashboard
                          ▼
               AI Executive Market Reports

## Engineering Foundation

Completed:

- ✅ Modern Python project setup with `uv`
- ✅ Centralized configuration management using Pydantic Settings
- ✅ Structured logging framework
- ✅ Custom exception hierarchy

## Networking Layer

Implemented:

- ✅ Reusable BaseHTTPClient
- ✅ HTTP connection pooling with `httpx.Client`
- ✅ Configurable timeout management
- ✅ Structured logging integration
- ✅ Foundation for financial API clients

## Data Sources

Implemented:

- ✅ CoinGecko API
  - Health Check
  - Market Data
  - Trending Coins

## Data Modeling

Implemented:

- ✅ Pydantic domain models
- ✅ Runtime schema validation
- ✅ Strongly typed cryptocurrency market objects
- ✅ Foundation for data quality and transformation

  ## Project Status

- ✅ Phase 1: Engineering Foundation
- 🚧 Phase 2: Financial Data Ingestion Platform (In Progress)
- ⏳ Phase 3: Medallion Architecture
- ⏳ Phase 4: BigQuery Warehouse
- ⏳ Phase 5: Analytics & AI Reporting