# RazorGrowth — Agentic Merchant Growth Engine

> **From "What happened?" to "What should the merchant do next?"**

RazorGrowth is an agentic merchant growth engine that analyzes transaction data, identifies revenue opportunities, selects the strongest next-best action, validates it through business guardrails, and—only after explicit merchant approval—can execute the recommended payment action.

The project demonstrates a controlled agentic workflow for merchant growth:

```text
Merchant Data
     ↓
Merchant Analysis
     ↓
Growth Opportunity Detection
     ↓
Opportunity Ranking
     ↓
Agentic Decision
     ↓
Guardrail Validation
     ↓
Merchant Approval
     ↓
Action Execution
```

## 🚀 Live Demo

- **Live API:** https://razorgrowth-agent.onrender.com
- **Interactive API Documentation:** https://razorgrowth-agent.onrender.com/docs
- **GitHub Repository:** https://github.com/ms1706g/razorgrowth-agent

The deployed application exposes merchant analytics, opportunity detection, agentic recommendation, guardrail validation, and action execution through FastAPI.

## 🎯 Problem Statement

Merchant dashboards are good at explaining historical performance:

- How much revenue was generated?
- How many orders were received?
- Which products performed best?
- How many customers purchased?

But these metrics do not directly answer the more valuable business questions:

- What is the biggest growth opportunity?
- Which product should the merchant promote?
- Which customers are eligible?
- Why is this opportunity valuable?
- What should the merchant do next?
- Can that action be executed safely?

RazorGrowth is designed to bridge this gap by moving from:

```text
Analytics
   ↓
Insights
   ↓
Decision
   ↓
Action
```

Instead of stopping at reporting, the system produces a structured next-best-action recommendation.

## 💡 Solution

RazorGrowth analyzes merchant transaction history and converts it into an actionable growth recommendation.

The current implementation focuses on cross-sell opportunities among existing customers.

The system:

1. Analyzes merchant performance.
2. Evaluates product-level revenue.
3. Identifies potential cross-sell opportunities.
4. Determines eligible customers.
5. Estimates revenue potential.
6. Compares multiple opportunities.
7. Selects the strongest opportunity.
8. Explains why the opportunity was selected.
9. Applies business guardrails.
10. Requires explicit merchant approval.
11. Executes the approved payment-link action.

This creates a controlled agentic workflow rather than an unrestricted autonomous system.

## 🧠 Core Idea

The central design principle is:

> The agent should recommend the best action, but it should not blindly execute it.

For example, the system can discover:

```text
Pro Analytics
      │
      ├── Growth Toolkit
      │      ├── 5 eligible customers
      │      └── ₹7,495 estimated revenue
      │
      ├── Annual Pro Upgrade
      │      ├── 6 eligible customers
      │      └── ₹14,994 estimated revenue
      │
      └── Premium Support
             ├── 6 eligible customers
             └── ₹4,794 estimated revenue
```

The agent then selects:

```text
Annual Pro Upgrade
₹14,994 estimated revenue potential
```

because it has the highest estimated revenue potential among the discovered opportunities.

## 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │    SQLite Database    │
                         │ Merchant Transactions │
                         └──────────┬────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Merchant Analysis     │
                         │                       │
                         │ • Revenue             │
                         │ • Orders              │
                         │ • Customers           │
                         │ • Product Performance │
                         └──────────┬────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Opportunity Engine    │
                         │                       │
                         │ • Cross-sell          │
                         │ • Eligible Customers  │
                         │ • Revenue Potential   │
                         └──────────┬────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Opportunity Ranking   │
                         │                       │
                         │ Select highest-value  │
                         │ growth opportunity    │
                         └──────────┬────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ RazorGrowth Agent     │
                         │                       │
                         │ Decision + Reasoning  │
                         └──────────┬────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Guardrails         │
                         │                       │
                         │ Recommendation        │
                         │ Validation            │
                         └──────────┬────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Merchant Approval     │
                         │                       │
                         │ Explicit consent      │
                         └──────────┬────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Action Execution      │
                         │                       │
                         │ Create Payment Link   │
                         └───────────────────────┘
