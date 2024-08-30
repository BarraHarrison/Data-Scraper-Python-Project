# Data-Scraper-Python-Project
# Data Scraper project where it asks you to enter a job title and job location. It kinda works in that it sends you a linkedin URL but there is issues with scraping the data.


# This Data Scraper project is designed to automate the process of gathering job listings from LinkedIn based on user-provided job titles and locations. The project utilizes Python’s Selenium library to interact with the LinkedIn website, enabling automated browsing and data retrieval. The scraped job data, including job titles, companies, and locations, is then parsed using BeautifulSoup and saved into a CSV file using pandas for easy access and analysis. Initially, the project aimed to automate the login process via Gmail, but this approach encountered significant challenges due to Google’s security measures, including CAPTCHA verifications.

# As a result, we pivoted to a more straightforward method where the user manually logs into LinkedIn before running the scraper. Another issue encountered was related to session management, specifically with Selenium’s ChromeDriver and the use of the user-data-dir option, which caused problems with creating or accessing the Chrome profile directory. To resolve this, we considered both correcting the profile path and removing the user-data-dir entirely to simplify the session handling.

# The final implementation allows users to manually log in, after which the scraper navigates to the LinkedIn job search page and extracts the relevant data. This project provides a practical example of web scraping while highlighting common issues like session management, handling dynamic web content, and dealing with security restrictions on automated logins.
