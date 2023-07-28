from itemadapter import ItemAdapter
from product_spider.models import Product


class ScrapySpidersPipeline:
    def process_item(self, item, spider):
        item_model = Product(**ItemAdapter(item).asdict())
        item_model.save()
        return item
