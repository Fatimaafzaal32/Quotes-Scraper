# Quotes Scraper

A Python web scraping project built with **Requests** and **BeautifulSoup**.

This scraper collects quotes from [Quotes to Scrape](https://quotes.toscrape.com/) and saves the data into a CSV file.

## What it does

The scraper collects:

- Quote
- Author
- Tags

It also goes through all available pages automatically instead of scraping only the first page.

## Features

- Scrapes multiple pages using pagination
- Extracts quotes, authors, and tags
- Handles missing elements
- Handles request errors and timeouts
- Cleans scraped text
- Removes duplicate quotes
- Saves the final data in `Quotes.csv`

## Technologies Used

- Python
- Requests
- BeautifulSoup
- CSV
- `urllib.parse`

## Project Structure

```text
Quotes_Scraper/
│
├── main.py
├── Quotes.csv
└── README.md
```

## How to Run

Install the required libraries:

```bash
pip install requests beautifulsoup4
```

Then run:

```bash
python main.py
```

The scraped data will be saved in:

```text
Quotes.csv
```

## What I Practiced

This project helped me practice real web scraping concepts such as:

- Sending HTTP requests
- Parsing HTML with BeautifulSoup
- Finding elements using tags and classes
- Extracting links and following pagination
- Handling missing data
- Handling request errors
- Cleaning scraped data
- Removing duplicates
- Exporting structured data to CSV

This is a learning project and part of my Python web scraping practice.