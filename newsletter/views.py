from typing import Text
from django.shortcuts import render, HttpResponse
import feedparser
import requests
from bs4 import BeautifulSoup
getContent = feedparser.parse('https://argusnews.in/rss/or/feed')

# concodinate This string in all line 
constr = "..."

# get 1st entery 
titleFeed = getContent.entries[0].title
linkFeed = getContent.entries[0].link
descriptionFeed = getContent.entries[0].description


# 2nd Entery 
titleFeed1 = getContent.entries[1].title
linkFeed1 = getContent.entries[1].link
descriptionFeed1 = getContent.entries[1].description


# 3Rd entery 
titleFeed2 = getContent.entries[2].title
linkFeed2 = getContent.entries[2].link
descriptionFeed2 = getContent.entries[2].description

# 4th Entery 
titleFeed3 = getContent.entries[3].title
linkFeed3 = getContent.entries[3].link
descriptionFeed3 = getContent.entries[3].description

# get image using feed url 
# create different request elements for 4abave link
url0 = linkFeed
url1 = linkFeed1
url2 = linkFeed2
url3 = linkFeed3

# get the html page image 1 
r1= requests.get(url0)
htmlcontent1 = r1.content 
soup1 = BeautifulSoup(htmlcontent1, 'html.parser')
news_image1 = (soup1.find('img', class_="fp-img-border mx-auto center-cropped-fp details-fp shimmer-effect").get("src"))
short_newsDescription = (soup1.find("div", class_="details-description").get_text())
replace1 = short_newsDescription.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>','').replace('&nbsp;','').replace('&', '').replace('rsquo;','')
characterPrint1 = replace1[0:300]
finalDescription1 = characterPrint1+constr


# get the html page image 2 
r2= requests.get(url1)
htmlcontent2 = r2.content 
soup2 = BeautifulSoup(htmlcontent2, 'html.parser')
news_image2 = (soup2.find('img', class_="fp-img-border mx-auto center-cropped-fp details-fp shimmer-effect").get("src"))
short_newsDescription2 = (soup2.find("div", class_="details-description").get_text())
replace2 = short_newsDescription2.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>','').replace('&nbsp;','').replace('&', '').replace('rsquo;','')
characterPrint2 = replace2[0:400]
finalDescription2 = characterPrint2+constr



# get the html page image 3 
r3= requests.get(url2)
htmlcontent3 = r3.content 
soup3 = BeautifulSoup(htmlcontent3, 'html.parser')
news_image3 = (soup3.find('img', class_="fp-img-border mx-auto center-cropped-fp details-fp shimmer-effect").get("src"))


# get the html page image 4 
r4= requests.get(url3)
htmlcontent4 = r4.content 
soup4 = BeautifulSoup(htmlcontent4, 'html.parser')
news_image4 = (soup4.find('img', class_="fp-img-border mx-auto center-cropped-fp details-fp shimmer-effect").get("src"))

#send all these values to html pages 

def index(request):
    
    context ={
        #1st article gose here
        'short_description':finalDescription1,
        'newsimage':news_image1,
        'veriable': titleFeed,
        'link1':linkFeed,
        # content for second news 
        'second_newsimage':news_image2,
        'second_veriable': titleFeed1,
        'description2':finalDescription2,
        'link2':linkFeed1,
        # content for Third news 
        'third_newsimage':news_image3,
        'third_veriable': titleFeed2,
        'link3':linkFeed2,
        # content for Fourth news 
        'forth_newsimage':news_image4,
        'forth_veriable': titleFeed3,
        'link4':linkFeed3,
    }
    return render(request, 'index.html', context)

    
    # return HttpResponse("This is Home Page")
def select(request):
    return HttpResponse("This is Select Page")

def post(request):
    return HttpResponse("This is Post Page")