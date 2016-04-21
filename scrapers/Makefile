elected_officials_twitter:
	$(eval FILEPATH = ../datasets/$@/toronto-council-2014-2018.csv)
	rm $(FILEPATH)
	heroku local:run scrapy crawl $@ \
		-a list_slug=reporterdonpeat/toronto-council-2014-2018 \
		--output $(FILEPATH) ;\
