# Selenium-Python-E2E-Testing-Suite :

[![E2E Test Suite](https://github.com/AminaSaoudi/Selenium-Python-E2E-Testing-Suite/actions/workflows/e2e-tests.yml/badge.svg)](https://github.com/AminaSaoudi/Selenium-Python-E2E-Testing-Suite/actions/workflows/e2e-tests.yml)

End-to-End UI test automation for a live e-commerce site – 100% open source, CI-ready, Allure reports, and Dockerized.

This project was built from scratch to demonstrate a professional test automation framework using industry best practices.

### Target Site :

URL: https://www.saucedemo.com/

### Key Features :
Continuous Integration (CI): Fully automated with GitHub Actions. The suite builds, runs, and tests on every push to main

Page Object Model (POM) for clean, maintainable, and reusable test code.

Pytest Framework for test running, fixtures, and assertions.

Allure Reports: Generates interactive and shareable HTML reports with step-by-step logging.

Dockerized: The entire suite is containerized with docker-compose. It runs a standalone Selenium Grid headlessly, making it CI/CD ready.

Data-Driven: All test data (users, passwords, errors) is stored externally in data/test_data.json.

Configuration Management: Environment details (like the base_url) are stored in pytest.ini, not hardcoded.

### Automated CI Pipeline (GitHub Actions)
This repository is configured with a GitHub Actions workflow (.github/workflows/e2e-tests.yml).

On every push to the main branch, the workflow will automatically:

1. Check out the latest code.
2. Build the python-tests Docker image.
3. Start the selenium and tests services using docker compose.
4. Wait for the Selenium container to be "healthy" (using our healthcheck).
5. Run the entire pytest suite inside the tests container.
6. Report a Pass (✅) or Fail (❌) based on the test results.
7. Upload the allure-results folder as an artifact for inspection.

### How to Run Using Docker

**Prerequisites:**

Docker installed and running.


**Clone the repository**
```
git clone https://github.com/AminaSaoudi/Selenium-Python-E2E-Testing-Suite.git
cd Selenium-Python-E2E-Testing-Suite
```

**Build and run the containers**

This command will:

- Build the 'python-tests' image
- Start the 'selenium' container
- Wait for Selenium to be healthy
- Run pytest, then stop everything.
```
docker-compose up --build --abort-on-container-exit
```

### How to Run on your local machine

Use this method if you want to run tests locally for development or debugging.

*Prerequisites:*

Python 3.10+

Google Chrome

Allure (for viewing reports)

**Clone the repository**

```
git clone https://github.com/AminaSaoudi/Selenium-Python-E2E-Testing-Suite.git
cd Selenium-Python-E2E-Testing-Suite
```

**Create and activate a virtual environment**

```
python -m venv venv source venv/bin/activate # (or .\venv\Scripts\activate on Windows)
```

**Install dependencies**

```
pip install -r requirements.txt
```

**Run pytest**

(This will run locally using webdriver-manager)
```
pytest
```


### Viewing the Allure Report

After running the tests (with either method), your test results are in the allure-results folder.

Make sure you have Allure installed

```scoop install allure or brew install allure```

Serve the report:

```
allure serve allure-results
```
Your browser will automatically open with a beautiful, interactive dashboard (Example below)

<img width="1857" height="888" alt="image" src="https://github.com/user-attachments/assets/64a96f21-e8e4-4fd0-8dcf-f05472fbb2e4" />
