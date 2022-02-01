from flask import Flask, render_template
#installing news api module
from newsapi import NewsApiClient

app = Flask(__name__)

#creating a route function and rendering the templates on that
@app.route('/')
def home():
    #enter client id and api key for authorization
    newsapi = NewsApiClient(api_key="9dd88fa321f340b9838c1cec4f8f859c")

    #for top headlines of news we will create some code
    top_headlines = newsapi.get_top_headlines(sources = 'bbc-news,the-verge')
    #for all the main articles we will code
    all_articles = newsapi.get_everything(sources = 'bbc-news,the-verge')
    #sources is where the news comes into your app by api

    #fetch all the articles of top headlines
    t_articles = top_headlines['articles']
    #fetch all the articles of article news
    a_articles = all_articles['articles']

    #make a list of contents to store the values on that list
    news = []
    desc = []
    img = []
    p_date = []
    url = []

    ##fetch all the contents of articles by using for loop
    for i in range(len(t_articles)):
        main_article = t_articles[i]

        #at last append all the contents in each of the lists
        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []
    url_all = []

    #make another loop for all the articles
    for j in range(len(a_articles)):
        a_article = a_articles[j]

        #append all articles in the list
        news_all.append(a_article['title'])
        desc_all.append(a_article['description'])
        img_all.append(a_article['urlToImage'])
        p_date_all.append(a_article['publishedAt'])
        url_all.append(a_article['url'])


        #make a zip for finding the content directly and shortly
        contents = zip(news,desc,img,p_date,url) 
        all = zip(news_all,desc_all,img_all,p_date_all,url_all)

        #pass it in the rendererd file


    return render_template('home.html',contents=contents,all=all)

if __name__ == '__main__':
    app.run(debug=True)