# RazorGrowth — Agentic Merchant Growth Engine

> **From "What happened?" to "What should the merchant do next?"**

RazorGrowth is an agentic AI-powered merchant growth engine that analyzes transaction data, identifies actionable growth opportunities, and recommends the next best action to help merchants increase revenue.

Unlike traditional analytics dashboards that primarily explain historical performance, RazorGrowth is designed to transform merchant data into **actionable growth decisions**.

---

## 🚀 Live Demo

**Live API:** https://razorgrowth-agent.onrender.com

**Interactive API Docs:** https://razorgrowth-agent.onrender.com/docs

**GitHub:** https://github.com/ms1706g/razorgrowth-agent

> The deployed API has been verified end-to-end, including merchant analysis, growth opportunity detection, and the RazorGrowth agent workflow.

---

## Overview

Merchants generate significant amounts of transaction data, but raw analytics alone do not answer the most important business question:

> **What should I do next to grow my business?**

RazorGrowth addresses this gap by combining merchant analytics, customer behavior analysis, product performance analysis, opportunity detection, business guardrails, and an agentic recommendation workflow.

The current implementation focuses on identifying **cross-sell opportunities among existing customers** and translating those opportunities into a concrete recommended action.

### Core Workflow

```text
Merchant Transaction Data
          │
          ▼
   Merchant Analysis
          │
          ▼
Customer & Product Insights
          │
          ▼
Growth Opportunity Detection
          │
          ▼
   Guardrail Validation
          │
          ▼
 Recommended Next Action
          │
          ▼
    Agent Response
```

---

## Problem Statement

Traditional merchant dashboards primarily answer questions such as:

- How much revenue did I generate?
- How many orders did I receive?
- Which products performed best?
- How many customers do I have?

While these metrics are useful, merchants also need answers to higher-value questions:

- Which customers should I target?
- Which product should I promote?
- Why is this a good opportunity?
- What action should I take?
- How can I convert an insight into an executable growth action?

RazorGrowth is designed to bridge this gap by moving from **analytics to action**.

---

## Solution

RazorGrowth processes merchant transaction history and converts it into a structured growth recommendation.

The system:

1. Analyzes merchant performance.
2. Evaluates customer and product purchasing patterns.
3. Detects potential growth opportunities.
4. Identifies a relevant product and customer segment.
5. Validates the recommendation through guardrails.
6. Produces a concrete next-best-action recommendation.

### Example Recommendation

```json
{
  "opportunity_type": "cross_sell",
  "target_product": "Growth Toolkit",
  "recommended_action": "create_payment_link"
}
```

The goal is not simply to tell the merchant **what happened**, but to provide a clear indication of **what to do next**.

---

## Key Features

### 📊 Merchant Intelligence

RazorGrowth provides structured merchant-level insights, including:

- Total revenue
- Total orders
- Total customers
- Customers with orders
- Product performance
- Product-level revenue

### 🔎 Growth Opportunity Detection

The opportunity engine analyzes transaction patterns to identify potential revenue-growth opportunities without requiring the merchant to manually inspect individual metrics.

### 🛒 Cross-Sell Intelligence

The current demonstration focuses on identifying existing customers who may be suitable for a relevant product cross-sell.

### 🤖 Agentic Recommendation

The agent combines merchant analysis and opportunity detection into a unified, actionable response.

### 🛡️ Guardrails

A dedicated guardrail layer validates recommendations before they are returned as merchant-facing actions.

This provides a foundation for controlled agentic behavior and future autonomous execution.

### 🔌 API-First Architecture

Core functionality is exposed through REST APIs using FastAPI, making the system straightforward to test, integrate, and extend.

---

## Architecture

```text
                         ┌───────────────────────┐
                         │     Merchant Data     │
                         │       SQLite DB       │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │  Merchant Analysis    │
                         │                       │
                         │  • Revenue            │
                         │  • Orders             │
                         │  • Customers          │
                         │  • Products           │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │  Opportunity Engine   │
                         │                       │
                         │  • Cross-sell         │
                         │  • Target Selection   │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │      Guardrails       │
                         │                       │
                         │  Recommendation       │
                         │      Validation       │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │   RazorGrowth Agent   │
                         │                       │
                         │ Recommended Next      │
                         │       Action          │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │    Merchant Action    │
                         │                       │
                         │  Create Payment Link  │
                         └───────────────────────┘
```

---

## Agentic Workflow

RazorGrowth follows a decision-oriented workflow rather than simply returning raw analytics.

### 1. Analyze Merchant

The system calculates merchant-level metrics such as:

- Revenue
- Order volume
- Customer count
- Product performance
- Customer purchasing behavior

### 2. Identify Growth Opportunity

The opportunity engine evaluates transaction patterns and determines whether an actionable growth opportunity exists.

### 3. Determine Target

The system identifies the relevant:

- Product
- Customer segment
- Opportunity type

### 4. Recommend Action

The identified opportunity is converted into a concrete recommended action.

