Python News Web Scraper

This project is a web scraper developed with Python to extract the latest news from news websites.

The scraper extracts information such as the news title, URL, description, publication date, and image URL (when available) and stores the extracted data in a database.

The main feature that distinguishes this scraper from other web scrapers is its ability to scrape multiple news websites with similar structures using configuration files. This means that, if a new website has a similar structure to the supported websites, it can be added by creating a suitable configuration without requiring major changes to the scraping logic.

Features

• Scrape multiple news websites
• Extract news titles
• Extract news URLs
• Extract news descriptions
• Extract publication dates
• Extract image URLs when available
• Store extracted data in a SQLite database
• Log different stages of the scraping process
• Support multiple websites through configuration
• Clean and organize extracted data before storing it

Technologies

• Python
• Requests
• BeautifulSoup
• SQLite3
• Logging
• Time
• Urllib
• Object-Oriented Programming (OOP)

Requirements

The required Python packages are listed in the "requirements.txt" file.

Installation

First, clone the repository from GitHub:

git clone <repository-url>

Navigate to the project directory:

cd <project-folder>

It is recommended to create a virtual environment for the project:

python -m venv venv

Activate the virtual environment and install the required dependencies:

pip install -r requirements.txt

Usage

After cloning the repository and installing the required dependencies, run the "main.py" file:

python main.py

By default, the scraper uses the configurations available in the project and scrapes the websites defined in the configuration.

Adding a New Website

To scrape a new website, first compare its structure with the websites currently supported by the project.

If the website has a similar structure and does not require significant changes to the scraping logic, you can add it by creating a new configuration.

The configuration can define the information required to extract data such as:

• News title
• News URL
• News description
• Publication date
• Image URL
• News category

Even if a website only provides basic information such as the news title and URL, it can still be scraped. Information that is not available on the website can be handled according to the project's scraping logic.

Output

The scraper processes and organizes the extracted data before storing it in the database.

The stored data includes:

• Website name
• News category
• News title
• News URL
• News description
• Publication date
• Image URL (when available)

The data is stored in a SQLite database.

Screenshots

SQLite Database

Example of the data stored in the SQLite database:

"SQLite Database" (images/database-screenshot.png)

Program Execution and Logs

Example of the scraper running and the logs generated during execution:

"Scraper Logs" (images/logs-screenshot.png)

Configuration Example

Example of a configuration file used to define a website's structure for scraping:

"Configuration Example" (images/config-screenshot.png)

Logging

The project uses Python's built-in "logging" module to record different stages of the scraper's execution.

Logging helps track the execution process and identify errors or potential problems during scraping.

Future Improvements

• Add a module for sending scraped news to different platforms such as Telegram.
• Implement asynchronous scraping using "async" / "await" to improve the efficiency of the scraping process.