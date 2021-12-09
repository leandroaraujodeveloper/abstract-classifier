from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os

def keywords_to_url(string):
    return string.replace(' ', '+')

keywords = ['recurrent neural networks', 'convolutional neural networks', 'natural language processing', 'reinforcement learning', 'unsupervised learning', 'clustering']

settings = get_project_settings()
process = CrawlerProcess(settings)

search_words = [keywords_to_url(keyword) for keyword in keywords]

arxiv_urls = [f'https://arxiv.org/search/?query={search_word}&searchtype=all&abstracts=show&order=-announced_date_first&size=200' for search_word in search_words]

name_file = 'arxiv_fields_dataset'
if name_file in os.listdir('.'):
    os.remove(name_file)
process.settings.set('FEEDS', {f'{name_file}.csv':{'format':'csv'}})

spider = 'arxiv'
for url, keyword in zip(arxiv_urls, keywords):
    process.crawl(spider, url, keyword)
process.start()
