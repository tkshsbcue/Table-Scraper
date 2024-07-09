# Table-Scraper

## Scraping Data from Table (Still in Development)

Table-Scraper is a simple Python tool for scraping tabular data from a specified webpage and saving it as a CSV file.

## Things Needed

- **URL**: The URL of the webpage containing the table.
- **Class Of the Table**: The class attribute of the HTML table element to target the specific table on the webpage.

## How to Use

1. **Install the required libraries**:
    ```sh
    pip install requests pandas beautifulsoup4
    ```

2. **Update the `url` and `class_` variables** in the script with the target URL and table class, respectively.

3. **Run the script**:
    ```sh
    python table_scraper.py
    ```

4. **Output**: The script will save the table data to a CSV file named `financial_data.csv`.


