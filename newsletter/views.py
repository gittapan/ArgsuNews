from typing import Text
from django.shortcuts import render, HttpResponse
from feedparser import html
from requests.models import Response
import feedparser
import requests
from bs4 import BeautifulSoup
NewsFeed = feedparser.parse("https://argusnews.in/rss/or/feed")

# 'title', 'title_detail', 'links', 'link', 'summary', 'summary_detail', 'authors', 'author', 'author_detail', 'published', 
# 'published_parsed', 'id', 'guidislink', 'tags'

# ------------------------Get 1St News from the feed--------------------------
entry = NewsFeed.entries[0]
postTitle0 = entry.title
postLink0 = entry.link
postSummary0 = entry.summary

# ------------------------Get 2nd News from the feed--------------------------
entry1 = NewsFeed.entries[1]
postTitle1 = entry1.title
postLink1 = entry1.link
postSummary1 = entry1.summary

# ------------------------Get 3rdNews from the feed--------------------------
entry2 = NewsFeed.entries[2]
postTitle2 = entry2.title
postLink2 = entry2.link
postSummary2 = entry2.summary

# ------------------------Get 4th News from the feed--------------------------
entry3 = NewsFeed.entries[3]
postTitle3 = entry3.title
postLink3 = entry3.link
postSummary3 = entry3.summary

# ------------------------Get 5th News from the feed--------------------------
entry4 = NewsFeed.entries[4]
postTitle4 = entry4.title
postLink4 = entry4.link
postSummary4 = entry4.summary

# ------------------------Get 6th News from the feed--------------------------
entry5 = NewsFeed.entries[5]
postTitle5 = entry5.title
postLink5 = entry5.link
postSummary5 = entry5.summary

# ------------------------Get 7th News from the feed--------------------------
entry6 = NewsFeed.entries[6]
postTitle6 = entry6.title
postLink6 = entry6.link
postSummary6 = entry6.summary

# replace unwanted tages of html from description
summary0 = postSummary0.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>','').replace('&nbsp;','').replace('&', '').replace('rsquo;','').replace('lsquo;','')
summary1 = postSummary1.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>','').replace('&nbsp;','').replace('&', '').replace('rsquo;','').replace('lsquo;','')
summary2 = postSummary2.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>','').replace('&nbsp;','').replace('&', '').replace('rsquo;','').replace('lsquo;','')
summary3 = postSummary3.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>','').replace('&nbsp;','').replace('&', '').replace('rsquo;','').replace('lsquo;','')
summary4 = postSummary4.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>','').replace('&nbsp;','').replace('&', '').replace('rsquo;','').replace('lsquo;','')
summary5 = postSummary5.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>','').replace('&nbsp;','').replace('&', '').replace('rsquo;','').replace('lsquo;','')
summary6 = postSummary6.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>','').replace('&nbsp;','').replace('&', '').replace('rsquo;','').replace('lsquo;','')

# count paragraphs worde and match it 
characterPrint0 = summary0[0:300]
characterPrint1 = summary1[0:300]
characterPrint5 = summary5[0:300]
characterPrint6 = summary6[0:300]
# Add 3 Dots 
constr = "..."
finalDescription0 = characterPrint0+constr
finalDescription1 = characterPrint1+constr
finalDescription5 = characterPrint5+constr
finalDescription6 = characterPrint6+constr
# get Feed Urls to get Images form that particular page 
ImageUrl0 = postLink0
ImageUrl1 = postLink1
ImageUrl2 = postLink2
ImageUrl3 = postLink3
ImageUrl4 = postLink4
# ImageUrl5 = postLink5
# ImageUrl6 = postLink6
imageUrlResponse0 = requests.get(ImageUrl0)
imageUrlResponse1 = requests.get(ImageUrl1)
imageUrlResponse2 = requests.get(ImageUrl2)
imageUrlResponse3 = requests.get(ImageUrl3)
imageUrlResponse4 = requests.get(ImageUrl4)
# imageUrlResponse5 = requests.get(ImageUrl5)
# imageUrlResponse6 = requests.get(ImageUrl6)
# Response sucessfull return 200 
# creaet bs4 object 
soup0 = BeautifulSoup(imageUrlResponse0.text, 'html.parser')
soup1 = BeautifulSoup(imageUrlResponse1.text, 'html.parser')
soup2 = BeautifulSoup(imageUrlResponse2.text, 'html.parser')
soup3 = BeautifulSoup(imageUrlResponse3.text, 'html.parser')
soup4 = BeautifulSoup(imageUrlResponse4.text, 'html.parser')
# soup5 = BeautifulSoup(imageUrlResponse5.text, 'html.parser')
# soup6 = BeautifulSoup(imageUrlResponse6.text, 'html.parser')

