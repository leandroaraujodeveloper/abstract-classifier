# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class ArxivCrawlerPipeline:
    def process_item(self, item, spider):
        FIELD = 1
        adapter = ItemAdapter(item)
        # abstract = adapter.get('abstract')
        adapter['field'] = adapter.get('field').split('>')[FIELD] 
        # search_word = adapter.get('search_word')
        return item
