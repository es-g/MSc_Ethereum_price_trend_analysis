from gdeltdoc import GdeltDoc, Filters
import datetime

f = Filters(
    keyword = "ethereum",
    start_date = "2020-05-10",
    end_date = "2021-05-11"
)

gd = GdeltDoc()

# Search for articles matching the filters
articles = gd.article_search(f)
articles['seendate'] = articles.seendate.apply(lambda x: datetime.datetime.strptime(x, '%Y%m%dT%H%M%SZ'))

# Get a timeline of the number of articles matching the filters
timeline_vol = gd.timeline_search("timelinevolraw", f)

# Tone calculation described in 10.1109/eScience.2012.6404440
timeline_tone = gd.timeline_search("timelinetone", f)

timeline_vol['datetime'] = timeline_vol.datetime.apply(lambda x: datetime.datetime.strptime(x, '%Y%m%dT%H%M%SZ'))

# timeline_vol.merge(articles, how='left', left_on='datetime', right_on='seendate')


print(articles)