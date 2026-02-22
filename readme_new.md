# ✨ Glwup ✨ - Beauty Product Crowdfunding Platform

**Vote with your wallet on beauty product reviews you want to see**

A full-stack crowdfunding platform for beauty enthusiasts to fund product reviews and comparisons. Support creators. Discover honest reviews. Get your glow up.

**Created by:** Veronica Yubo Chen

---

## 📱 Deployed Project

- **Frontend:** https://magnificent-meringuee-d6339fs.netlify.app
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

## 📋 Error Handling & Status Codes

### HTTP Status Codes Reference

| Code | Status | Meaning |
|------|--------|---------|
| 200 | OK | Request successful, returning data |
| 201 | Created | Resource successfully created |
| 204 | No Content | Successful delete (no response body) |
| 400 | Bad Request | Invalid input or validation error |
| 401 | Unauthorized | Missing authentication token |
| 403 | Forbidden | Authenticated but not authorized (e.g., not owner) |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Server-side error |

### Example Error Responses

**Invalid Amount Pledge:**
```json
POST /pledges/
Body: {"amount": 0, "fundraiser": 1, "comment": "test"}

Response (400 Bad Request):
{
  "amount": ["Amount must be greater than 0"]
}
```

**Duplicate Pledge:**
```json
POST /pledges/
Body: {"amount": 50, "fundraiser": 1, "comment": "test"} 
(User already pledged to fundraiser 1)

Response (400 Bad Request):
{
  "non_field_errors": ["You have already pledged to this campaign"]
}
```

**Unauthorized Update:**
```json
PUT /fundraisers/999/
Headers: Authorization: Token your_token

Response (403 Forbidden):
{
  "detail": "You do not have permission to perform this action."
}
```

**Resource Not Found:**
```json
GET /fundraisers/99999/

Response (404 Not Found):
{
  "detail": "Not found."
}
```

---

## 🔐 Environment Variables

### Backend (.env in crowdfunding/ directory)

```bash
# Production
DJANGO_SECRET_KEY=your_secret_key_here
DJANGO_DEBUG=False
DATABASE_URL=postgresql://user:password@host/dbname

# Development
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=dev-secret-only-local
```

### Frontend (.env in crowdfunding-frontend/ directory)

```bash
VITE_API_URL=https://yubo-crowdfunding-shecodes-f2aced9e5879.herokuapp.com
```

---

## 🧪 Testing with Insomnia

### Setting Up Insomnia

1. **Download & Install:** https://insomnia.rest/
2. **Create Workspace:** File → New Workspace
3. **Set Base URL:** Environment variables → Set `base_url` = `https://yubo-crowdfunding-shecodes-f2aced9e5879.herokuapp.com`

### Sample Requests

**Test 1: Register User**
```
POST {{ base_url }}/users/
Body (JSON):
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "testpass123"
}
```

**Test 2: Get Token**
```
POST {{ base_url }}/api-token-auth/
Body (JSON):
{
  "username": "testuser",
  "password": "testpass123"
}
```
Save the token to a variable: `token`

**Test 3: Create Campaign (Using Token)**
```
POST {{ base_url }}/fundraisers/
Headers:
  Authorization: Token {{ token }}
Body (JSON):
{
  "title": "Vitamin C Serum Review",
  "description": "Testing top vitamin C serums",
  "goal": 500,
  "image": "https://via.placeholder.com/400",
  "category": "Skincare",
  "is_open": true
}
```

**Test 4: View Campaign with Pledges**
```
GET {{ base_url }}/fundraisers/1/
```

**Test 5: Create Pledge**
```
POST {{ base_url }}/pledges/
Headers:
  Authorization: Token {{ token }}
Body (JSON):
{
  "amount": 25,
  "comment": "Excited to see the results!",
  "anonymous": false,
  "fundraiser": 1
}
```

### 📸 Screenshots
*[Insomnia GET request screenshot]*
*[Insomnia POST request screenshot]*
*[Token response screenshot]*

---

## 🏗️ Project Structure

```
CrowdFunding_Backend/
├── crowdfunding/                 # Django project settings
│   ├── __init__.py
│   ├── settings.py              # Database, installed apps, middleware
│   ├── urls.py                  # Root URL routing
│   ├── asgi.py & wsgi.py        # WSGI/ASGI interfaces
│   └── __pycache__/
│
├── users/                        # User app
│   ├── models.py                # Custom user model
│   ├── views.py                 # User CRUD endpoints
│   ├── serializers.py           # User serialization
│   ├── urls.py                  # User API routes
│   └── migrations/              # Database migrations
│
├── fundraisers/                  # Fundraiser app
│   ├── models.py                # Fundraiser & Pledge models
│   ├── views.py                 # Fundraiser & Pledge endpoints
│   ├── serializers.py           # Fundraisers & Pledges serialization
│   ├── urls.py                  # Fundraiser API routes
│   └── migrations/              # Database migrations
│
├── db.sqlite3                   # Development database
├── manage.py                    # Django CLI
├── requirements.txt             # Python dependencies
├── Procfile                     # Heroku deployment config
└── readme.md                    # This file
```

---

## 🎨 Design & Branding

### Glwup Brand Identity

**Color Palette:**
- Primary Purple: `#9b59b6`
- Secondary Pink: `#c44569`
- Background Gradient: Purple → Pink
- Text: Dark gray on light backgrounds

**Typography:**
- Primary font: System default or Poppins
- Sizes: 16px (body), 24px (headings), 32px (titles)

**Logo Concept:**
"Glow Up" = empowerment through beauty product knowledge

