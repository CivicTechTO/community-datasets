# Toronto Elected Officials Twitter

The scrapers for this dataset are
[here](/scrapers/community_datasets/spiders/elected_officials_twitter.py).

The list is pulled from [@ReporterDonPeat's](https://twitter.com/reporterdonpeat) Twitter lists:

* [Toronto Council 2010-2014](https://twitter.com/reporterdonpeat/lists/toronto-city-council-2).
* [Toronto Council 2014-2018](https://twitter.com/reporterdonpeat/lists/toronto-council-2014-2018).

### Usage

```
git clone https://github.com/CivicTechTO/community-datasets.git
cd community-datasets/scrapers
mkvirtualenv community-datasets --python=`which python3`
workon community-datasets
pip install -r requirements.txt
make elected_officials_twitter
```
