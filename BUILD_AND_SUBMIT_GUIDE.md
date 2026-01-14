# Tea Timer - Build & Submit to App Store Guide

Complete step-by-step guide to build and submit your app to the App Store.

---

## Step 1: Get Your Team ID

1. Go to [Apple Developer Portal](https://developer.apple.com/account)
2. Sign in with your Apple Developer account
3. Click "Membership" in the sidebar
4. Your **Team ID** will be shown (10 characters, like "A1B2C3D4E5")
5. **Copy this Team ID** - you'll need it next

---

## Step 2: Update Project with Team ID

Once you have your Team ID, run this command (replace YOUR_TEAM_ID):

```bash
# Update project.yml with your Team ID
sed -i '' 's/teamID: ""/teamID: "YOUR_TEAM_ID"/' project.yml
sed -i '' 's/DEVELOPMENT_TEAM: ""/DEVELOPMENT_TEAM: "YOUR_TEAM_ID"/' project.yml

# Regenerate Xcode project
xcodegen generate
```

**OR manually edit `project.yml`:**
- Line 10: Change `teamID: ""` to `teamID: "YOUR_TEAM_ID"`
- Line 32: Change `DEVELOPMENT_TEAM: ""` to `DEVELOPMENT_TEAM: "YOUR_TEAM_ID"`

Then run: `xcodegen generate`

---

## Step 3: Register App ID (Optional - Xcode can do this)

If you want to manually register the App ID:

1. Go to [Certificates, Identifiers & Profiles](https://developer.apple.com/account/resources/identifiers/list)
2. Click the "+" button
3. Select "App IDs" → Continue
4. Type: **App**
5. Description: "Tea Timer"
6. Bundle ID: **com.raymondluo.teatimer** (Explicit)
7. Capabilities:
   - ✅ Push Notifications (for future features, optional)
8. Click "Continue" → "Register"

**Note**: Xcode can register the App ID automatically when you archive, so this step is optional.

---

## Step 4: Create App in App Store Connect

1. Go to [App Store Connect](https://appstoreconnect.apple.com)
2. Click "My Apps"
3. Click the "+" button → "New App"
4. Fill in the form:
   - **Platforms**: iOS
   - **Name**: Tea Timer
   - **Primary Language**: English (U.S.)
   - **Bundle ID**: Select "com.raymondluo.teatimer" from dropdown
   - **SKU**: teatimer-ios-2026 (unique identifier for your records)
   - **User Access**: Full Access
5. Click "Create"

---

## Step 5: Build & Archive in Xcode

### Option A: Using Xcode GUI (Recommended for first submission)

1. **Open Xcode project**:
   ```bash
   open TeaTimer.xcodeproj
   ```

2. **Select a Real Device or "Any iOS Device"**:
   - In the top toolbar, click the device selector
   - Choose "Any iOS Device (arm64)" (NOT simulator)

3. **Archive the app**:
   - Menu: **Product** → **Archive**
   - Wait for build to complete (1-2 minutes)
   - Xcode Organizer window will open automatically

4. **Validate the Archive** (recommended):
   - Select your archive
   - Click "Validate App"
   - Choose your Apple ID / Team
   - Accept defaults
   - Wait for validation (checks for issues)
   - Should say "Validation Successful"

5. **Distribute the Archive**:
   - Click "Distribute App"
   - Select "App Store Connect"
   - Click "Upload"
   - Choose your distribution certificate (Xcode manages this automatically)
   - Review app info → Click "Upload"
   - Wait for upload (may take 5-10 minutes depending on connection)

### Option B: Using Command Line (Advanced)

```bash
# Clean build folder
rm -rf build/

# Archive the app
xcodebuild archive \
  -scheme TeaTimer \
  -archivePath build/TeaTimer.xcarchive \
  -configuration Release \
  CODE_SIGN_STYLE=Automatic \
  DEVELOPMENT_TEAM=YOUR_TEAM_ID

# Export for App Store
xcodebuild -exportArchive \
  -archivePath build/TeaTimer.xcarchive \
  -exportPath build/ \
  -exportOptionsPlist ExportOptions.plist
```

---

## Step 6: Wait for Processing

After upload:
1. Go to [App Store Connect](https://appstoreconnect.apple.com)
2. Select your app
3. Go to "TestFlight" tab or "App Store" tab
4. The build will show "Processing" (10-30 minutes)
5. You'll get an email when processing is complete
6. If there are issues, you'll get an email with details

---

## Step 7: Fill in App Store Metadata

While waiting for build processing, fill in your app information:

1. Go to your app in App Store Connect
2. Under "App Information":
   - **Name**: Tea Timer
   - **Subtitle**: Gongfu Tea Brewing Master
   - **Privacy Policy URL**: `https://rlraymondluo.github.io/tea-timer/privacy.html`

3. Under "Pricing and Availability":
   - **Price**: Free
   - **Availability**: All territories (or select specific countries)

4. Go to version "1.0 Prepare for Submission":

   **Promotional Text** (170 chars, appears above description):
   ```
   Perfect every steep with precision timing for traditional Gongfu tea brewing. Track unlimited rounds with automatic time adjustments and gentle alerts.
   ```

   **Description** (from APP_STORE_LISTING.md):
   - Copy the full description text
   - Paste into description field

   **Keywords** (100 chars):
   ```
   tea,timer,gongfu,brewing,steep,oolong,puerh,green tea,ceremony,mindful,meditation,chinese tea
   ```

   **Support URL**: `https://rlraymondluo.github.io/tea-timer/support.html`

   **Marketing URL** (optional): `https://rlraymondluo.github.io/tea-timer/`

5. **Screenshots**:
   - Upload from `AppStoreScreenshots/Resized/`
   - For 6.7" Display (iPhone 16 Pro Max, required):
     - `01_tea_selection_marketing_6.7inch.png`
     - `02_timer_view_marketing_6.7inch.png`
     - `03_dark_mode_timer_marketing_6.7inch.png`
   - For 6.5" Display (optional but recommended):
     - Upload the 6.5inch versions
   - For 5.5" Display (optional):
     - Upload the 5.5inch versions

6. **App Icon**:
   - This is pulled from your build automatically
   - Should show the tea cup icon

7. **Age Rating**:
   - Click "Edit"
   - Answer questions (all "No")
   - Result should be: **4+**

8. **App Review Information**:
   - **Contact Information**:
     - First Name: Raymond
     - Last Name: Luo
     - Phone: [Your phone]
     - Email: [Your email]

   - **Notes** (optional but helpful):
     ```
     Tea Timer is a specialized timer for traditional Chinese Gongfu tea brewing.

     How to test:
     1. Select "Green Tea" from the main screen
     2. Tap "Start Timer" to begin the first steep
     3. Timer counts down and plays a gentle chime when complete
     4. App automatically advances to next round
     5. After 5 predefined rounds, app continues with "additional steeps"
        that automatically add time to each subsequent round

     No login required. Works entirely offline. No data collection.
     ```

9. **Version Release**:
   - Select "Automatically release this version"
   - Or "Manually release this version" if you want to control timing

---

## Step 8: Select Build & Submit

1. Under "Build", click "Select a build before you submit your app"
2. Choose your uploaded build (version 1.0, build 1)
3. Click "Done"

4. **Export Compliance** (if asked):
   - Does your app use encryption? **No**
   - (Standard HTTPS doesn't count as encryption requiring declaration)

5. **Advertising Identifier**:
   - Does your app use the Advertising Identifier? **No**

6. Review everything one last time

7. Click **"Submit for Review"**

---

## Step 9: Wait for Review

- **Typical review time**: 24-48 hours
- You'll get emails about:
  - "In Review" - Apple is testing your app
  - "Pending Developer Release" or "Ready for Sale" - Approved!
  - "Rejected" - If there are issues (you can fix and resubmit)

---

## Common Issues & Solutions

### Issue: "Code signing failed"
**Solution**: Make sure you added your Team ID to project.yml and regenerated the project.

### Issue: "Provisioning profile doesn't include the application identifier"
**Solution**:
1. In Xcode, go to Signing & Capabilities
2. Check "Automatically manage signing"
3. Select your team
4. Clean build folder (Product → Clean Build Folder)

### Issue: "Archive not showing in Organizer"
**Solution**: Make sure you selected "Any iOS Device" (not a simulator) before archiving.

### Issue: "Missing required icon"
**Solution**: Your app icon should be in `TeaTimer/Assets.xcassets/AppIcon.appiconset/`. If missing, run `./generate_assets.sh` again.

### Issue: "Invalid Bundle Structure"
**Solution**: This usually means a framework or resource isn't properly embedded. Check that all files compile correctly.

### Issue: "Missing Privacy Policy"
**Solution**: Verify your GitHub Pages URL is accessible: https://rlraymondluo.github.io/tea-timer/privacy.html

---

## TestFlight (Optional - Before Public Release)

Before submitting to App Store, you can test via TestFlight:

1. After build processes in App Store Connect
2. Go to TestFlight tab
3. Add yourself as an internal tester
4. Install TestFlight app on your iPhone
5. You'll get an email invitation
6. Install and test your app
7. Fix any issues and upload a new build if needed

---

## After Approval

Once approved:
1. App will appear on App Store within a few hours
2. Update your landing page:
   - Add App Store badge with link
   - Remove "Coming Soon" text
3. Share on social media, tea forums, etc.
4. Monitor reviews and ratings
5. Respond to user feedback

---

## Quick Checklist

Before submitting, verify:

- [ ] Team ID added to project.yml
- [ ] Project regenerated with xcodegen
- [ ] App builds without errors
- [ ] All 3 screenshots uploaded (6.7" required)
- [ ] Privacy policy URL accessible
- [ ] Support URL accessible
- [ ] App description, keywords filled in
- [ ] Age rating set to 4+
- [ ] Contact information added
- [ ] Build uploaded and processed
- [ ] Build selected in App Store Connect
- [ ] Export compliance answered
- [ ] Submitted for review

---

## Support

If you run into issues:
- Check Xcode's issue navigator (⌘ + 5)
- Look at organizer logs (Window → Organizer)
- Apple's review feedback is usually clear and actionable
- You can appeal rejections if you believe they're incorrect

Good luck with your submission! 🍵
