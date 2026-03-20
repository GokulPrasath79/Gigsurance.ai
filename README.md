# 🛡️ Gigsurance.ai — AI-Powered Parametric Income Insurance for E-commerce Delivery Partners

> *"Every shift. Every rupee. Insured."*

> **Guidewire DEVTrails 2026** | University Hackathon Submission — Phase 1

---

## 📌 Problem Statement

India's e-commerce delivery partners (Amazon, Flipkart, Meesho, etc.) are essential to the digital economy but are completely exposed to income loss caused by external disruptions beyond their control — extreme weather, toxic air quality, local curfews, or platform outages. When these events occur, workers lose 20–30% of monthly earnings with zero safety net.

**Gigsurance.ai** is an AI-enabled parametric insurance platform that automatically detects these disruptions and pays out lost income directly to workers — no claim forms, no delays, no friction.

> ⚠️ **Coverage Scope**: GigShield covers INCOME LOSS ONLY. Health, life, accident, and vehicle repair claims are strictly excluded.

---

## 👤 Primary Persona

**E-commerce Delivery Partner** (Amazon / Flipkart)

| Attribute | Detail |
|---|---|
| Platform | Amazon Flex / Flipkart Ekart |
| Earning Cycle | Weekly payouts (₹4,000–₹9,000/week) |
| Working Hours | 8–12 hrs/day, 6 days/week |
| Primary Risks | Heavy rain, poor AQI, curfews, platform outages |
| Geography | Tier-1 & Tier-2 cities (Mumbai, Delhi, Bengaluru, Chennai, Hyderabad) |

### Persona Scenario

**Rajan**, 29, delivers for Amazon Flex in Chennai. He averages ₹700/day, 6 days a week. During the Northeast Monsoon season, heavy flooding causes him to lose 3–4 working days per week for several weeks. With GigShield, a real-time rainfall sensor trigger fires automatically when the IMD threshold is crossed in his zone, a claim is instantly approved, and ₹2,100 (3 days × ₹700) is transferred to his UPI within minutes — no action needed from Rajan.

**Future Scope**: Extending the same platform to Food Delivery (Zomato/Swiggy) and Grocery/Q-Commerce (Zepto/Blinkit) personas with tailored risk models and triggers.

---

## ⚡ Parametric Triggers

Gigsurance.ai uses objective, verifiable data signals — not worker self-reporting — to trigger claims automatically.

| # | Trigger | Data Source | Threshold | Income Loss Basis |
|---|---|---|---|---|
| 1 | **Extreme Weather** (Rain/Flood/Heat) | IMD API / OpenWeatherMap | Rainfall > 64.5mm/day OR Temp > 42°C | Deliveries halted in affected zone |
| 2 | **Severe Air Pollution (AQI)** | CPCB AQI API / IQAir | AQI > 300 (Hazardous) for 4+ hours | Outdoor work unsafe, platform reduces orders |
| 3 | **Curfew / Local Strike** | News API + Govt alerts | Section 144 declared or verified bandh | Zone inaccessible for pickup/drop |
| 4 | **Platform App Outage** | Synthetic monitoring / StatusPage API | Downtime > 45 minutes during peak hours | Worker logged in but unable to receive orders |

> All triggers are **parametric** — payout is based on the event threshold being met, not on individual claim verification.

---

## 💰 Weekly Premium Model

Premiums are calculated and charged **weekly**, aligned to how gig workers earn.

### Base Premium Structure

| Coverage Tier | Weekly Premium | Max Weekly Payout | Coverage Days |
|---|---|---|---|
| Basic | ₹29/week | ₹1,500 | Up to 2 disrupted days |
| Standard | ₹49/week | ₹3,000 | Up to 4 disrupted days |
| Pro | ₹79/week | ₹5,000 | Up to 6 disrupted days |

### AI-Driven Dynamic Pricing

The weekly premium is adjusted in real-time using a **Risk Score** (0–100) computed by our ML model:

```
Weekly Premium = Base Premium × Risk Multiplier

Risk Multiplier inputs:
  - Zone flood/waterlogging history (past 3 years)
  - Seasonal weather forecast (IMD 7-day)
  - Worker's average daily earnings (to size payout correctly)
  - Historical claim frequency in the worker's pin code
  - Platform outage frequency for their delivery app
```

**Example**: A worker in a Chennai zone with high flood risk during October–December gets a dynamically higher premium (e.g., ₹65 instead of ₹49 for Standard), while a worker in a historically dry Bengaluru zone gets a discount (e.g., ₹41).

---

## 🔄 Application Workflow

```
┌─────────────────────────────────────────────────────────┐
│                     WORKER ONBOARDING                    │
│  Sign up → Verify ID (Aadhaar/PAN) → Link UPI/Bank      │
│  → Select delivery platform → Choose coverage tier       │
│  → AI calculates personalised weekly premium             │
└───────────────────────┬─────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────┐
│                  WEEKLY POLICY ACTIVATION                │
│  Auto-debit weekly premium → Policy active for 7 days    │
│  → Worker receives coverage confirmation on app          │
└───────────────────────┬─────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────┐
│               REAL-TIME DISRUPTION MONITORING            │
│  Continuous polling of Weather / AQI / News / Platform   │
│  APIs → Trigger engine evaluates thresholds per zone     │
└───────────────────────┬─────────────────────────────────┘
                        │  [Threshold breached]
┌───────────────────────▼─────────────────────────────────┐
│               AUTO CLAIM INITIATION                      │
│  System identifies all insured workers in affected zone  │
│  → Fraud engine validates (GPS, login status, activity)  │
│  → Claim auto-approved or flagged for review             │
└───────────────────────┬─────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────┐
│                  INSTANT PAYOUT                          │
│  Payout calculated (hours lost × daily earnings rate)    │
│  → Transferred via UPI / bank within minutes             │
│  → Worker notified on app with breakdown                 │
└─────────────────────────────────────────────────────────┘
```

