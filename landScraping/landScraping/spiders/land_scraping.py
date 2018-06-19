import scrapy
import json


class landsSpider(scrapy.Spider):
	name = "houses"
	def start_requests(self):
		url = "https://www.lankapropertyweb.com/sale/index.php?page="
		urls = []
		for i in range(50):
			y = url + str(i+1)+"/"
			urls.append(y)
		for url in urls:
		    yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		url_first = "https://www.lankapropertyweb.com/"
		for url in response.css("article.item div.thumbnail div.caption1 h4.listing-titles"):
			inner_url = url_first+ url.css('a::attr(href)').extract_first()
			yield scrapy.Request(url=inner_url, callback=self.parse_house)
	
	def parse_house(self, response):
		details_1 = response.css("div.details-heading")[0]
		details_2 = response.css("div.details-heading")[1]

		title = details_1.css("h1::text").extract_first()
		location = details_1.css("span.details-location::text").extract_first()
		price = details_1.css("div.price-detail::text").extract_first().strip()
		details = details_2.css("p").extract_first()

		house_entry = {
			'type' : "house",
            		'title' : title,
			'location' : location,
			'price' : price,
			'details': details
        	}

		file_name = 'corpus/' + title + '.json'
		with open(file_name, 'w') as file:
		    file.write(json.dumps(house_entry, indent=2))

		
		
