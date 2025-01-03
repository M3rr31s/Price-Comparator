Price Comparison Web Scraping Script
A simple Python script that automates the process of comparing prices for a product across two websites using web scraping.

Technologies Used
Selenium: Used to automate web browsers for dynamic content extraction.
Pandas: Used to structure and manipulate data efficiently.
BeautifulSoup: Used to parse and extract information from HTML.

Description
A few days ago, I was thinking about upgrading my setup and decided to buy a new graphics card. I spent around 2 hours browsing websites and, in the end, got frustrated with all the time wasted. That's when I thought: "Why not automate this search for myself?"
So, I created this script that compares prices between two websites and helps me find the lowest price quickly. It scrapes the websites using Selenium to handle dynamic content and BeautifulSoup to parse the data. The results are processed with Pandas for easy comparison.

How It Works
The script uses Selenium to open the websites and fetch product pages.
BeautifulSoup is then used to parse the HTML and extract product price data.
The extracted data is stored and manipulated using Pandas to compare prices between the two websites.
The script outputs the lowest price for the product.
