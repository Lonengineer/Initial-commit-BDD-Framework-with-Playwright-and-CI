# 🧪 SauceDemo Selenium BDD Automation Framework

A professional **Test Automation Framework** built with **Python**, **Selenium WebDriver**, and **Behave (Cucumber for Python)** using the **Page Object Model (POM)** design pattern. This project automates testing of the [SauceDemo](https://www.saucedemo.com/) web application.

---

## 📋 Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How to Run Tests](#how-to-run-tests)
- [How to Generate Allure Reports](#how-to-generate-allure-reports)
- [Test Cases](#test-cases)
- [GitHub Usage](#github-usage)
- [CI/CD Integration](#cicd-integration)

---

## 📖 Project Description

This framework is a **Behavior-Driven Development (BDD)** test automation solution designed to test the SauceDemo e-commerce website. It covers product sorting, cart management, checkout flow, negative testing, and performance testing — all written in readable Gherkin syntax.

### Key Features
- ✅ **BDD with Behave** — Human-readable test scenarios in Gherkin
- ✅ **Page Object Model** — Clean separation of test logic and page interactions
- ✅ **Allure Reporting** — Professional HTML reports with screenshots
- ✅ **Automatic Screenshots** — Captured on test failure
- ✅ **Logging** — Detailed logs for debugging
- ✅ **CI/CD Ready** — GitHub Actions workflow included

---

## 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3.11+** | Programming language |
| **Selenium WebDriver** | Browser automation |
| **Behave** | BDD framework (Cucumber for Python) |
| **Allure Reports** | Test reporting |
| **webdriver-manager** | Automatic ChromeDriver management |
| **Google Chrome** | Test browser |
| **GitHub Actions** | CI/CD pipeline |

---

## 📁 Project Structure

```
Tests/
│
├── config/
│   └── config.json              # Framework configuration (URLs, credentials, timeouts)
│
├── features/
│   ├── login.feature            # Login prerequisite scenarios
│   ├── sorting.feature          # Product sorting test cases (4 scenarios)
│   ├── cart.feature             # Shopping cart test cases (5 scenarios)
│   ├── checkout.feature         # Checkout process test cases (2 scenarios)
│   ├── performance.feature      # Page load performance tests (2 scenarios)
│   ├── environment.py           # Behave hooks (setup/teardown, screenshots)
│   └── steps/
│       ├── login_steps.py       # Login step definitions
│       ├── sorting_steps.py     # Sorting step definitions
│       ├── cart_steps.py        # Cart step definitions
│       ├── checkout_steps.py    # Checkout step definitions
│       └── performance_steps.py # Performance step definitions
│
├── pages/
│   ├── base_page.py             # Base page with reusable Selenium methods
│   ├── login_page.py            # Login page object
│   ├── products_page.py         # Products/inventory page object
│   ├── cart_page.py             # Shopping cart page object
│   └── checkout_page.py         # Checkout page object
│
├── utilities/
│   ├── driver_factory.py        # WebDriver creation and configuration
│   ├── config_reader.py         # Configuration file reader
│   ├── logger.py                # Centralized logging utility
│   └── screenshot_helper.py     # Screenshot capture utility
│
├── reports/                     # Generated test reports (auto-created)
├── screenshots/                 # Failure screenshots (auto-created)
├── logs/                        # Log files (auto-created)
│
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI/CD workflow
│
├── requirements.txt             # Python dependencies
├── behave.ini                   # Behave framework configuration
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

---

## ⚙️ Installation

### Prerequisites
- **Python 3.11+** installed ([Download Python](https://www.python.org/downloads/))
- **Google Chrome** browser installed
- **Git** (optional, for cloning the repository)
- **Allure CLI** (for generating reports — see [Allure Reports section](#how-to-generate-allure-reports))

### Step-by-Step Setup

1. **Clone the repository** (or download the project):
   ```bash
   git clone https://github.com/your-username/saucedemo-automation.git
   cd saucedemo-automation
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Create required directories**:
   ```bash
   mkdir reports screenshots logs
   ```

---

## ▶️ How to Run Tests

### Run All Tests
```bash
behave
```

### Run a Specific Feature File
```bash
behave features/sorting.feature
behave features/cart.feature
behave features/checkout.feature
behave features/performance.feature
```

### Run with Console Output (verbose mode)
```bash
behave --no-capture -v
```

### Run in Headless Mode
Edit `config/config.json` and set `"headless": true`, then run normally:
```bash
behave
```

---

## 📊 How to Generate Allure Reports

### Step 1: Install Allure CLI

**Windows (using Scoop):**
```bash
scoop install allure
```

**Windows (using Chocolatey):**
```bash
choco install allure
```

**macOS (using Homebrew):**
```bash
brew install allure
```

### Step 2: Run Tests with Allure Formatter
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

### Step 3: Generate and Open the Report
```bash
allure serve reports/allure-results
```

This will generate a professional HTML report and open it in your browser automatically.

### Alternative: Generate a Static Report
```bash
allure generate reports/allure-results -o allure-report --clean
allure open allure-report
```

---

## 🧪 Test Cases

| # | Test Case | Feature File | Type |
|---|---|---|---|
| 1 | Sort products A-Z | sorting.feature | Functional |
| 2 | Sort products Z-A | sorting.feature | Functional |
| 3 | Sort by price low-to-high | sorting.feature | Functional |
| 4 | Sort by price high-to-low | sorting.feature | Functional |
| 5 | Add a single product to cart | cart.feature | Functional |
| 6 | Add multiple products to cart | cart.feature | Functional |
| 7 | Remove a product from cart | cart.feature | Functional |
| 8 | Cart badge updates correctly | cart.feature | Functional |
| 9 | Complete checkout successfully | checkout.feature | Functional |
| 10 | Checkout with empty fields | checkout.feature | Negative |
| 11 | Remove all products, verify empty cart | cart.feature | Negative |
| 12 | Page loads within acceptable time | performance.feature | Performance |

---

## 🐙 GitHub Usage

### Initial Upload to GitHub

1. **Create a new repository** on GitHub

2. **Initialize Git and push**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - SauceDemo Automation Framework"
   git branch -M main
   git remote add origin https://github.com/your-username/saucedemo-automation.git
   git push -u origin main
   ```

### Branching Strategy
- `main` — Stable, production-ready test code
- `develop` — Development and new test cases
- `feature/*` — Individual feature branches

---

## 🔄 CI/CD Integration

A GitHub Actions workflow is included at `.github/workflows/ci.yml`. It automatically:

1. ✅ Sets up Python and Chrome
2. ✅ Installs dependencies
3. ✅ Runs all tests in headless mode
4. ✅ Generates Allure reports
5. ✅ Uploads reports and screenshots as artifacts

The CI pipeline triggers on:
- Every push to `main` or `develop`
- Every pull request to `main`

---

## 📝 Notes

- **Default credentials**: `standard_user` / `secret_sauce` (configured in `config/config.json`)
- **Browser**: Chrome (managed automatically by `webdriver-manager`)
- **Screenshots**: Automatically saved to `screenshots/` folder on test failure
- **Logs**: Saved to `logs/` folder with timestamps

---

## 👤 Author

Created for university Software Testing course presentation.

## 📄 License

This project is for educational purposes.
