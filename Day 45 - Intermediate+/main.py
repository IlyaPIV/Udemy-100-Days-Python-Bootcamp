 
# import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(markup=contents, features="html.parser")
print(soup.title)
print(soup.title.string)

print(soup.prettify())

all_anchor = soup.find_all(name="a")
print(all_anchor)
for tag in all_anchor:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.getText())

all_headings = soup.find_all(name="h3", class_="heading")
for head in all_headings:
    print(head.getText())

company_url = soup.select_one(selector="p a")
print(company_url.getText())
print(company_url.get("href"))

headings = soup.select(selector=".heading")
print(headings)
