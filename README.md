# mobile-rate-comparator
"Python automation tool to compare mobile prices across Amazon &amp; Flipkart with anti-bot bypass and Excel reporting."
# 🛒 Smart Price Comparator (Amazon & Flipkart)

A powerful Python-based web scraping tool that fetches real-time product data from **Amazon** and **Flipkart**, compares prices, and generates a professional Excel report.

## 🚀 Key Features
- **Dual-Platform Scraping:** Simultaneously extracts data from Amazon India and Flipkart.
- **Stealth Mode:** Implements advanced anti-detection techniques to bypass Amazon's bot security (User-Agent spoofing, automation flag removal).
- **Dynamic Content Handling:** Uses **Selenium** with `WebDriverWait` to manage AJAX and slow-loading elements.
- **Automated Data Processing:** Utilizes **Pandas** to clean price strings and normalize data for comparison.
- **Professional Reporting:** Generates an `.xlsx` file with **clickable product links** using `XlsxWriter`.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Automation:** Selenium WebDriver
- **Data Analysis:** Pandas
- **Excel Formatting:** XlsxWriter
- **Environment:** Chrome/ChromeDriver

## 📸 How it Works
1. User enters the Mobile Name, RAM, and Storage.
2. The bot automates searches on both e-commerce sites.
3. It cleans the "₹" and "," symbols to convert prices into numerical data.
4. It saves a structured report named `price-comparison.xlsx`.

## 🛡️ Anti-Bot Implementation
To avoid being blocked, this bot uses:
- `AutomationControlled` flag removal.
- Custom `navigator.webdriver` JavaScript override.
- Random delays and User-Agent rotation.

## 📦 Installation
```bash
pip install selenium pandas xlsxwriter
