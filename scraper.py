import json
import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import Counter

# Website URL
BASE_URL = "https://quotes.toscrape.com"

# User-Agent header
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; StudentQuoteScraper/1.0)"
}


# Function to scrape quotes from multiple pages
def scrape_quotes():

    url = BASE_URL + "/"
    all_quotes = []

    while url:

        try:
            print("\nScraping:", url)

            # Send HTTP request
            response = requests.get(
                url,
                headers=HEADERS,
                timeout=10
            )

            response.raise_for_status()

            # Parse HTML content
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract quotes
            quotes = soup.select("div.quote")

            for quote in quotes:

                text = quote.select_one("span.text")
                author = quote.select_one("small.author")

                tags = [
                    tag.get_text(strip=True)
                    for tag in quote.select("a.tag")
                ]

                all_quotes.append({
                    "text": text.get_text(strip=True) if text else "N/A",
                    "author": author.get_text(strip=True) if author else "N/A",
                    "tags": tags
                })

            print("Quotes collected:", len(all_quotes))

            # Find next page
            next_page = soup.select_one("li.next a")

            if next_page:
                url = urljoin(BASE_URL, next_page["href"])
            else:
                url = None

            # Polite delay between requests
            if url:
                time.sleep(1)

        except requests.exceptions.RequestException as e:

            print("Request error:", e)
            break

    return all_quotes


# Main program
if __name__ == "__main__":

    # Start scraping
    data = scrape_quotes()

    print("\n" + "=" * 45)
    print("          SCRAPING COMPLETED")
    print("=" * 45)

    # Display total quotes
    print("\nTotal quotes collected:", len(data))

    # Save data into JSON file
    with open("quotes.json", "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("\nQuotes successfully saved to quotes.json")

    # Save data into TXT file
    with open("quotes.txt", "w", encoding="utf-8") as file:

        for index, quote in enumerate(data, start=1):

            file.write(f"Quote {index}\n")
            file.write(f"Text: {quote['text']}\n")
            file.write(f"Author: {quote['author']}\n")
            file.write(f"Tags: {', '.join(quote['tags'])}\n")
            file.write("-" * 60 + "\n")

    print("Quotes successfully saved to quotes.txt")

    # Calculate author statistics
    authors = Counter(
        quote["author"] for quote in data
    )

    # Calculate tag statistics
    all_tags = []

    for quote in data:
        all_tags.extend(quote["tags"])

    tags = Counter(all_tags)

    # Display statistics
    print("\n" + "=" * 45)
    print("          SCRAPING STATISTICS")
    print("=" * 45)

    if authors:

        author, count = authors.most_common(1)[0]

        print("\nMost quoted author:", author)
        print("Number of quotes:", count)

    if tags:

        tag, count = tags.most_common(1)[0]

        print("\nMost common tag:", tag)
        print("Tag frequency:", count)

    print("\n" + "=" * 45)
    print("       ALL TASKS COMPLETED SUCCESSFULLY")
    print("=" * 45)