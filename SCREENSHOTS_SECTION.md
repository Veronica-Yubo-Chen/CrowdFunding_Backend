# 📸 Project Screenshots

This section contains screenshots demonstrating the key features of the Glwup crowdfunding platform. Please add the following screenshots to your README.md file:

## 1. Homepage / Fundraiser List
**File:** `homepage-screenshot.png`
**What to show:**
- Purple-pink gradient navbar with Glwup logo
- Hero section with "Vote with your wallet" tagline and "Create Campaign" button
- Grid of fundraiser cards showing:
  - Campaign image
  - Campaign title
  - Campaign description
  - Progress bar with funded amount vs goal
  - Category badge

**Instructions to take screenshot:**
1. Navigate to home page: https://magnificent-meringuee-d6339fs.netlify.app
2. Scroll down to show multiple fundraiser cards
3. Capture the full page layout

---

## 2. Fundraiser Creation Page
**File:** `create-campaign-page.png`
**What to show:**
- Page title: "Create a New Fundraiser"
- Form with all input fields visible
- Purple gradient submit button

**Instructions to take screenshot:**
1. Login to the app
2. Navigate to "Create Campaign" or "/create-fundraiser"
3. Show the empty form with all fields visible
4. Include labels: Title, Description, Goal Amount, Image URL, Category, Product Link

---

## 3. Fundraiser Creation Form (Filled)
**File:** `create-campaign-filled.png`
**What to show:**
- Form with sample data filled in:
  - Title: "Top 10 K-Beauty Serums Review"
  - Description: "Testing the most popular Korean beauty serums..."
  - Goal: 500
  - Image URL: Valid product image
  - Category: "Skincare"
- Submit button ready to click

**Instructions to take screenshot:**
1. Fill in the form with sample beauty-related data
2. Show all fields completed
3. Don't submit yet

---

## 4. Fundraiser Detail Page with Pledges
**File:** `fundraiser-detail-pledges.png`
**What to show:**
- Campaign details (image, title, description, goal, current amount raised)
- Progress bar showing funding status
- "Pledge Now" button/section
- Existing pledges list with:
  - Pledge amount (in purple/pink color)
  - Supporter name or "Anonymous"
  - Comment
  - Date pledged

**Instructions to take screenshot:**
1. Click on any fundraiser card to view details
2. Scroll down to show pledges from supporters
3. Show at least 2-3 pledges to demonstrate the feature
4. Include the "Pledge Now" form (visible or collapsed)

---

## 5. Pledge Creation Form
**File:** `pledge-form.png`
**What to show:**
- Pledge form with fields:
  - Amount (number input)
  - Comment (text area)
  - Anonymous checkbox
- Purple gradient "Pledge" button
- Form properly styled with Glwup colors

**Instructions to take screenshot:**
1. Navigate to a fundraiser detail page
2. Scroll to pledge section or click "Pledge Now"
3. Show the form with sample data:
  - Amount: 50
  - Comment: "Love this idea! Can't wait to see the results."
  - Anonymous: unchecked

---

## 6. Unauthorized Edit Attempt (Optional but Recommended)
**File:** `unauthorized-edit.png`
**What to show:**
- Either:
  - Option A: A 403 Forbidden message when non-owner tries to edit
  - Option B: Edit button disabled/hidden for non-owners
  - Option C: Error message in console (browser DevTools)

**Instructions to take screenshot:**
1. Login as User A, create a campaign
2. Login as User B (different account)
3. Navigate to User A's campaign
4. Try to click edit button (if visible) or show that edit button is hidden
5. If button exists and you click it, capture the error message

---

## How to Add Screenshots to README

1. **Save screenshots** with names matching above (e.g., `homepage-screenshot.png`)
2. **Place them in a folder** in your repository (e.g., `screenshots/` folder)
3. **Add to your README.md** in the deployment section:

```markdown
## 📸 Project Screenshots

### Homepage
![Glwup Homepage - Fundraiser List](screenshots/homepage-screenshot.png)
*The main page showing featured fundraisers with our purple-pink gradient theme*

### Create Campaign
![Create Fundraiser Form](screenshots/create-campaign-page.png)
*Form for creating a new beauty product review campaign*

### Campaign Details
![Fundraiser Detail with Pledges](screenshots/fundraiser-detail-pledges.png)
*Detailed view of a campaign showing pledges from supporters*

### Pledge Form
![Pledge Creation Form](screenshots/pledge-form.png)
*User pledging to support a campaign*
```

4. **Commit and push** to GitHub:
```bash
git add screenshots/
git add readme.md
git commit -m "Add project screenshots to README"
git push origin main
```

---

## Alternative: Using GitHub-hosted Images

If you don't want to commit image files, you can:
1. Upload screenshots to an image hosting service (imgur.com, imgur.io)
2. Use the image URLs in markdown:
```markdown
![Homepage](https://imgur.com/your-image-url.png)
```

---

## Before You Submit

✅ Verify your README includes:
- [ ] Link to deployed frontend
- [ ] Link to deployed backend
- [ ] 4-5 screenshots showing key features
- [ ] All project information
- [ ] Setup and deployment instructions
- [ ] List of requirements met

✅ Test everything works:
- [ ] Homepage loads and shows fundraisers
- [ ] Registration works
- [ ] Login works
- [ ] Campaign creation works
- [ ] Pledge system works
- [ ] Permissions are enforced (can't edit others' campaigns)
- [ ] Responsive design works on mobile

Then submit to: https://forms.gle/34ymxgPhdT8YXDgF6