---

## 🤖 AI/ML Integration Plan

### 1. Dynamic Premium Calculation
- **Model**: Gradient Boosted Trees (XGBoost / LightGBM)
- **Features**: Zone risk score, seasonality index, worker earnings history, platform reliability score, city-level disruption frequency
- **Output**: Weekly premium multiplier (0.7x – 1.8x of base)
- **Training Data**: IMD historical weather, CPCB AQI archives, mock claim history

### 2. Predictive Risk Modeling
- **Model**: Time-series forecasting (Prophet / LSTM)
- **Purpose**: Predict likelihood of a disruption trigger in the next 7 days per zone
- **Use**: Shown to workers as a "Risk Forecast" widget; used by insurer for reserve planning

### 3. Intelligent Fraud Detection
- **Anomaly Detection**: Isolation Forest on claim patterns
- **Location Validation**: Cross-check worker's GPS at time of disruption vs. claimed zone
- **Activity Validation**: Check if worker was logged into delivery platform during disruption window
- **Duplicate Prevention**: Fingerprinting on device ID + UPI + Aadhaar hash
- **Social Graph Check**: Flag clusters of simultaneous claims from the same area (collusion detection)

### 4. NLP for Social/Curfew Triggers
- **Model**: Fine-tuned BERT classifier on Indian news headlines
- **Purpose**: Detect curfew/bandh declarations from news feeds and government alerts
- **Output**: Zone-level disruption flag with confidence score

---

## 🖥️ Platform Choice: Web + Mobile

We are building **both** a web dashboard and a mobile-first PWA (Progressive Web App):

| Platform | Primary Users | Key Screens |
|---|---|---|
| **Mobile PWA** | Delivery workers | Onboarding, Policy status, Payout history, Risk forecast |
| **Web Dashboard** | Insurers / Admins | Analytics, Claim management, Fraud alerts, Loss ratios |

**Justification**: Delivery workers primarily use smartphones; a PWA avoids app store friction while still providing a native-like experience. Insurers need a full desktop dashboard for analytics and operations.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend (Web)** | React + Next.js, TailwindCSS |
| **Mobile** | React Native (PWA-first, native later) |
| **Backend API** | Python + FastAPI |
| **ML Models** | scikit-learn, XGBoost, Prophet |
| **Database** | PostgreSQL (core data), Redis (trigger cache) |
| **Auth** | JWT + Aadhaar OTP (mocked for hackathon) |
| **Weather API** | OpenWeatherMap (free tier) / IMD mock |
| **AQI API** | CPCB / IQAir free tier |
| **News/Curfew** | NewsAPI + custom NLP classifier |
| **Payments** | Razorpay test mode / UPI simulator |
| **Hosting** | Vercel (frontend) + Railway / Render (backend) |

---

## 📅 Development Plan

### Phase 1 (March 4–20) — ✅ Ideation & Foundation
- [x] Problem scoping and persona definition
- [x] Parametric trigger design
- [x] Weekly premium model design
- [x] AI/ML architecture plan
- [x] Tech stack selection
- [x] Repository setup and README

### Phase 2 (March 21 – April 4) — Automation & Protection
- [ ] Worker registration and onboarding flow
- [ ] Insurance policy creation with weekly premium calculation
- [ ] 4 automated trigger integrations (Weather, AQI, Curfew, Outage)
- [ ] Zero-touch claim initiation pipeline
- [ ] Basic fraud detection (location + activity validation)
- [ ] Payout simulation (Razorpay test mode)

### Phase 3 (April 5–17) — Scale & Optimise
- [ ] Advanced fraud detection (GPS spoofing, anomaly detection)
- [ ] Worker dashboard (earnings protected, active coverage)
- [ ] Admin/Insurer dashboard (loss ratios, predictive analytics)
- [ ] Final demo video (simulated disruption → auto claim → payout)
- [ ] Pitch deck preparation

---

## 📁 Repository Structure (Planned)

```
gigsurance-ai/
├── frontend/          # Next.js web app
├── mobile/            # React Native PWA
├── backend/           # FastAPI backend
│   ├── api/           # REST endpoints
│   ├── ml/            # ML models and training scripts
│   ├── triggers/      # Parametric trigger engine
│   └── fraud/         # Fraud detection module
├── data/              # Mock datasets for ML training
├── docs/              # Architecture diagrams
└── README.md
```

---

## 👥 Team Codegenz
 GOKUL PRASATH VENKATESH


LAASYA REDDY NAGATHAM


KUSHAAGRA KULSHRESHTHA


PAVITHRA S

---

## 📜 License

MIT License

---

*Gigsurance.ai — Built for Guidewire DEVTrails 2026 — protecting the backbone of India's digital economy.*