# taget object to get details 
divTagselect0 = soup0.select('#post_detail div.img-fluid')
divTagselect1 = soup1.select('#post_detail div.img-fluid')
divTagselect2 = soup2.select('#post_detail div.img-fluid')
divTagselect3 = soup3.select('#post_detail div.img-fluid')
divTagselect4 = soup4.select('#post_detail div.img-fluid')
# divTagselect5 = soup5.select('#post_detail div.img-fluid')
# divTagselect6 = soup6.select('#post_detail div.img-fluid')

# Find image from div
imageSrc0 =[x.find('img') for x in divTagselect0]
imageSrc1 =[x.find('img') for x in divTagselect1]
imageSrc2 =[x.find('img') for x in divTagselect2]
imageSrc3 =[x.find('img') for x in divTagselect3]
imageSrc4 =[x.find('img') for x in divTagselect4]
# imageSrc5 =[x.find('img') for x in divTagselect5]
# imageSrc6 =[x.find('img') for x in divTagselect6]

# Extract data-src Attributes 
srcList0 = [img['data-src'] for img in imageSrc0]
srcList1 = [img['data-src'] for img in imageSrc1]
srcList2 = [img['data-src'] for img in imageSrc2]
srcList3 = [img['data-src'] for img in imageSrc3]
srcList4 = [img['data-src'] for img in imageSrc4]
# srcList5 = [img['data-src'] for img in imageSrc5]
# srcList6 = [img['data-src'] for img in imageSrc6]

# print only single image data src 
ImageOutput0 = srcList0[0]
ImageOutput1 = srcList1[0]
ImageOutput2 = srcList2[0]
ImageOutput3 = srcList3[0]
ImageOutput4 = srcList4[0]
# ImageOutput5 = srcList5[0]
# ImageOutput6 = srcList6[0]


#send all these values to html pages 

def index(request):
    
    context ={
        #1st article gose here
        'short_description':finalDescription0,
        'newsimage':ImageOutput0,
        'veriable': postTitle0,
        'link1':postLink0,
        # content for second news 
        'second_newsimage':ImageOutput1,
        'second_veriable': postTitle1,
        'description2':finalDescription1,
        'link2':postLink1,
        # content for Third news 
        'third_newsimage':ImageOutput2,
        'third_veriable': postTitle2,
        'link3':postLink2,
        # content for Fourth news 
        'forth_newsimage':ImageOutput3,
        'forth_veriable': postTitle3,
        'link4':postLink3,
    }
    return render(request, 'index.html', context)

    
    # return HttpResponse("This is Home Page")
def ad(request):
    context={
        #1st article gose here
        'short_description':finalDescription0,
        'newsimage':ImageOutput0,
        'veriable': postTitle0,
        'link1':postLink0,

        # content for second news 
        'second_newsimage':ImageOutput1,
        'second_veriable': postTitle1,
        'description2':finalDescription1,
        'link2':postLink1,

        # content for Third news 
        'third_newsimage':ImageOutput2,
        'third_veriable': postTitle2,
        'link3':postLink2,

         # content for Fourth news 
        'forth_newsimage':ImageOutput3,
        'forth_veriable': postTitle3,
        'link4':postLink3,

        #Fifth News Details
        'newsImage5':ImageOutput4,
        'newsTitle5': postTitle4,
        'newsLink5':postLink4,

        #6th News Details
        'newsTitle6': postTitle5,
        'newsDescription6':finalDescription5,
        'newsLink6':postLink5,

        #7th News Details
        'newsTitle7': postTitle6,
        'newsDescription7':finalDescription6,
        'newsLink7':postLink6,
    }
    return render(request, 'ad.html', context)

def post(request):
    return HttpResponse("This is Post Page")
