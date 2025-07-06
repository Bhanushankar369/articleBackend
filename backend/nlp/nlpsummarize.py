from newspaper import Article
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


# Create your views here.
def summarize_text(url):
    article = Article(url)
    
    article.download()
    article.parse()
    article.nlp()
    
    summarize = article.summary
    return summarize