# AI Security Lab – OWASP LLM & Agentic AI Vulnerability Simulator

## Project Overview
AI Security Lab is a Python-based security testing application built using Streamlit. It demonstrates common security vulnerabilities in Large Language Models (LLMs) and Agentic AI systems using simulated NGO data.

The project provides two modes:
- **Vulnerable Mode:** Demonstrates selected security risks in an intentionally vulnerable environment.
- **Protected Mode:** Applies security controls to reduce the impact of selected attacks.

## Features
- Claude and Gemini model integration
- Interactive Streamlit interface
- Vulnerable and Protected testing modes
- Prompt injection detection
- Synthetic sensitive-information redaction
- Simulated agent tools and actions
- Local audit logging
- Automated attack test cases
- CSV-based test result reporting
- Safe simulation using fake NGO data

## Security Risks Covered

### OWASP LLM Top 10
- LLM01 – Prompt Injection
- LLM02 – Sensitive Information Disclosure
- LLM03 – Excessive Agency
- LLM08 – Hidden Context Exposure
- LLM10 – Improper Output Handling

### OWASP Agentic AI Security Risks
- ASI01 – Agent Goal Hijack
- ASI02 – Tool Misuse
- ASI03 – Identity & Privilege Abuse
- ASI05 – Unexpected Code Execution
- ASI06 – Memory & Context Poisoning

## Technology Stack
- Python
- Streamlit
- Claude API
- Gemini API
- Regular Expressions
- CSV
- JSON
- Git and GitHub

## Project Structure
```text
ai-security-poc/
├── app/
│   ├── app.py
│   ├── models.py
│   ├── agent.py
│   └── security.py
├── data/
│   ├── knowledge.txt
│   └── private.txt
├── tests/
│   ├── attack_cases.py
│   ├── run_tests.py
│   └── reevaluate_results.py
├── results/
│   ├── results.csv
│   ├── results_raw.csv
│   ├── audit.log
│   └── outbox.json
├── .env.example
├── .gitignore
├── Dockerfile
└── README.md
```

## Running the Project

1. Install Python 3.10 or later.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure API credentials in your local `.env` file.
4. Start the application:
   ```bash
   streamlit run app/app.py
   ```

## Testing
Run the automated security test suite:

```bash
python tests/run_tests.py
```

Test results are stored in `results/results.csv`.

## Safety Disclaimer
This project is intended for educational and defensive AI security research. It uses synthetic NGO data and simulated agent actions. No real confidential information or external actions are intended.

## Author
AI Security Internship Project