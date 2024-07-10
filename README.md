# Jomashop Price Scraper

## Workflow

![Scraping for Jomashop(Watch Price) Workflow](Scraping%20for%20Jomashop%28Watch%20Price%29%2000_00_00-00_00_30.gif)

This project is a web scraping application that compares product prices from a Word document with the prices listed on Jomashop's website. The application uses Python, Selenium, and the `python-docx` library to perform the following tasks:

1. Extract product names and prices from a Word document.
2. Search for these products on Jomashop's website.
3. Compare the prices and categorize the products based on the comparison results.
4. Save the results in a JSON file.

## Features

- Extract product data from a Word document (`datalist.docx`).
- Scrape product prices from Jomashop's website.
- Compare the extracted prices with the scraped prices.
- Categorize products into three categories:
  - Products with incorrect prices.
  - Products not found on the website.
  - Products with multiple matches on the website.
- Save the categorized results in a JSON file (`data.json`).

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

### Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/jomashop-price-scraper.git
   cd jomashop-price-scraper
   ```

2. Install the required Python packages:

   ```bash
   pip install selenium python-docx
   ```

3. Download the ChromeDriver executable and place it in a directory included in your system's PATH, or specify the path to the executable in your script.

## Usage

1. Ensure you have the `datalist.docx` file with the product data in the same directory as your script.

2. Run the script:

   ```bash
   python Completed\ Products\kong.py
   ```

3. The results will be saved in a file named `data.json` in the same directory.

## Example `datalist.docx` Format

The Word document should contain a table with two columns:
- The first column for product names.
- The second column for product prices.

## Notes

- Make sure your Chrome browser is up-to-date to avoid compatibility issues with ChromeDriver.
- The script opens and closes the browser for each product, which may be slow for a large number of products.