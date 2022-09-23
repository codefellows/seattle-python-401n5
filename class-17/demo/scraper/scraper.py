import requests
from bs4 import BeautifulSoup

# https://testing-www.codefellows.org/courses/code-400/

URL = 'https://testing-www.codefellows.org/courses/code-400/'
page = requests.get(URL)
# print(page.content)

soup = BeautifulSoup(page.content, "html.parser")

# print(soup)

results = soup.find(class_="course-details")

# print(results.prettify())

titles = results.find_all("h3")

# for title in titles:
#     print(title)
# print(titles)

# https://testing-www.codefellows.org/courses/code-400/
# https://testing-www.codefellows.org/courses/code-401/advanced-software-development-in-python/

anchors = results("a")
# print(anchors)
# for anchor in anchors:
#     print(anchor)

# print(anchors[1])

# python_link = anchors[1]
#
# print(python_link)

links = [anchor["href"] for anchor in anchors]
python_link = links[1]
# print(python_link)
new_python_link = "https://testing-www.codefellows.org" + python_link
# print(new_python_link)

python_content = requests.get(new_python_link)
# print(python_content)
python_link_soup = BeautifulSoup(python_content.content, "html.parser")

article = python_link_soup.select("ul li ul li")

print(article)

print(titles[1].text)
for li in article:
    print(li.text)
