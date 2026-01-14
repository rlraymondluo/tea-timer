# GitHub Pages Setup Guide

This guide will help you host your Tea Timer support pages on GitHub Pages.

## Step 1: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" button in the top right → "New repository"
3. Name it: `tea-timer`
4. Description: "Gongfu Tea Timer iOS App"
5. Make it **Public** (required for free GitHub Pages)
6. Don't initialize with README (we'll push our existing files)
7. Click "Create repository"

## Step 2: Initialize Git and Push Files

Open Terminal in your tea-timer directory and run:

```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit - Tea Timer iOS app"

# Add GitHub remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/tea-timer.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/YOUR_USERNAME/tea-timer`
2. Click "Settings" (top right)
3. In the left sidebar, click "Pages"
4. Under "Source":
   - Select **Deploy from a branch**
   - Branch: **main**
   - Folder: **/docs**
   - Click "Save"

5. Wait 1-2 minutes for deployment
6. Your site will be live at: `https://YOUR_USERNAME.github.io/tea-timer/`

## Step 4: Verify Your URLs

After deployment, verify these URLs work:

- **Main page:** `https://YOUR_USERNAME.github.io/tea-timer/`
- **Privacy Policy:** `https://YOUR_USERNAME.github.io/tea-timer/privacy.html`
- **Support Page:** `https://YOUR_USERNAME.github.io/tea-timer/support.html`

## Step 5: Update App Store Listing

Use these URLs in App Store Connect:

- **Privacy Policy URL:** `https://YOUR_USERNAME.github.io/tea-timer/privacy.html`
- **Support URL:** `https://YOUR_USERNAME.github.io/tea-timer/support.html`
- **Marketing URL (optional):** `https://YOUR_USERNAME.github.io/tea-timer/`

## Files Structure

```
tea-timer/
├── docs/                    # GitHub Pages root
│   ├── index.html          # Landing page
│   ├── privacy.html        # Privacy policy
│   └── support.html        # Support page
├── TeaTimer/               # iOS app source
├── AppStoreScreenshots/    # App Store assets
└── [other project files]
```

## Troubleshooting

### "404 - File not found"
- Make sure you selected `/docs` folder (not root)
- Wait a few minutes for changes to propagate
- Check that files are in the `docs/` directory

### "Page not loading"
- Verify the repository is Public
- Check GitHub Pages settings are enabled
- Look for deployment errors in Settings → Pages

### "Need to update content"
After making changes to HTML files:

```bash
git add docs/
git commit -m "Update support pages"
git push
```

Changes will appear within 1-2 minutes.

## Custom Domain (Optional)

If you want a custom domain like `teatimer.app`:

1. Buy domain from provider (Namecheap, Google Domains, etc.)
2. Add CNAME record pointing to: `YOUR_USERNAME.github.io`
3. In GitHub Pages settings, add your custom domain
4. Enable "Enforce HTTPS"

---

## Quick Commands Reference

```bash
# Update docs after changes
git add docs/
git commit -m "Update support/privacy pages"
git push

# Check git status
git status

# View remote URL
git remote -v
```

---

## Security Notes

- GitHub Pages sites are always public
- Don't put sensitive information in these files
- Privacy policy and support pages should be public anyway
- Your iOS source code in other directories won't be hosted (only `/docs`)

---

Your support pages will be live at:
**https://YOUR_USERNAME.github.io/tea-timer/**

Replace `YOUR_USERNAME` with your actual GitHub username!
