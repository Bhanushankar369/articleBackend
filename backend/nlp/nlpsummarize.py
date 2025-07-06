from newspaper import Article

# Create your views here.
def summarize_text(url):
    article = Article(url)
    
    article.download()
    article.parse()
    article.nlp()
    
    summarize = article.summary
    return summarize