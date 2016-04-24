elected_officials_twitter:
	$(eval FILEPATH = ../datasets/$@/toronto-council-2014-2018.csv)
	rm -f $(FILEPATH)
	heroku local:run scrapy crawl $@ \
		-a list_slug=reporterdonpeat/toronto-council-2014-2018 \
		--output $(FILEPATH) ;\

	$(eval FILEPATH = ../datasets/$@/toronto-council-2010-2014.csv)
	rm -f $(FILEPATH)
	heroku local:run scrapy crawl $@ \
		-a list_slug=reporterdonpeat/toronto-city-council-2 \
		--output $(FILEPATH) ;\
