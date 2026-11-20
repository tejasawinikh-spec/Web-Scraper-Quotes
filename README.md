# Web Scraper for Headlines & Quotes

## Project Overview

This project is a Python-based web scraper that extracts quotes, author names, and tags from a practice website using Requests and BeautifulSoup.

The application automatically navigates through multiple pages, collects quote information, and saves the extracted data into JSON and TXT files.

It also generates statistics to identify the most quoted author and the most frequently used tag.

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- JSON
- HTML

## Features

- Fetches webpage content using HTTP requests.
- Parses HTML using BeautifulSoup.
- Extracts quotes, authors, and tags.
- Automatically navigates through multiple pages.
- Handles HTTP request errors.
- Uses a timeout and polite delay between requests.
- Exports collected data into JSON format.
- Exports collected data into readable TXT format.
- Calculates the most quoted author.
- Identifies the most common tag.

## Project Structure

```text
Web-Scraper-Quotes/
│
├── scraper.py
├── quotes.json
├── quotes.txt
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/tejasawinikh-spec/Web-Scraper-Quotes.git
```

2. Navigate to the project folder:

```bash
cd Web-Scraper-Quotes
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment (Windows):

```bash
venv\Scripts\activate
```

5. Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Execute the following command:

```bash
python scraper.py
```

The application will automatically scrape all available quote pages and generate the output files.

## Output Files

**quotes.json**

Stores all extracted quotes, author names, and tags in structured JSON format.

**quotes.txt**

Stores the collected information in a readable text format.

## Data Source

Website: https://quotes.toscrape.com/

This website is specifically designed for practicing web scraping and is used as the main data source for this project.

## Scraping Guidelines

- Uses a descriptive User-Agent header.
- Sets a request timeout.
- Waits one second between page requests.
- Uses a publicly accessible practice website.
- Does not access login-protected pages or collect personal information.

## Learning Outcomes

Through this project, I learned:

- How to send HTTP requests using Python.
- How to inspect and parse HTML structures.
- How to extract information using BeautifulSoup selectors.
- How to scrape multiple webpages automatically.
- How to save collected information in JSON and TXT formats.
- How to perform basic data analysis using Python.

## Project Status

Completed

---

Developed as part of the InternCircle Python Programming Internship Project.