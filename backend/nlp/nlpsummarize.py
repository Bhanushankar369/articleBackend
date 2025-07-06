from newspaper import Article
import nltk

# Try to download both required resources
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')



# Create your views here.
def summarize_text(url):
    article = Article(url)
    
    article.download()
    article.parse()
    article.nlp()
    
    summarize = article.summary
    return summarize