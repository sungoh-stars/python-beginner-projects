# Stock Portfolio Tracker — Project Curriculum (D1–D33)

**Project:** A backend service where I register my holdings and it shows current price, return, and asset allocation
**Goal:** My first project built 100% by my own hands → deploy → prove "I built this myself" in interviews
**Pace:** 2–3 sessions/week, 90 min each (algorithms stay daily)

**Rules**
- We write it line by line together at first, then I take the wheel. No copy-paste, type everything by hand.
- Days tagged `[NEW]` introduce a new concept: full explanation first, then step-by-step practice.
- I add holdings manually. Prices are fetched automatically by an API.

---

## Phase 1: Build the Skeleton (D1–D6)
Goal: Finish stock CRUD using Flask + DB I already know. No new concepts — all review.

- D1: Project folder structure + run a basic Flask app (already learned)
- D2: Design DB schema — `holdings` table (ticker, quantity, average cost). Use multi-table experience
- D3: Add a stock (Create) — form + INSERT
- D4: List stocks (Read) — SELECT + render to screen
- D5: Delete + Update a stock
- D6: Review + add error handlers (404/500)

Pass: Add, view, update, and delete a stock without breaking.

---

## Phase 2: Live Prices (D7–D12)
Goal: Fetch current prices from an external stock API. First new-tech zone of this project.

- D7: `[NEW]` What is the `requests` library? Start from what an HTTP request is
- D8: Pick a free stock API + get an API key (Finnhub / Alpha Vantage, etc.)
- D9: `[NEW]` Hide the API key with environment variables (.env) — why hiding matters
- D10: `[NEW]` Parse a JSON response — extract just the current price
- D11: Show the live price for each registered stock on screen
- D12: Review + handle API errors (ticker not found, slow response)

Pass: Real current prices show up for the stocks I registered.

---

## Phase 3: My Account (D13–D17)
Goal: Add auth so only "my portfolio" is visible. Mostly review.

- D13: `users` table + sign-up (bcrypt review)
- D14: Login + session (review)
- D15: Login check via middleware (`@app.before_request` review)
- D16: Show only my portfolio — link `user_id` to holdings
- D17: Review + logout

Pass: Logging in as a different account hides my stocks.

---

## Phase 4: Returns & Allocation (D18–D22)
Goal: Crunch the numbers. Learned material + calculation logic, almost no new concepts.

- D18: Calculate position value (current price × quantity)
- D19: Calculate return (current price vs average cost)
- D20: Calculate allocation (each position ÷ total)
- D21: Build a total-portfolio summary view
- D22: Review + number formatting (decimals, thousands separators)

Pass: Total value, per-stock return, and allocation are calculated correctly and easy to read.

---

## Phase 5: Speed / Optimization (D23–D27)
Goal: Build the depth to answer "why did you design it this way?" — the interview core.

- D23: `[PROBLEM]` Calling the API every time → slow + hits rate limits. Why caching is needed
- D24: `[NEW]` Simple time-based caching — store the last-fetched timestamp
- D25: Apply caching — reuse stored value within N minutes, refetch after
- D26: `[NEW]` DB indexing — why lookups stay fast as data grows
- D27: Review + practice explaining "why caching/indexing" out loud (interview prep)

Pass: Can explain "why did you add caching?" smoothly for a full minute.

---

## Phase 6: Automation + Deploy (D28–D33)
Goal: Scale appeal + actually ship it. The graduation zone.

- D28: `[NEW]` What is a scheduler? Periodic automatic execution
- D29: Auto-refresh prices (periodic background update)
- D30: Target-price alert logic (flag when a condition is hit)
- D31: `[NEW]` Deploy prep — requirements.txt, config cleanup
- D32: Deploy to free hosting (Render, etc.) → get a real URL
- D33: Write README (English, GitHub) + prepare 3 interview stories

Graduation: A live deployed URL exists, and the README states what/why/how in English.

---

## Commit Naming
`Portfolio_D1_Setup`, `Portfolio_D3_AddStock` — Day number + content.
Keep the streak. Commit every session.

## What I'll Have at the End
- One deployed backend project built 100% by me
- Interview keywords: CRUD, external API integration, auth, caching, DB indexing, scheduler, deployment
- Depth to answer every "why did you do it this way?"

Let's go.
