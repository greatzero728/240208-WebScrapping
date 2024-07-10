# Jomashop Price Scraper

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

## Workflow

![Scraping for Jomashop(Watch Price) Workflow](Scraping%20for%20Jomashop%28Watch%20Price%29%2000_00_00-00_00_30.gif)

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

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Download the ChromeDriver executable and place it in a directory included in your system's PATH, or specify the path to the executable in your script.

## Usage

1. Ensure you have the `datalist.docx` file with the product data in the same directory as your script.

2. Run the script:

   ```bash
   python scraper.py
   ```

3. The results will be saved in a file named `data.json` in the same directory.

## Example `datalist.docx` Format

The Word document should contain a table with two columns:
- The first column for product names.
- The second column for product prices.

## Notes

- Make sure your Chrome browser is up-to-date to avoid compatibility issues with ChromeDriver.
- The script opens and closes the browser for each product, which may be slow for a large number of products.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Additional Instructions:

1. **Add the requirements file:** Create a `requirements.txt` file with the following content:

    ```txt
    python-docx
    selenium
    ```

2. **Script File:** Save your code in a file named `scraper.py`.

3. **Ensure Paths are Correct:** Make sure the paths for `datalist.docx`, the gif file, and the output JSON file are correctly set in your script and `README.md`.

4. **Include License:** If you need a license file, create a `LICENSE` file with the appropriate content. MIT License is a common choice.

This `README.md` file provides a comprehensive guide for users to understand, install, and use your web scraping application.