For example:

```json
{
  "opportunity_type": "cross_sell",
  "target_product": "Growth Toolkit",
  "recommended_action": "create_payment_link"
}
```

### 5. Apply Guardrails

Before the recommendation reaches the agent response, it passes through predefined business rules and guardrails.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| FastAPI | REST API layer |
| SQLite | Demo transaction database |
| Uvicorn | ASGI application server |
| Pytest | Automated testing |
| REST APIs | System integration |
| Agentic Workflow | Decision and recommendation layer |

---

## Project Structure

```text
razorgrowth-agent/
│
├── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── api.py
│   ├── config.py
│   ├── database.py
│   ├── guardrails.py
│   ├── main.py
│   ├── models.py
│   ├── seed.py
│   │
│   └── tools/
│       └── __init__.py
│
├── data/
│   ├── .gitkeep
│   └── razorgrowth.db
│
├── tests/
│   ├── __init__.py
│   ├── test_agent.py
│   ├── test_guardrails.py
│   └── test_tools.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Getting Started

### Prerequisites

Make sure the following are installed:

- Python 3.x
- pip
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/ms1706g/razorgrowth-agent.git
cd razorgrowth-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file with the required configuration.

Example:

```env
RAZORPAY_KEY_ID=your_test_key_id
RAZORPAY_KEY_SECRET=your_test_key_secret
```

**Security:** Never commit real API credentials, secrets, or production keys to the repository.

### 4. Initialize Demo Data

Run:

```bash
python -m app.seed
```

This initializes the SQLite database and loads the demonstration merchant dataset.

### 5. Start the API Server

Run:

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

RazorGrowth uses FastAPI's automatically generated interactive API documentation.

### Local Documentation

Once the server is running:

```text
http://127.0.0.1:8000/docs
```

### Live Documentation

```text
https://razorgrowth-agent.onrender.com/docs
```

The Swagger interface allows you to:

- Explore available endpoints
- View request and response schemas
- Execute API calls
- Inspect returned recommendations

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns API information |
| GET | `/health` | Health check |
| GET | `/merchant/analyze` | Analyzes merchant performance |
| GET | `/merchant/opportunity` | Identifies a growth opportunity |
| POST | `/agent/analyze` | Runs the RazorGrowth agent |

---

## Demo Dataset

The project includes a seeded demonstration dataset designed to showcase the growth engine without requiring a production payment environment.

The dataset contains:

- 10 customers
- 17 orders
- Multiple products
- Different customer purchasing patterns
- Different order recency values

This enables the system to demonstrate merchant analytics and opportunity detection using a controlled dataset.

---

## Example Merchant Analysis

The merchant analysis endpoint returns structured merchant-level information.

Example:

```json
{
  "total_revenue": 21383,
  "total_orders": 17,
  "total_customers": 10,
  "customers_with_orders": 10
}
```

Product-level performance can also be analyzed.

Example:

```json
{
  "name": "Pro Analytics",
  "orders": 8,
  "revenue": 7992
}
```

---

## Example Growth Opportunity

The current demonstration identifies a cross-sell opportunity.

Example:

```json
{
  "opportunity_type": "cross_sell",
  "target_product": "Growth Toolkit",
  "target_product_price": 1499,
  "recommended_action": "create_payment_link"
}
```

The system also determines the number of customers eligible for the identified opportunity.

---

## Agent Response

The `/agent/analyze` endpoint combines merchant intelligence and growth opportunity detection into a unified response.

Conceptually:

```text
RazorGrowth Agent
       │
       ├── Merchant Analysis
       │      ├── Revenue
       │      ├── Orders
       │      ├── Customers
       │      └── Product Performance
       │
       ├── Growth Opportunity
       │      ├── Opportunity Type
       │      ├── Target Product
       │      └── Eligible Customers
       │
       └── Recommended Action
              │
              └── Create Payment Link
```

This enables the system to move from raw transaction data to a specific merchant-facing recommendation.

---

## Guardrails

Agentic systems should not blindly execute every generated recommendation.

RazorGrowth therefore includes a dedicated guardrail layer between opportunity detection and action recommendation.

The guardrail architecture is intended to support:

- Recommendation validation
- Business-rule enforcement
- Controlled actions
- Safer agent behavior

This creates a foundation for gradually introducing more autonomous capabilities while maintaining appropriate control over merchant-facing actions.

---

## Testing

The project includes automated tests covering core components of the growth engine.

Run the complete test suite with:

```bash
python -m pytest -v
```

The tests validate functionality including:

- Merchant analysis
- Total order calculation
- Customer count
- Revenue calculation
- Growth opportunity detection
- Opportunity type
- Recommended action
- Eligible customer count

### Current Verification

**2 passed**

---

## Demo Flow

A complete demonstration can be performed through the following sequence:

```text
1. Start the FastAPI server
        │
        ▼
2. Open /docs
        │
        ▼
3. Run /health
        │
        ▼
