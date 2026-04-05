AI Real Estate Automation System

End-to-end AI workflow that automates property analysis, lead scoring, and listing generation.

Built to simulate a real-world system that reduces manual work and scales real estate operations.

Key Results
Reduced manual listing creation time by approximately 80%
Improved speed in identifying investment opportunities
Automated end-to-end real estate workflows
Standardized listing quality using AI
What This System Does
Input
Property data (CSV or structured dataset)
Processing
Price analysis and opportunity detection
AI-generated property descriptions (ChatGPT)
Lead scoring logic
Output
Ready-to-publish property listings
Automated messages via Telegram and Email
Architecture
Real-Estate-Bot/
│
├── Data/                # Property dataset
├── SRC/
│   ├── lector.py        # Data ingestion
│   ├── ai_brain.py      # AI processing
│   ├── mensajero.py     # Messaging system
│   ├── logger.py        # Logging
│   └── main.py          # Orchestrator
Tech Stack
Python
OpenAI / ChatGPT
Telegram API
Email Automation (SMTP)
CSV Data Processing
Demo

Include in this section:

Screenshot of input data (CSV)
Screenshot of generated listing
Screenshot of Telegram message

Without this section, the project loses significant impact for recruiters.

Example Output
Exceptional Investment Opportunity

This property offers strong potential with competitive pricing and strategic location...
How to Run
git clone https://github.com/juliomarianocampuzano-git/Real-Estate-Bot
cd Real-Estate-Bot
pip install -r requirements.txt
python SRC/main.py
Environment Variables

Create a .env file with the following variables:

OPENAI_API_KEY=your_key
TELEGRAM_TOKEN=your_token
EMAIL_USER=your_email
EMAIL_PASS=your_password
Why This Project Matters

This project demonstrates the ability to:

Build real-world AI automation systems
Integrate multiple services (AI, messaging, and data processing)
Design scalable workflows for business use
Move beyond analysis into execution
Future Improvements
Web dashboard (Streamlit)
Database integration (PostgreSQL)
Task scheduling (cron or Airflow)
CRM integration
