# OrangeHRM Automation & Performance Testing Framework

## Overview

This project is a hybrid Automation and Performance Testing Framework developed for the OrangeHRM application.

The framework includes:

- UI Automation Testing using Playwright with Python and Behave
- API Performance Testing using K6
- CI/CD Integration using GitHub Actions
- Reporting and Artifact Management

The framework follows the Page Object Model (POM) design pattern and supports scalable, maintainable, and reusable test automation.

---

## Tech Stack

- Python
- Playwright
- Behave (BDD)
- K6
- JavaScript
- GitHub Actions
- Jenkins
- Docker
- Git

---

## Test Coverage

### UI Automation

- Login
- Logout
- Create Employee
- Search Employee
- Update Employee
- Delete Employee

### API Performance Testing

- Login API
- Create Employee API

### Performance Metrics

- Response Time
- Latency
- Throughput
- Failure Rate
- Concurrent Users
- P90 Response Time
- P95 Response Time

---

## Framework Structure

```text
Demo_orangehrm
│
├── features
├── pages
├── locators
├── step_definitions
├── utils
├── reports
├── screenshots
├── videos
├── clients
├── config
├── data
├── tests
├── .github/workflows
├── requirements.txt
└── README.md