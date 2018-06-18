import scrapy


class AnalysisSpider(scrapy.Spider):
	name = "analysis"
	def start_requests(self):
		url = "http://bizenglish.adaderana.lk/category/analysis/page/"
		urls = []
		for i in range(28):
			y = url + str(i+1)+"/"
			urls.append(y)
		for url in urls:
		    yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]
		print(page)
		filename = 'analysis-%s.html' % page
		with open(filename, 'wb') as f:
		    f.write(response.body)
		self.log('Saved file %s' % filename)
