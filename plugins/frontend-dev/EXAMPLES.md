# Frontend Development Plugin - Examples

Real-world examples of using the frontend development plugin for closed-loop visual testing.

## Table of Contents
1. [Testing a New Component](#testing-a-new-component)
2. [Full Feature Implementation](#full-feature-implementation)
3. [Fixing Styling Issues](#fixing-styling-issues)
4. [Form Validation Testing](#form-validation-testing)
5. [Responsive Design Testing](#responsive-design-testing)
6. [Error State Testing](#error-state-testing)
7. [Interactive Widget Testing](#interactive-widget-testing)
8. [Integration Testing](#integration-testing)

---

## Testing a New Component

**Scenario**: You've created a new ProductCard component and want to verify it displays correctly.

### Conversation

```
You: I just created a ProductCard component in src/components/ProductCard.tsx.
Can you test it?

Claude: I'll test your ProductCard component visually. Let me use /test-frontend.

You: The card should show on the /products page.
Verify it displays the image, title, price, and "Add to Cart" button.

Claude:
✅ Dev server running at http://localhost:5173
🔍 Testing ProductCard component...

[Browser opens, navigates to /products]
[Screenshots captured]

📊 Test Results:
- ✅ Product cards rendering correctly
- ✅ Images loaded and displayed
- ✅ Title text visible and formatted
- ✅ Price shown in correct format ($XX.XX)
- ✅ "Add to Cart" button present and clickable
- ✅ Hover effects working
- ✅ No console errors

Visual Evidence:
[Screenshot 1: Products page with cards]
[Screenshot 2: Hover state on card]

Status: PASS ✅
```

---

## Full Feature Implementation

**Scenario**: Implementing a dark mode toggle with complete testing and validation.

### Conversation

```
You: /frontend-dev - Add a dark mode toggle to the navbar

Claude: I'll implement a dark mode toggle with full testing and validation.

Let me clarify the requirements:
- Where in the navbar? (left, center, right)
- What icon style? (moon/sun, lightbulb, generic toggle)
- Should the preference be persisted?
- Any specific styling?

You:
- Top right of navbar
- Moon icon for dark, sun icon for light
- Yes, persist with localStorage
- Match existing navbar button styles

Claude:
📋 Creating todo list for this workflow...

[TODO LIST]
1. ✅ Gather requirements
2. 🔄 Implement dark mode toggle
3. ⏳ Start/verify dev server
4. ⏳ Test implementation visually
5. ⏳ Validate against requirements
6. ⏳ Fix issues (if any)
7. ⏳ Complete workflow

Step 1: Implementing dark mode toggle...

Changes made:
- Created DarkModeToggle.tsx component
- Added dark mode context (DarkModeContext.tsx)
- Integrated toggle in Navbar.tsx
- Added dark mode styles to global.css
- Implemented localStorage persistence

✅ Implementation complete

Step 2: Starting dev server...
✅ Dev server running at http://localhost:5173

Step 3: Testing in browser...
[Browser automation]
- Navigated to home page
- Located dark mode toggle
- Initial state: Light mode ☀️
- Clicked toggle → Dark mode activated 🌙
- Screenshot captured
- Verified localStorage set
- Refreshed page → Dark mode persisted
- Console: 1 warning found

Console Warning:
⚠️ "React Hook useEffect has a missing dependency"

📸 Screenshots:
[Screenshot 1: Light mode]
[Screenshot 2: Dark mode activated]
[Screenshot 3: After page refresh - dark mode persisted]

Step 4: Validating against requirements...

❌ FAIL - Iteration Required

Issues Found:
1. MAJOR: Console warning about React Hook dependency
2. MINOR: Toggle animation could be smoother

Recommended fixes:
1. Add missing dependency to useEffect
2. Add CSS transition to toggle

Step 5: Fixing issues...

Fixed:
- Added 'theme' to useEffect dependency array
- Added transition: "all 0.3s ease" to toggle button

✅ Fixes applied

Step 6: Re-testing...
[Browser automation]
- All previous tests passed
- Console is clean ✅
- Animation is smooth ✅

📸 Screenshots:
[Screenshot 4: Smooth toggle animation]

Step 7: Re-validating...
✅ PASS - All requirements met!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Frontend Development Complete ✅
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Summary:
Dark mode toggle successfully implemented in navbar with persistence.

Changes Made:
- src/components/DarkModeToggle.tsx (created)
- src/contexts/DarkModeContext.tsx (created)
- src/components/Navbar.tsx (modified)
- src/styles/global.css (modified)

Test Results:
- ✅ Toggle visible in top right of navbar
- ✅ Moon/sun icons display correctly
- ✅ Clicking toggles between light and dark modes
- ✅ Preference persisted in localStorage
- ✅ Works after page refresh
- ✅ No console errors or warnings
- ✅ Smooth animation

Visual Evidence:
[Final screenshots showing complete functionality]

Would you like me to commit these changes?
```

---

## Fixing Styling Issues

**Scenario**: Button styles aren't matching the design mockup.

### Conversation

```
You: The primary button styling looks wrong. The background should be #3B82F6
and border-radius should be 8px. Can you fix it and test?

Claude: I'll fix the button styles and verify them visually.

[Edits Button.css]
[Hook detects change]

Recommendation: Frontend file changed (Stylesheet)
Run /test-frontend to verify the styling changes.

Claude: Let me test these changes.

/test-frontend

Testing button styles...
✅ Dev server running at http://localhost:5173

[Browser opens to /components/demo]
[Screenshots of button in different states]

📊 Test Results:
- ✅ Background color: #3B82F6 (correct)
- ✅ Border radius: 8px (correct)
- ✅ Hover state working
- ✅ Active state working
- ❌ Focus outline is missing

📸 Screenshots:
[Screenshot 1: Default state]
[Screenshot 2: Hover state]
[Screenshot 3: Active state]

Issue found: Focus outline missing for accessibility

Would you like me to add a focus outline?

You: Yes please, add a focus outline.

Claude:
[Adds focus outline style]
[Re-tests]

✅ Focus outline added and tested
📸 [Screenshot 4: Focus state with outline]

All styling now matches design requirements!
```

---

## Form Validation Testing

**Scenario**: Testing a complex form with multiple validation rules.

### Conversation

```
You: /test-frontend

Test the registration form at /signup:
1. Try submitting empty
2. Try with invalid email
3. Try with password too short
4. Try with valid data
5. Verify error messages display correctly

Claude:
Testing registration form with comprehensive validation scenarios...

✅ Dev server running at http://localhost:5173

Test Scenario 1: Submit empty form
[Browser action: Click submit with empty fields]
Result: ✅ Error messages shown for all fields
📸 [Screenshot 1: Empty form errors]

Test Scenario 2: Invalid email
[Browser action: Enter "notanemail" in email field, submit]
Result: ✅ Email validation error shown: "Please enter a valid email"
📸 [Screenshot 2: Email validation error]

Test Scenario 3: Short password
[Browser action: Enter "123" in password field, submit]
Result: ✅ Password error shown: "Password must be at least 8 characters"
📸 [Screenshot 3: Password validation error]

Test Scenario 4: Valid data
[Browser action: Fill all fields with valid data, submit]
Result: ❌ Console error: "POST /api/register 404"
📸 [Screenshot 4: Form submitted but API error]

Console Output:
Error: POST http://localhost:5173/api/register 404 (Not Found)

Issues Found:
1. CRITICAL: Form submits but API endpoint doesn't exist
2. The form validation works correctly
3. Error handling for API errors not implemented

Recommendations:
1. Either mock the API endpoint or handle 404 gracefully
2. Add loading state during submission
3. Add error message for failed submissions

Status: PARTIAL PASS ⚠️
- Form validation: Working correctly ✅
- API integration: Needs attention ❌
```

---

## Responsive Design Testing

**Scenario**: Verify a component works on different screen sizes.

### Conversation

```
You: /test-frontend

Test the hero section on mobile, tablet, and desktop sizes.
Check that the layout adapts correctly.

Claude:
Testing hero section responsiveness across viewport sizes...

Test 1: Desktop (1920x1080)
[Browser resized to 1920x1080]
[Screenshot captured]
Result: ✅ Two-column layout, image on right, text on left
📸 [Screenshot 1: Desktop layout]

Test 2: Tablet (768x1024)
[Browser resized to 768x1024]
[Screenshot captured]
Result: ✅ Stacked layout, image above text
📸 [Screenshot 2: Tablet layout]

Test 3: Mobile (375x667)
[Browser resized to 375x667]
[Screenshot captured]
Result: ❌ Text overflowing, button cut off
📸 [Screenshot 3: Mobile layout - overflow visible]

Console: No errors

Issues Found:
- Text overflows container on mobile
- CTA button is partially hidden
- Font size too large for mobile viewport

Would you like me to fix these responsive issues?

You: Yes, please fix them.

Claude:
[Modifies hero.css with media queries]
[Re-tests on all viewport sizes]

✅ All viewport sizes now display correctly
📸 [Screenshots showing fixed layouts]

Mobile fixes applied:
- Reduced heading font size
- Added proper text wrapping
- Made CTA button full-width on mobile
- Added padding adjustments
```

---

## Error State Testing

**Scenario**: Testing how the app handles error conditions.

### Conversation

```
You: /test-frontend

Test the user profile page when:
1. User data loads successfully
2. Network error occurs
3. User not found (404)

Claude:
Testing user profile page error states...

Note: To test error states, I'll need to simulate them.
This might require mocking or using browser DevTools.

Test 1: Successful load
[Navigate to /profile/john-doe]
Result: ✅ Profile loads, shows avatar, name, bio
📸 [Screenshot 1: Successful load]

Test 2: Network error simulation
[Use browser to simulate offline]
Result: ❌ App shows no error message, spinner loads forever
Console: Error: "Failed to fetch"
📸 [Screenshot 2: Loading spinner stuck]

Test 3: User not found
[Navigate to /profile/nonexistent-user]
Result: ❌ Blank page, no "user not found" message
Console: Error 404
📸 [Screenshot 3: Blank page]

Issues Found:
1. CRITICAL: No error handling for network failures
2. CRITICAL: No 404 error page for missing users
3. Loading spinner never times out

Recommendations:
1. Add error boundary to catch fetch errors
2. Add timeout for loading states
3. Show user-friendly error messages
4. Add "User not found" state
5. Add retry button for network errors

Status: FAIL ❌
Error handling needs to be implemented.

Would you like me to implement proper error handling?
```

---

## Interactive Widget Testing

**Scenario**: Testing a complex interactive component (e.g., date picker).

### Conversation

```
You: /test-frontend

Test the date picker component:
1. Click to open calendar
2. Select a date
3. Verify the selected date displays
4. Test keyboard navigation

Claude:
Testing date picker component interaction...

✅ Dev server running at http://localhost:5173

Test 1: Open calendar
[Click date picker input]
Result: ✅ Calendar popover opens
📸 [Screenshot 1: Calendar opened]

Test 2: Select date
[Click on date: March 15, 2024]
Result: ✅ Date selected, popover closes
Value: "03/15/2024"
📸 [Screenshot 2: Date selected]

Test 3: Display verification
[Check input field value]
Result: ✅ Selected date displays in correct format
📸 [Screenshot 3: Date displayed in input]

Test 4: Keyboard navigation
[Open calendar, press Arrow keys]
Result: ❌ Keyboard navigation not working
Pressing arrows doesn't move focus between dates
Console: No errors

Additional findings:
- ✅ Previous/Next month buttons work
- ✅ Year dropdown works
- ✅ Today button works
- ❌ Escape key doesn't close calendar
- ❌ Enter key doesn't select focused date

Issues Found:
1. MAJOR: Keyboard navigation not implemented
2. MAJOR: Escape key doesn't close calendar
3. Accessibility: ARIA labels present ✅
4. Accessibility: Focus management needs improvement

Status: PARTIAL PASS ⚠️
Mouse interaction works, keyboard accessibility needs work.

Recommendations:
1. Add keyboard event handlers for arrow keys
2. Add Escape key to close
3. Add Enter key to select
4. Add focus trap inside calendar
```

---

## Integration Testing

**Scenario**: Testing a complete user flow across multiple pages.

### Conversation

```
You: /test-frontend

Test the complete checkout flow:
1. Browse products
2. Add item to cart
3. Go to cart
4. Proceed to checkout
5. Fill shipping form
6. Review order
7. Confirm (mock payment)

Claude:
Testing complete checkout flow with multi-page navigation...

✅ Dev server running at http://localhost:5173

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Flow Step 1: Browse products
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Navigate to /products]
Result: ✅ Products page loaded
Products visible: 12
📸 [Screenshot 1: Products page]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Flow Step 2: Add item to cart
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Click "Add to Cart" on first product]
Result: ✅ Success notification shown
Cart badge: Updated to "1"
📸 [Screenshot 2: Item added notification]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Flow Step 3: Go to cart
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Click cart icon]
Result: ✅ Cart page displayed
Items in cart: 1
Subtotal: $29.99
📸 [Screenshot 3: Cart page]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Flow Step 4: Proceed to checkout
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Click "Proceed to Checkout"]
Result: ✅ Redirected to /checkout
📸 [Screenshot 4: Checkout page]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Flow Step 5: Fill shipping form
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Fill form fields]
- Name: John Doe
- Address: 123 Main St
- City: Springfield
- ZIP: 12345
- Email: john@example.com
[Click "Continue"]
Result: ✅ Form submitted successfully
📸 [Screenshot 5: Form filled]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Flow Step 6: Review order
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Result: ✅ Order review page shown
Order details correct:
- Item: Product Name - $29.99
- Shipping: $5.00
- Total: $34.99
📸 [Screenshot 6: Order review]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Flow Step 7: Confirm order
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Click "Place Order"]
Result: ✅ Success! Redirected to /order-confirmation
Order ID: #12345
📸 [Screenshot 7: Order confirmation]

Console Output:
✅ No errors
ℹ️ 3 informational logs (state updates)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Test Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Status: PASS ✅

Complete checkout flow works end-to-end:
- ✅ Product browsing
- ✅ Cart functionality
- ✅ Form submission
- ✅ Navigation between pages
- ✅ Order confirmation
- ✅ No console errors
- ✅ All interactions smooth

Total time: ~45 seconds
Screenshots captured: 7
Pages tested: 5

The checkout flow is working correctly!
```

---

## Best Practices from Examples

1. **Be Specific**: Define exact test scenarios
2. **Test Edge Cases**: Empty forms, invalid data, error states
3. **Check Console**: Always monitor for errors
4. **Capture Evidence**: Screenshots prove functionality
5. **Test Complete Flows**: Don't just test isolated components
6. **Iterate on Failures**: Use validation feedback to improve
7. **Consider Accessibility**: Test keyboard navigation
8. **Test Responsiveness**: Multiple viewport sizes
9. **Verify Persistence**: LocalStorage, cookies, etc.
10. **End-to-End Flows**: Test real user journeys

---

## Additional Resources

- [README.md](README.md) - Full documentation
- [SETUP.md](SETUP.md) - Quick setup guide
- [GitHub Issues](https://github.com/anthropics/claude-code/issues) - Report issues or request features

Happy testing! 🎉
