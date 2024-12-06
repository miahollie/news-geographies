## import libraries
import csv
import time
from bs4 import BeautifulSoup
import requests

## make the request
url = "https://www.nycitynewsservice.com/"
response = requests.get(url)
page_content = response.content

## create an empty list
rows = []

## parse with beautiful soup
soup = BeautifulSoup(page_content, "html.parser")
story_block = soup.find("div", class_ = "posts-wrapper")
stories = story_block.find_all("div", class_ = "post-details")

## loop through and grab the values
for story in stories:
    headlines = story.find("h2", class_ = "post-title").get_text().strip().split("\n")
    links = story.find("a", href = True)["href"]
    excerpts = story.find("p", class_ = "post-excerpt").get_text()
    date = story.find("li", class_ = "post-date").get_text()
    row = {
        "headlines": headlines,
        "links": links,
        "excerpts": excerpts,
        "date": date,
    }
    rows.append(row)
    print(row)

# write to a new csv file
with open ("news-service-articles.csv", "w+") as csvfile: 
      fieldnames = ["headlines","links", "excerpts", "date"] 
      writer = csv.DictWriter(csvfile, fieldnames = fieldnames) 
      writer.writeheader() 

      for row in rows: 
          writer.writerow(row)