```

## 🔄 Agentic Workflow

### 1. Analyze Merchant

The merchant analysis layer calculates:

- Total revenue
- Total orders
- Total customers
- Customers with orders
- Product-level order volume
- Product-level revenue

Example:

```json
{
  "total_revenue": 21383,
  "total_orders": 17,
  "total_customers": 10,
  "customers_with_orders": 10
}
```

### 2. Discover Growth Opportunities

The opportunity engine evaluates products against the merchant's existing customer purchase history.

For each candidate product, the system determines:

- Anchor product
- Target product
- Eligible customers
- Customer count
- Target product price
- Estimated revenue potential
- Recommended action

Example:

```json
{
  "opportunity_type": "cross_sell",
  "anchor_product": "Pro Analytics",
  "target_product": "Annual Pro Upgrade",
  "target_product_price": 2499.0,
  "eligible_customer_count": 6,
  "eligible_customer_ids": [1, 2, 4, 5, 8, 10],
  "revenue_potential": 14994.0,
  "recommended_action": "create_payment_link"
}
```

### 3. Compare Opportunities

The agent does not simply take the first opportunity returned by the database. It evaluates the available opportunities and ranks them by estimated revenue potential.

Current demonstration:

| Rank | Opportunity | Revenue Potential |
|------|-------------|--------------------|
| 1 | Annual Pro Upgrade | ₹14,994 |
| 2 | Growth Toolkit | ₹7,495 |
| 3 | Premium Support | ₹4,794 |

The highest-value opportunity is selected.

### 4. Agentic Decision

The agent converts the opportunity analysis into a structured recommendation.

Example:

```json
{
  "opportunity_type": "cross_sell",
  "anchor_product": "Pro Analytics",
  "target_product": "Annual Pro Upgrade",
  "target_product_price": 2499.0,
  "eligible_customer_count": 6,
  "revenue_potential": 14994.0,
  "why_this_opportunity": "Selected because it has the highest estimated revenue potential among the discovered opportunities.",
  "recommended_action": "create_payment_link",
  "guardrail_required": true
}
```

The recommendation contains both the decision and the reasoning behind it.

## 🛡️ Guardrails

A core design principle of RazorGrowth is controlled execution.

The system does not allow an agent recommendation to directly trigger a merchant-facing action without validation.

The workflow is:

```text
Agent Recommendation
        ↓
Guardrail Validation
        ↓
Merchant Approval
        ↓
Action Execution
```

The guardrail layer validates whether the opportunity satisfies the defined business rules.

Example:

```json
{
  "valid": true,
  "reason": "Opportunity passed all guardrail checks."
}
```

If the opportunity fails validation, execution is blocked.

## ✋ Merchant Approval

RazorGrowth intentionally separates recommendation from execution.

Calling the execution endpoint without approval returns:

```json
{
  "success": false,
  "status": "approval_required",
  "message": "Merchant approval is required before executing the recommended action."
}
```

Only an explicitly approved action can proceed.

This creates a safer human-in-the-loop architecture:

```text
Detect
  ↓
Recommend
  ↓
Validate
  ↓
Ask Merchant
  ↓
Approve
  ↓
