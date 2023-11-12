import scrapy

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.00.00.00.00.00.html']

    def parse(self, response):
        # extract book info
        # this is just an example, you should adjust the selectors to match the real web structure
        for book in response.css('ul.bang_list li'):
            yield {
                'name': book.css('.name::text').get(),
                'author': book.css('.author::text').get(),
                'price': book.css('.price::text').get()
            }
        # follow links to next pages
        # this is just an example, you should adjust the selectors to match the real web structure
        next_page = response.css('.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)