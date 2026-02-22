# ✨ Glwup ✨ - Beauty Product Crowdfunding Platform

**Vote with your wallet on beauty product reviews you want to see**

A full-stack crowdfunding platform for beauty enthusiasts to fund product reviews and comparisons. Support creators. Discover honest reviews. Get your glow up.

**Created by:** Veronica Yubo Chen

---

## 📱 Deployed Project

- **Frontend:** https://magnificent-meringue-d639f5.netlify.app (CORRECT URL)
- **Backend API:** https://yubo-crowdfunding-shecodes-f2aced9e5879.herokuapp.com
- **API Root Endpoint:** https://yubo-crowdfunding-shecodes-f2aced9e5879.herokuapp.com/ (returns JSON documentation)

---

## 🎯 Project Overview

### Concept
**Glwup** (pronounced "Glow Up") is a crowdfunding platform for beauty enthusiasts. Users can create campaigns to fund product reviews, comparisons, and beauty content. Supporters pledge to campaigns they're interested in, and creators provide detailed product comparisons with links to purchase the reviewed items.

The platform connects beauty content creators with their audience, allowing the community to vote with their wallets on which product comparisons they want to see.

### Target Audience
Beauty enthusiasts, skincare lovers, makeup artists, and content creators aged 18-45 who want honest product comparisons before making purchases.

### Core Features
- 👤 User authentication with token-based login
- 💄 Create and manage beauty product review campaigns
- 💰 Pledge to support campaigns you believe in
- 🔍 Search and filter campaigns by category
- 🛡️ Permission-based access control
- ✅ Funding goal protection
- 🚫 Duplicate pledge prevention
- 📊 Real-time funding status tracking

---

## 🛠️ Tech Stack

### Backend
- **Framework:** Django 5.1 + Django REST Framework
- **Database:** PostgreSQL (Heroku)
- **Authentication:** Token-based (rest_framework.authtoken)
- **Deployment:** Heroku

### Frontend
- **Framework:** React 19 + Vite
- **Router:** React Router v7.13
- **State Management:** React Context API
- **Styling:** CSS with purple-pink gradient theme
- **Deployment:** Netlify

---

## 🚀 Quick Start Guide

### Step 1: Register a New User

**In Insomnia/Postman:**
```
Method: POST
URL: https://yubo-crowdfunding-shecodes-f2aced9e5879.herokuapp.com/users/
Body (JSON):
{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "secure_password"
}
```

✅ **Response (201 Created):**
```json
{
  "id": 1,
  "username": "your_username",
  "email": "your_email@example.com"
}
```

### Step 2: Get Authentication Token

```
Method: POST
URL: https://yubo-crowdfunding-shecodes-f2aced9e5879.herokuapp.com/api-token-auth/
Body (JSON):
{
  "username": "your_username",
  "password": "secure_password"
}
```

✅ **Response (200 OK):**
```json
{
  "token": "your_token_here",
  "user_id": 1,
  "email": "your_email@example.com"
}
```

**Save the token for all authenticated requests!**

### Step 3: Create Your First Campaign

```
Method: POST
URL: https://yubo-crowdfunding-shecodes-f2aced9e5879.herokuapp.com/fundraisers/
Headers:
  Authorization: Token your_token_here
  Content-Type: application/json
Body (JSON):
{
  "title": "Best K-Beauty Moisturizers Comparison",
  "description": "I'll test and review the top Korean skincare moisturizers",
  "goal": 500,
  "image": "https://example.com/campaign.jpg",
  "category": "Skincare",
  "is_open": true
}
```

✅ **Response (201 Created):** Campaign object with id

### Step 4: View Your Campaign

```
Method: GET
URL: https://yubo-crowdfunding-shecodes-f2aced9e5879.herokuapp.com/fundraisers/{campaign_id}/
```

✅ **Response (200 OK):** Full campaign details with nested pledges

### Step 5: Make a Pledge

```
Method: POST
URL: https://yubo-crowdfunding-shecodes-f2aced9e5879.herokuapp.com/pledges/
Headers:
  Authorization: Token your_token_here
  Content-Type: application/json
Body (JSON):
{
  "amount": 50,
  "comment": "Love this campaign!",
  "anonymous": false,
  "fundraiser": 1
}
```

✅ **Response (201 Created):** Pledge object

---

## 📚 API Specification

### API Root - Documentation Endpoint
```
GET https://yubo-crowdfunding-shecodes-f2aced9e5879.herokuapp.com/
```

