from bs4 import BeautifulSoup
import requests

page_response = requests.get("https://news.ycombinator.com/news")
webpage = page_response.text

soup = BeautifulSoup(webpage, "html.parser")
articles = soup.find_all(class_="titleline")
article_texts = []
for article_tag in articles:
    # print(article_tag)
    text = article_tag.getText()
    article_texts.append(text)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
