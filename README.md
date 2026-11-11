# Playwright & Pytest E2E Test Suite

[![Playwright Tests](https://github.com/MalihinMihai/saucedemo-e2e/actions/workflows/playright.yml/badge.svg)] - CI Status.

Automated E2E testing framework built with **Python**, **Pytest**, and **Playwright** for SauceDemo - https://www.saucedemo.com/, featuring Page Object Model (POM) design and session storage authentication.

---

## Structure

```text
saucedemo/
├── .github/workflows/    # CI/CD workflows (playwright.yml)
├── auth/                 # Generated session state files
├── pages/                # Page Object Model classes
├── tests/                # Test cases & conftest.py
├── .env                  # Environment variables
├── pytest.ini            # Pytest configuration
└── requirements.txt      # Project dependencies

## Test Coverage & Architecture

* **Login Tests**: UI error validation (locked-out user, invalid credentials, missing fields).
* **Inventory Tests**: Page title (`Products`) and product count (6 items) validation.
* **Checkout Flow**: E2E test – item selection, cart verification, and order completion.
* **Auth & Architecture**: Session storage reuse (`auth/*.json`) + Page Object Model design.
  * Cart quantity verification (2 items).
  * Checkout form submission (`John`, `Doe`, `12345`).
  * Final order execution (`finish_order`).
