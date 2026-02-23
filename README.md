# SEIR Web Scraper

## About the Project

This project is a simple Python web scraper. It takes a website URL as input and extracts useful information from the page.

It does the following things:

* Prints the **title** of the webpage
* Prints the **text content** inside the body
* Prints all the **links** present on the page

It uses basic Python and common libraries like `requests` and `BeautifulSoup` to fetch and read the webpage.

---

## Requirements

Make sure you have Python installed.

Install the required libraries using terminal:

```bash
pip install requests beautifulsoup4
```

---

## How to Run

### Step 1: Open terminal in the project folder

```bash
cd SEIR
```

### Step 2: Run the script with a website URL

```bash
python main.py https://example.com
```

Example:

```bash
python main.py https://www.w3schools.com
```

---

## File Structure

```
SEIR/
│
├── main.py
└── README.md
```

---

## Output

The program will display:

* Website title
* Website text content
* All links found on the page

---

## Purpose

This project is useful for learning:

* Basic web scraping
* How to use Python libraries
* How to work with HTML using BeautifulSoup
* How to run Python scripts from terminal
