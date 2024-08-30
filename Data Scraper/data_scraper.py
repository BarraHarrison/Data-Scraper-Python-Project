from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

def fetch_html_content_selenium(url):
    # Setup Chrome options to keep the session open
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=/path/to/your/chrome/profile")  # Ensure to replace this with the correct path
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)  # Navigate to the job search URL
        time.sleep(10)   # Wait for the page to load

        html = driver.page_source  # Get the page source
    except Exception as e:
        print(f"Error occurred: {e}")
        html = None
    finally:
        driver.quit()  # Close the browser
    return html

def parse_job_listings(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    jobs = []
    
    job_cards = soup.find_all('div', class_='result-card__contents job-result-card__contents')
    for job_card in job_cards:
        job_title = job_card.find('h3', class_='result-card__title job-result-card__title').text.strip()
        company_name = job_card.find('h4', class_='result-card__subtitle job-result-card__subtitle').text.strip()
        job_location = job_card.find('span', class_='job-result-card__location').text.strip()
        
        jobs.append({
            'Title': job_title,
            'Company': company_name,
            'Location': job_location
        })
    
    return jobs

def save_jobs_to_csv(jobs, filename="job_listings.csv"):
    df = pd.DataFrame(jobs)
    df.to_csv(filename, index=False)
    print(f"Saved {len(jobs)} jobs to {filename}")

if __name__ == "__main__":
    job_title = input("Enter the job title: ").replace(' ', '%20')
    location = input("Enter the job location: ").replace(' ', '%20')

    search_url = f"https://www.linkedin.com/jobs/search/?keywords={job_title}&location={location}"
    print(f"Constructed URL: {search_url}")
    
    html_content = fetch_html_content_selenium(search_url)
    if html_content:
        job_listings = parse_job_listings(html_content)
        print(f"Found {len(job_listings)} job listings.")
        save_jobs_to_csv(job_listings)
