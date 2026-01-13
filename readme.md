# Glwup - Beauty Product Crowdfunding Platform (generate from LLM)
**By Veronica Yubo Chen**

## Planning

### Concept/Name
**Glwup** (pronounced "Glow Up") is a crowdfunding platform for beauty enthusiasts. Users can create campaigns to fund product reviews, comparisons, and beauty content. Supporters pledge to campaigns they're interested in, and creators provide detailed product comparisons with links to purchase the reviewed items.

The platform connects beauty content creators with their audience, allowing the community to vote with their wallets on which product comparisons they want to see.

### Intended Audience/User Stories
**Target Audience:** Beauty enthusiasts, skincare lovers, makeup artists, and content creators aged 18-45 who want honest product comparisons before making purchases.

**User Stories:**
- As a **beauty content creator**, I want to create fundraising campaigns so that I can fund product reviews and comparisons.
- As a **beauty enthusiast**, I want to support campaigns for products I'm interested in so that I can get honest reviews.
- As a **supporter**, I want to pledge anonymously if I prefer privacy.
- As a **campaign owner**, I want to update my campaign description to keep supporters informed.
- As a **user**, I want to see external links to products so I can purchase them directly.

### Front End Pages/Functionality
- **Home Page**
    - Display all open fundraising campaigns
    - Filter by category (Skincare, Makeup, Haircare, etc.)
    - Search functionality
    - Responsive grid layout

- **Campaign Detail Page**
    - Full campaign description and image
    - Progress bar showing funding goal
    - List of pledges (with anonymous option)
    - External product link button
    - Pledge form for authenticated users

- **Create Campaign Page** (Authenticated)
    - Form to create new fundraiser
    - Image URL input
    - Category selection
    - Product link input

- **User Profile Page**
    - View owned campaigns
    - View pledges made
    - Edit profile

- **Login/Register Pages**
    - User authentication forms
    - Token-based login

### API Spec

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------------ | --------------------- | ---------------------------- |
| `/fundraisers/` | GET | List all fundraisers | None | 200 | None |
| `/fundraisers/` | POST | Create new fundraiser | `{title, description, goal, image, category, product_link}` | 201 | Token Required |
| `/fundraisers/<id>/` | GET | Get fundraiser details | None | 200 | None |
| `/fundraisers/<id>/` | PUT | Update fundraiser | `{title, description, goal, image, is_open, category, product_link}` | 200 | Owner Only |
| `/fundraisers/<id>/` | DELETE | Delete fundraiser | None | 204 | Owner Only |
| `/pledges/` | GET | List all pledges | None | 200 | None |
| `/pledges/` | POST | Create new pledge | `{amount, comment, anonymous, fundraiser}` | 201 | Token Required |
| `/pledges/<id>/` | GET | Get pledge details | None | 200 | None |
| `/pledges/<id>/` | PUT | Update pledge | `{amount, comment, anonymous}` | 200 | Supporter Only |
| `/pledges/<id>/` | DELETE | Delete pledge | None | 204 | Supporter Only |
| `/users/` | GET | List all users | None | 200 | None |
| `/users/` | POST | Register new user | `{username, email, password}` | 201 | None |
| `/users/<id>/` | GET | Get user details | None | 200 | None |
| `/api-token-auth/` | POST | Obtain auth token | `{username, password}` | 200 | None |

### DB Schema

```
┌─────────────────────┐       ┌─────────────────────┐
│     customUser      │       │     Fundraiser      │
├─────────────────────┤       ├─────────────────────┤
│ id (PK)             │       │ id (PK)             │
│ username            │       │ title               │
│ email               │◄──────┤ owner (FK)          │
│ password            │       │ description         │
└─────────────────────┘       │ goal                │
         │                    │ image               │
         │                    │ is_open             │
         │                    │ date_created        │
         │                    │ category            │
         │                    │ product_link        │
         │                    └─────────────────────┘
         │                              │
         │                              │
         │                    ┌─────────────────────┐
         │                    │       Pledge        │
         │                    ├─────────────────────┤
         │                    │ id (PK)             │
         └───────────────────►│ supporter (FK)      │
                              │ fundraiser (FK)     │◄────┘
                              │ amount              │
                              │ comment             │
                              │ anonymous           │
                              └─────────────────────┘
```

## Setup Instructions

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Veronica-Yubo-Chen/CrowdFunding_Backend.git
cd CrowdFunding_Backend

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
cd crowdfunding
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### API Testing Examples

```bash
# Register a new user
curl -X POST http://127.0.0.1:8000/users/ \
  -H "Content-Type: application/json" \
  -d '{"username": "beautyqueen", "email": "beauty@example.com", "password": "securepass123"}'

# Get auth token
curl -X POST http://127.0.0.1:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "beautyqueen", "password": "securepass123"}'

# Create a fundraiser (use token from above)
curl -X POST http://127.0.0.1:8000/fundraisers/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{
    "title": "Top 5 Vitamin C Serums Comparison",
    "description": "I will test and compare the top 5 vitamin C serums on the market",
    "goal": 500,
    "image": "https://example.com/vitc-serum.jpg",
    "category": "Skincare",
    "product_link": "https://example.com/buy-serums"
  }'

# Create a pledge
curl -X POST http://127.0.0.1:8000/pledges/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{
    "amount": 25,
    "comment": "Can not wait to see the results!",
    "anonymous": false,
    "fundraiser": 1
  }'
```

## Features Implemented

- ✅ User registration and authentication
- ✅ Token-based authentication with user details
- ✅ CRUD operations for fundraisers
- ✅ CRUD operations for pledges
- ✅ Owner-only permissions for fundraiser updates
- ✅ Supporter-only permissions for pledge updates
- ✅ Custom 404 error handler (JSON response)
- ✅ Beauty-specific fields (category, product_link)
- ✅ Proper HTTP status codes
