import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=Python&limit={LIMIT}"

def extract_indeed_pages():
  indeed_result = requests.get(URL)

  indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

  pagination = indeed_soup.find("div", {"class":"pagination"})

  links = pagination.find_all('a')
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))
  max_page = pages[-1]
  return max_page

def extract_job(html):
  title = html.select_one("span[title]").text
  company = html.select_one(".companyName").text
  location = html.select_one(".companyLocation").text
  return{'title': title, 'company': company, 'location': location}

def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("td", {"class" : "resultContent"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs