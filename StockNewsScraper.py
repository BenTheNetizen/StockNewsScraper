import feedparser

def parseRSS(rss_url): 
    return feedparser.parse(rss_url)


def getHeadLines(rss_url):
    headlines = []
    
    feed = parseRSS(rss_url)
    for newitem in feed['items']:
        headlines.append(newitem['title'])
        headlines.append(newitem['published'])
        headlines.append(newitem['link'])
        headlines.append("-----------------------------------------")
    #good structures: title, link, and published (time published)
    return headlines



def main(): 
    stock_ticker = input("Enter a stock name or ticker symbol: ")
    allheadlines = []
    
    newsurls = {
            'googlenews': 'https://news.google.com/rss/search?cf=all&hl=en-US&q=' + stock_ticker + '&gl=US&ceid=US:en',            
        }
    
    for key, url in newsurls.items():
        allheadlines.extend(getHeadLines(url))
        
    
    for h in allheadlines:
        print(h)

    
    
    
if __name__ == "__main__":
  main();