Execute
```

This approach provides a safer foundation for future autonomous merchant workflows.

## 💳 Action Execution

After approval and successful guardrail validation, RazorGrowth can execute the recommended payment-link action.

The demonstrated workflow creates a payment link for the selected target product.

Example result:

```json
{
  "success": true,
  "status": "executed",
  "action": "create_payment_link",
  "amount": 2499.0,
  "currency": "INR"
}
```

The execution response also includes:

- Agent result
- Selected opportunity
- Guardrail result
- Payment-link result

## 🤖 LLM / Safe Fallback Architecture

The agentic layer is designed to remain operational even when an external LLM is unavailable.

When the LLM is unavailable because of API quota or credits, RazorGrowth switches to a deterministic safe fallback.

Example:

```json
{
  "agent": "RazorGrowth",
  "mode": "safe_fallback",
  "status": "success",
  "reason": "LLM unavailable: API quota or credits exhausted."
}
```

The fallback still:

- Discovers opportunities.
- Compares revenue potential.
- Selects the highest-value opportunity.
- Produces a structured recommendation.
- Requires guardrail validation.
- Requires merchant approval before execution.

This means the core merchant-growth decision pipeline does not depend entirely on LLM availability.

## 🧰 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core application logic |
| FastAPI | REST API layer |
| SQLite | Demonstration transaction database |
| Uvicorn | ASGI application server |
| Pytest | Automated testing |
| REST APIs | System integration |
| Agentic Workflow | Opportunity selection and next-best-action |
| Guardrails | Controlled recommendation and execution |

## 📁 Project Structure

```text
razorgrowth-agent/
│
├── app/
│   ├── __init__.py
│   ├── actions.py
│   ├── agent.py
│   ├── agentic_agent.py
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
├── README.md
└── requirements.txt
```

`.env` is intentionally excluded from the documented repository structure because it contains local secrets/configuration and should remain ignored by Git.

## 🚀 Getting Started

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

Create a local `.env` file:

```env
RAZORPAY_KEY_ID=your_test_key_id
RAZORPAY_KEY_SECRET=your_test_key_secret
```

**Security:** Never commit real credentials, secrets, or production API keys.

The `.env` file should remain excluded through `.gitignore`.

### 4. Initialize Demo Data

Run:

```bash
python -m app.seed
```

This initializes the SQLite database and loads the demonstration merchant dataset.

### 5. Run Tests

Run the automated test suite:

```bash
python -m pytest -v
```

Current verification:

```text
5 passed
```

### 6. Start the API

Run:

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive documentation:

```text
http://127.0.0.1:8000/docs
```

## 📡 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/merchant/analyze` | Analyze merchant performance |
| GET | `/merchant/opportunity` | Return strongest growth opportunity |
| POST | `/agent/analyze` | Run the standard growth agent |
| POST | `/agent/agentic-analyze` | Run the agentic growth workflow |
| POST | `/action/payment-link` | Create payment link after approval |
| POST | `/agent/execute` | Validate and execute the agent recommendation |

## 🧪 API Demo Flow

A complete local demonstration can be performed through:

```text
1. Start FastAPI
        ↓
2. Open /docs
        ↓
3. Run /health
        ↓
4. Run /merchant/analyze
        ↓
5. Run /merchant/opportunity
        ↓
6. Run /agent/agentic-analyze
        ↓
7. Inspect selected opportunity
        ↓
8. Run /agent/execute
        ↓
9. Observe approval_required
        ↓
10. Approve the action
        ↓
11. Execute payment-link action
```

This demonstrates the full journey:

```text
Transaction Data
      ↓
Merchant Intelligence
      ↓
Opportunity Detection
      ↓
Opportunity Ranking
      ↓
Agentic Decision
      ↓
Guardrail Validation
      ↓
Merchant Approval
      ↓
Payment Action
```

## 📊 Demo Dataset

The project contains a controlled demonstration merchant dataset.

The dataset includes:

- 10 customers
- 17 orders
- Multiple products
- Different customer purchasing patterns
- Product-level revenue
- Cross-sell opportunities

The controlled dataset makes it possible to demonstrate the complete decision pipeline without requiring production merchant data.

## 🔎 Example Opportunity Analysis

The current dataset produces opportunities such as:

| Opportunity | Eligible Customers | Product Price | Estimated Revenue |
|-------------|--------------------|----------------|--------------------|
| Growth Toolkit | 5 | ₹1,499 | ₹7,495 |
| Annual Pro Upgrade | 6 | ₹2,499 | ₹14,994 |
| Premium Support | 6 | ₹799 | ₹4,794 |

The agent selects **Annual Pro Upgrade** because it has the highest estimated revenue potential.

## 🔐 Security Considerations

Credentials and sensitive configuration should always be stored outside source code.

Never commit:

```text
.env
```

or any file containing real API credentials.

For production deployment, the system should additionally implement:

- Secure secret management
- Authentication
- Authorization
- Rate limiting
- Production-grade database infrastructure
- Structured logging
- Monitoring
- Observability
- Audit trails
- Action-level authorization
- Idempotency controls
- Customer communication consent management

## 🧩 Design Principles

### 1. Decision Over Dashboard

RazorGrowth is designed to answer:

> What should happen next?

rather than only:

> What happened?

### 2. Evidence-Based Recommendations

Recommendations are generated from:

- Transaction history
- Product performance
- Customer purchase relationships
- Estimated revenue potential

### 3. Human-in-the-Loop Execution

The system separates **Recommendation** from **Execution**.

Merchant approval is required before executing the recommended action.