**Target Aesthetic:**
Modern, clean, feminine, empowering, beauty-focused

---

## ✅ Requirements Checklist

### Lesson Requirements

#### ✅ **Users App**
- [x] User model with username, email, password
- [x] Token authentication endpoint
- [x] User list endpoint (GET /users/)
- [x] User detail endpoint (GET /users/{id}/)
- [x] User registration endpoint (POST /users/)
- [x] User self-update endpoint (PUT /users/{id}/, owner only)
- [x] User self-delete endpoint (DELETE /users/{id}/, owner only)
- [x] Current user endpoint (GET /users/me/)
- [x] Authentication token includes user details

#### ✅ **Fundraisers App**
- [x] Fundraiser model with title, description, goal, image, is_open fields
- [x] Fundraiser list endpoint (GET /fundraisers/)
- [x] Fundraiser detail endpoint (GET /fundraisers/{id}/)
- [x] Fundraiser create endpoint (POST /fundraisers/, authenticated)
- [x] Fundraiser update endpoint (PUT /fundraisers/{id}/, owner only)
- [x] Fundraiser delete endpoint (DELETE /fundraisers/{id}/, owner only)
- [x] Owner field on Fundraiser model
- [x] Nested pledges in fundraiser detail view
- [x] Search functionality (?search=term)
- [x] Filtering by status (?is_open=true), category (?category=Skincare)
- [x] Filtering by funding status (?funded=true)

#### ✅ **Pledges App**
- [x] Pledge model with amount, comment, anonymous, date_created fields
- [x] Pledge list endpoint (GET /pledges/)
- [x] Pledge detail endpoint (GET /pledges/{id}/)
- [x] Pledge create endpoint (POST /pledges/, authenticated)
- [x] Pledge update endpoint (PUT /pledges/{id}/, supporter only)
- [x] Pledge delete endpoint (DELETE /pledges/{id}/, supporter only)
- [x] Supporter field on Pledge model
- [x] Campaign field (foreign key to Fundraiser) on Pledge
- [x] Amount validation (> 0)
- [x] Duplicate pledge prevention (one pledge per user per campaign)
- [x] Funding goal protection (cannot pledge to funded campaigns)
- [x] Campaign deadline support (optional)

#### ✅ **Model Relationships**
- [x] User → Fundraiser (One-to-Many): owner field
- [x] User → Pledge (One-to-Many): supporter field
- [x] Fundraiser → Pledge (One-to-Many): campaign field
- [x] Pledge unique constraint: (campaign, supporter)
- [x] CASCADE on delete for FK relationships

#### ✅ **Permissions**
- [x] Custom IsOwnerOrReadOnly permission (Fundraiser updates)
- [x] Custom IsSupporterOrReadOnly permission (Pledge updates)
- [x] IsAuthenticatedOrReadOnly for fundraiser creation
- [x] Manual permission checks for sensitive operations
- [x] 403 Forbidden for unauthorized actions
- [x] 404 for accessing non-existent resources

#### ✅ **Validation**
- [x] Serializer-level validation (amount > 0)
- [x] Model-level validation (clean() method)
- [x] Duplicate pledge validation
- [x] Campaign acceptance validation (is_open, deadline, goal)
- [x] 400 Bad Request with detailed error messages
- [x] Proper error response structure

#### ✅ **Frontend Integration**
- [x] React frontend deployed on Netlify
- [x] API calls using fetch + async/await
- [x] Authentication context (AuthProvider)
- [x] useAuth hook for state management
- [x] Login functionality with token storage
- [x] Create fundraiser form
- [x] Pledge creation form
- [x] User profile page
- [x] Responsive design with media queries
- [x] Glwup branding and purple-pink theme

#### ✅ **API Quality**
- [x] RESTful endpoint design
- [x] Proper HTTP methods (GET, POST, PUT, DELETE)
- [x] Proper status codes (200, 201, 204, 400, 403, 404)
- [x] JSON request/response format
- [x] CORS configured for Netlify frontend
- [x] Error responses in JSON format
- [x] Calculated fields (total_pledged, is_funded, can_accept_pledges)
- [x] Nested serializers (pledges in campaign detail)

#### ✅ **Deployment**
- [x] Backend deployed to Heroku
- [x] Frontend deployed to Netlify
- [x] Auto-deployment on git push
- [x] Environment variables configured
- [x] Database migrations in production
- [x] Secret key secure (env variable)

### Additional Features Beyond Requirements

- ✨ Campaign deadline support for time-limited fundraising
- ✨ is_public field for visibility control
- ✨ Pledge anonymous option for privacy-conscious supporters
- ✨ Product link field for easy access to reviewed products
- ✨ Category field for better organization
- ✨ Glwup branding and beautiful UI
- ✨ Advanced search with title AND description
- ✨ Multiple filter options (category, status, funding)
- ✨ Comprehensive API documentation at root endpoint
- ✨ Error handling with helpful messages
- ✨ Professional README with quick start guide

---

## 🔗 Repository Links

- **Frontend Repository:** https://github.com/Veronica-Yubo-Chen/crowdfunding-frontend
- **Backend Repository:** https://github.com/Veronica-Yubo-Chen/CrowdFunding_Backend

---

## 📧 Support

For questions or issues, please reach out to:
- **Email:** yuboveronicachen@gmail.com
- **GitHub:** [@Veronica-Yubo-Chen](https://github.com/Veronica-Yubo-Chen)

---

## 📄 License

This project is created for She Codes Plus.

---

**Last Updated:** December 2024
**Version:** 1.0.0 - Production Ready ✨