Returns comprehensive JSON documentation of all available endpoints, features, and validation rules.

### Authentication Endpoint
```
POST /api-token-auth/
Content-Type: application/json

Request:
{
  "username": "user",
  "password": "pass"
}

Response (200 OK):
{
  "token": "string",
  "user_id": integer,
  "email": "string"
}
```

### User Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|----------------|
| GET | /users/ | List all users | No |
| POST | /users/ | Register new user | No |
| GET | /users/{id}/ | Get user profile | No |
| GET | /users/me/ | Get current user | Yes |
| PUT | /users/{id}/ | Update profile | Yes (owner) |
| DELETE | /users/{id}/ | Delete account | Yes (owner) |

### Fundraiser Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|----------------|
| GET | /fundraisers/ | List campaigns (search: ?search=, category: ?category=, is_open: ?is_open=, funded: ?funded=) | No |
| POST | /fundraisers/ | Create campaign | Yes |
| GET | /fundraisers/{id}/ | Get campaign with pledges | No |
| PUT | /fundraisers/{id}/ | Update campaign | Yes (owner) |
| DELETE | /fundraisers/{id}/ | Delete campaign | Yes (owner) |

### Pledge Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|----------------|
| GET | /pledges/ | List all pledges | No |
| POST | /pledges/ | Create pledge | Yes + Validation |
| GET | /pledges/{id}/ | Get pledge | No |
| PUT | /pledges/{id}/ | Update pledge | Yes (supporter) |
| DELETE | /pledges/{id}/ | Delete pledge | Yes (supporter) |

---

## 📊 Database Schema

```
┌─────────────────────────────────┐
│         User (customUser)       │
├─────────────────────────────────┤
│ id (PK)                         │
│ username (unique)               │
│ email                           │
│ password (hashed)               │
│ date_joined                     │
│ is_active                       │
└──────────────┬──────────────────┘
               │
         ┌─────┼─────┐
         │           │
         ▼           ▼
┌─────────────────┐  ┌──────────────────┐
│  Fundraiser     │  │      Pledge      │
├─────────────────┤  ├──────────────────┤
│ id (PK)         │  │ id (PK)          │
│ title           │  │ amount           │
│ description     │  │ comment          │
│ goal            │  │ anonymous        │
│ image (URL)     │  │ date_created     │
│ is_open         │  │ fundraiser (FK)  │
│ is_public       │  │ supporter (FK)   │
│ category        │  │ unique_together: │
│ product_link    │  │  (fundraiser,    │
│ date_created    │  │   supporter)     │
│ deadline        │  │                  │
│ owner (FK)  ────┼──┤ foreign keys:    │
│             ────┼──│  CASCADE delete  │
└─────────────────┘  └──────────────────┘
        ▲
        │
   Many-to-Many through Pledges
```

### Relationships
- **User → Fundraiser** (One-to-Many): User owns many campaigns
- **User → Pledge** (One-to-Many): User makes many pledges
- **Fundraiser → Pledge** (One-to-Many): Campaign receives many pledges
- **Pledge Constraint**: unique_together('fundraiser', 'supporter')

---

## ✨ Advanced Features

| Feature | Description |
|---------|-------------|
| **Funding Goal Protection** | Pledges auto-blocked when goal reached |
| **Duplicate Pledge Prevention** | Users can only pledge once per campaign |
| **Pledge Validation** | Amount > 0, campaign must accept pledges |
| **Search & Filtering** | Search by title/description, filter by category/status/funding |
| **Calculated Fields** | total_pledged, is_funded, can_accept_pledges |
| **Campaign Deadlines** | Optional time-based campaign limits |
| **Permission Controls** | Owner/Supporter-only updates and deletes |
| **Nested Serializers** | Pledges included in campaign detail view |

---

## 🧪 Setup Instructions

### Prerequisites
- Python 3.12+
- Django 5.1
- PostgreSQL (Heroku) or SQLite (local)

### Local Development Setup

```bash
# Clone repository
git clone https://github.com/Veronica-Yubo-Chen/CrowdFunding_Backend
cd CrowdFunding_Backend

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cd crowdfunding
echo "DJANGO_SECRET_KEY=dev-secret" > .env
echo "DJANGO_DEBUG=True" >> .env

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start server
python manage.py runserver
```

Visit: http://localhost:8000

---

## 📋 Complete API Endpoint Reference