### 4. Guardrail-First Execution

Actions must pass validation before execution.

```text
Recommendation
      ↓
Guardrails
      ↓
Approval
      ↓
Execution
```

### 5. Graceful Degradation

The system can fall back to deterministic opportunity selection when the LLM is unavailable.

This prevents the core merchant-growth workflow from becoming completely dependent on external model availability.

## 🗺️ Roadmap

### Advanced Customer Segmentation

Introduce richer customer-level signals:

- Recency
- Frequency
- Monetary value
- Product affinity
- Purchase history
- Customer lifetime value

### Multiple Growth Strategies

Expand beyond cross-selling into:

- Upselling
- Win-back campaigns
- Repeat-purchase campaigns
- High-value customer retention
- Product bundling
- Personalized offers

### LLM-Powered Business Reasoning

Enhance the agent with deeper reasoning around:

- Why an opportunity was selected
- Why a customer segment was targeted
- Why a specific product is recommended
- What assumptions influenced the decision
- Alternative opportunities considered

### Campaign Execution

Extend the action layer beyond payment links:

```text
Opportunity
    ↓
Recommendation
    ↓
Merchant Approval
    ↓
Campaign Generation
    ↓
Customer Communication
    ↓
Conversion Tracking
```

### Closed-Loop Optimization

The long-term workflow can evolve toward:

```text
Detect Opportunity
        ↓
Generate Recommendation
        ↓
Validate Guardrails
        ↓
Merchant Approval
        ↓
Execute Action
        ↓
Track Conversion
        ↓
Measure Revenue Impact
        ↓
Learn From Results
        ↓
Detect Next Opportunity
```

This would allow RazorGrowth to continuously optimize merchant growth strategies based on observed outcomes.

## 🏆 Hackathon Submission

**Project:** RazorGrowth — Agentic Merchant Growth Engine

**Category:** Agentic AI / Merchant Growth

**Core Idea:**

Transform merchant transaction data into actionable, controlled, agent-driven growth decisions.

### Demonstrated Capabilities

- Merchant transaction analysis
- Revenue analytics
- Order analytics
- Customer analysis
- Product performance analysis
- Cross-sell opportunity detection
- Eligible customer detection
- Revenue-potential estimation
- Multi-opportunity comparison
- Highest-value opportunity selection
- Agentic recommendation
- Safe fallback behavior
- Guardrail validation
- Human-in-the-loop approval
- Payment-link action execution
- FastAPI REST API
- Interactive Swagger documentation
- Automated testing
- Production deployment

## ✅ Current Verification

The core project has been locally verified with:

```text
5 passed
```

The API application has also been verified to:

- ✓ Import successfully
- ✓ Start successfully with Uvicorn
- ✓ Serve `/`
- ✓ Serve `/health`
- ✓ Serve `/docs`
- ✓ Generate OpenAPI documentation
- ✓ Analyze merchant data
- ✓ Detect growth opportunities
- ✓ Rank opportunities
- ✓ Generate agentic recommendations
- ✓ Apply guardrails
- ✓ Require merchant approval
- ✓ Execute the approved payment-link action

## 🔭 Vision

The long-term vision of RazorGrowth is to evolve from a merchant analytics and recommendation engine into an intelligent merchant growth copilot.

Instead of requiring merchants to manually interpret dashboards, RazorGrowth should continuously help answer:

- What is the biggest growth opportunity right now?
- Who should be targeted?
- Why is this opportunity valuable?
- What should happen next?
- Can the action be executed safely?

The ultimate goal is a controlled closed-loop growth system:

```text
Merchant Data
      ↓
Understand
      ↓
Discover
      ↓
Prioritize
      ↓
Recommend
      ↓
Validate
      ↓
Approve
      ↓
Execute
      ↓
Measure
      ↓
Learn
      ↓
Discover the Next Opportunity
```

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
Opportunity Ranking
      ↓
Agentic Recommendation
      ↓
Guardrails
      ↓
Merchant Approval
      ↓
Next Best Action
```

The next stage is to connect these recommendations to real-world execution and measurable outcomes, creating a merchant growth engine that can continuously detect, recommend, execute, and learn.

<p align="center">
  <strong>🚀 RazorGrowth</strong><br>
  <em>Turning merchant data into the next best action.</em>
</p>
