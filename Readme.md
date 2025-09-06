# Atomberg Share of Voice Analyzer

## AI-Powered Social Media Analytics for Smart Fan Market

A comprehensive full-stack application that analyzes Share of Voice (SOV) for Atomberg smart fans across social media platforms using AI-powered sentiment analysis.

## 🎯 Project Overview

This project was developed for Atomberg's AI/ML internship challenge to build an AI agent that:
- Searches for 'smart fan' content across multiple platforms (Google, YouTube, Instagram, Twitter/X)
- Analyzes top N search results with configurable parameters
- Quantifies Share of Voice (SOV) that Atomberg gets compared to competitors
- Provides sentiment analysis and actionable insights

## 🏗️ Architecture

### Backend (FastAPI)
- **Social Media Scraping**: Multi-platform data collection using Playwright and BeautifulSoup
- **Sentiment Analysis**: Ensemble approach using VADER, TextBlob, and NLTK
- **SOV Calculation**: Advanced metrics including engagement rates, sentiment breakdown
- **REST API**: Comprehensive endpoints for analysis, results, and configuration

### Frontend (React/Vanilla JS)
- **Interactive Dashboard**: Real-time analytics with Chart.js visualizations
- **Search Configuration**: Flexible parameter settings for keywords, platforms, and analysis scope
- **Live Progress Tracking**: Real-time updates during analysis execution
- **Export Capabilities**: JSON and CSV export for further analysis

## 🚀 Features

### Core Analytics
- **Share of Voice Metrics**: Percentage breakdown across competitors
- **Sentiment Analysis**: Positive, negative, neutral classification with confidence scores
- **Engagement Analysis**: Likes, comments, shares, and views aggregation
- **Competitor Comparison**: Head-to-head analysis with market leaders
- **Trend Analysis**: Temporal patterns and keyword trending

### Visualizations
- SOV Distribution (Pie Chart)
- Brand Mentions Comparison (Bar Chart)
- Sentiment Breakdown (Donut Chart)
- Engagement vs SOV Scatter Plot
- Competitor Performance Table
- Trend Lines Over Time

### Intelligence Features
- **Market Insights**: Automated market position analysis
- **Strategic Recommendations**: AI-generated actionable insights
- **Competitive Intelligence**: Strength/weakness identification
- **Growth Opportunities**: Untapped market identification

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI (Python)
- **Scraping**: Playwright, BeautifulSoup4, Selenium
- **AI/ML**: TextBlob, VADER, NLTK, Transformers
- **Data Processing**: Pandas, NumPy
- **Database**: MongoDB (with Motor async driver)
- **Caching**: Redis
- **Task Queue**: Celery

### Frontend
- **Core**: React 18 / Vanilla JavaScript
- **UI Components**: Ant Design / Custom CSS
- **Charts**: Chart.js, Recharts
- **HTTP Client**: Axios
- **State Management**: React Query

### DevOps
- **Containerization**: Docker, Docker Compose
- **API Documentation**: OpenAPI/Swagger
- **Testing**: pytest, Jest
- **CI/CD**: GitHub Actions

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 16+
- Docker (optional)
- MongoDB (local or cloud)
- Redis (for caching)

### Docker Setup
```bash
# Run entire stack with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down