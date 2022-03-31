from indeed import extract_indeed_pages, extract_indeed_jobs

from save import save_to_file

last_indeed_page = extract_indeed_pages()

indeed_jobs = extract_indeed_jobs(last_indeed_page)

save_to_file(indeed_jobs)