4. Run /merchant/analyze
        │
        ▼
5. Run /merchant/opportunity
        │
        ▼
6. Run /agent/analyze
        │
        ▼
7. Present the generated growth recommendation
```

This demonstrates the complete journey from merchant transaction data to an actionable growth recommendation.

---

## Security Considerations

Credentials and sensitive configuration should always be stored outside the source code.

Do not commit:

```text
.env
```

or any file containing real credentials.

For a production deployment, the system should additionally implement:

- Secure secret management
- Authentication
- Authorization
- Rate limiting
- Production-grade database infrastructure
- Structured logging
- Monitoring and observability
- Audit trails for agent actions

---

## Future Roadmap

RazorGrowth can evolve from a recommendation engine into a more autonomous merchant growth platform.

### Payment Execution

Integrate with payment infrastructure to generate payment links directly after appropriate merchant approval.

### Customer Segmentation

Introduce advanced customer segmentation using signals such as:

- Recency
- Frequency
- Monetary value
- Product affinity
- Purchase history

### Multiple Growth Strategies

Expand beyond cross-selling to support:

- Upselling
- Win-back campaigns
- Repeat-purchase campaigns
- High-value customer retention
- Product bundling
- Personalized offers

### LLM-Powered Reasoning

Introduce an LLM reasoning layer capable of explaining:

- Why an opportunity was selected
- Why a particular customer segment was targeted
- Why an action is recommended
- What assumptions influenced the recommendation

LLM-powered reasoning is a future extension and is not presented as a dependency of the current core decision engine.

### Autonomous Execution

With appropriate approval mechanisms and guardrails, the workflow could evolve toward:

```text
Detect Opportunity
        │
        ▼
Generate Recommendation
        │
        ▼
Merchant Approval
        │
        ▼
Create Payment Link
        │
        ▼
Launch Campaign
        │
        ▼
Track Conversion
        │
        ▼
Learn From Results
        │
        └───────────────► Detect Next Opportunity
```

---

## Vision

The long-term vision of RazorGrowth is to evolve from a merchant analytics system into an intelligent merchant growth copilot.

Instead of requiring merchants to manually interpret dashboards, RazorGrowth should continuously help answer three critical questions:

**What is the biggest growth opportunity right now?**

**Who should be targeted?**

**What should happen next?**

The ultimate goal is to create a closed-loop growth system where merchant data continuously informs recommendations, actions, and measurable outcomes.

---

## Why RazorGrowth?

RazorGrowth is built around a simple progression:

```text
Analytics
   ↓
What happened?

Intelligence
   ↓
Why did it happen?

Agentic Decision-Making
   ↓
What should happen next?
```

RazorGrowth brings these layers together to transform merchant transaction data into actionable growth decisions.

---

## Hackathon Submission

**Project:** RazorGrowth — Agentic Merchant Growth Engine

**Category:** Agentic AI / Merchant Growth

**Core Idea:** Transform merchant transaction data into actionable, agent-driven growth recommendations.

### Demonstrated Capabilities

- Merchant transaction analysis
- Revenue and order analytics
- Customer analysis
- Product performance analysis
- Growth opportunity detection
- Cross-sell identification
- Eligible customer detection
- Guardrail integration
- Agentic recommendation
- REST API exposure
- Interactive API documentation
- Automated testing
- Production deployment

---

## Development Status

### Completed

- Merchant database
- Demo merchant dataset
- Merchant analytics
- Product analytics
- Growth opportunity engine
- Cross-sell recommendation
- Eligible customer detection
- Guardrails
- Agent layer
- FastAPI endpoints
- Swagger documentation
- Automated tests
- Project documentation
- Production deployment

### Planned

- Production payment integration
- Real payment-link execution
- LLM-powered reasoning
- Advanced customer segmentation
- Campaign execution
- Conversion tracking
- Closed-loop growth optimization

---

## Final Verification Checklist

Before submitting or sharing the repository, verify the following:

- README contains the live API URL
- README contains the interactive API documentation URL
- README contains the GitHub repository URL
- Production deployment is marked as completed
- `.env` is included in `.gitignore`
- No real API credentials are committed
- FastAPI server starts successfully
- `/health` responds successfully
- `/merchant/analyze` works
- `/merchant/opportunity` works
- `/agent/analyze` works
- Automated tests pass
- Git working tree is clean
- Latest changes are pushed to GitHub

---

## Conclusion

RazorGrowth demonstrates how merchant transaction data can be transformed from passive analytics into actionable growth intelligence.

The current implementation establishes the core foundation:

```text
Merchant Data
      ↓
Analytics
      ↓
Opportunity Detection
      ↓
Guardrails
      ↓
Agentic Recommendation
      ↓
Next Best Action
```

The next stage is to connect these recommendations to real-world execution and measurable outcomes, creating a merchant growth engine that can continuously detect, recommend, execute, and learn.

---

## 🚀 RazorGrowth

**Turning merchant data into the next best action.**
