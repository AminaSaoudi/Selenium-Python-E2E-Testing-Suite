# Selenium-Python-E2E-Testing-Suite
End-to-End UI test automation for a live e-commerce site – 100% open source, CI-ready, Allure reports, and Dockerized.

This project was built from scratch to demonstrate a professional, scalable, and maintainable test automation framework using industry-best-practices.

🎯 Target Site
URL: https://www.saucedemo.com/

✨ Key Features
Page Object Model (POM): Fully implemented for clean, maintainable, and reusable test code.

Pytest Framework: Leverages pytest for test running, fixtures, and assertions.

Allure Reports: Generates beautiful, interactive, and shareable HTML reports with step-by-step logging.

Dockerized: The entire suite is containerized with docker-compose. It runs a standalone Selenium Grid headlessly, making it CI/CD ready.

Robust Waiting: Uses Docker healthchecks to ensure tests only run when the Selenium Grid is 100% ready, eliminating flaky "wait" scripts.

Data-Driven: All test data (users, passwords, errors) is stored externally in data/test_data.json.

Configuration Management: Environment details (like the base_url) are stored in pytest.ini, not hardcoded.

🚀 How to Run
1. The Docker / CI-Ready Way (Recommended)
This is the simplest and most reliable way to run the entire suite. It runs headlessly and exactly as it would in a CI/CD pipeline.

Prerequisites:

[suspicious link removed] installed and running.

Run the Suite:

Bash

# 1. Clone the repository
git clone [https://github.com/YOUR_USERNAME/Selenium-Python-E2E-Testing-Suite.git](https://github.com/YOUR_USERNAME/Selenium-Python-E2E-Testing-Suite.git)
cd Selenium-Python-E2E-Testing-Suite
2. Build and run the containers
This command will:
- Build the 'python-tests' image
- Start the 'selenium' container
- Wait for Selenium to be healthy
- Run pytest, then stop everything.
docker-compose up --build --abort-on-container-exit


### 2\. The Local / Development Way
Use this method if you want to run tests locally for development or debugging.

Prerequisites:

Python 3.10+

Google Chrome

Allure (for viewing reports)

Run the Suite:

Bash

# 1. Clone the repository
git clone [https://github.com/YOUR_USERNAME/Selenium-Python-E2E-Testing-Suite.git](https://github.com/YOUR_USERNAME/Selenium-Python-E2E-Testing-Suite.git)
cd Selenium-Python-E2E-Testing-Suite
2. Create and activate a virtual environment
python -m venv venv source venv/bin/activate # (or .\venv\Scripts\activate on Windows)

3. Install dependencies
pip install -r requirements.txt

4. Run pytest
(This will run locally using webdriver-manager)
pytest


-----
📊 Viewing the Allure Report
After running the tests (with either method), your test results are in the allure-results folder.

Make sure you have Allure installed (scoop install allure or brew install allure).

Serve the report:

```bash
allure serve allure-results
```
Your browser will automatically open with a beautiful, interactive dashboard.

```
```