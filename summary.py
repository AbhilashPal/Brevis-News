from newspaper import Article
import newspaper
def trending():
	trending_terms=newspaper.hot()
	trending_urls=newspaper.popular_urls()[:10]
	return trending_terms,trending_urls
def get_summary(url):
	article=Article(url)
	article.download()
	article.parse()
	text=article.text
	article.nlp()
	text_summary=article.summary
	return text,text_summary