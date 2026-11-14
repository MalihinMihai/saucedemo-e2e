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

```

## Tests

| File                 | Test                            | What it verifies                |
|----------------------|----------------------------------|----------------------------------|
| `test_login.py`      | `test_login_errors` (4 cases)   | Login error messages            |
| `test_inventory.py`  | `test_inventory_page_products`  | Products page loads after login |
| `test_checkout.py`   | `test_checkout_process`         | Full checkout flow              |

## Run locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
playwright install --with-deps chromium firefox
cp .env.example .env
pytest -v
```
