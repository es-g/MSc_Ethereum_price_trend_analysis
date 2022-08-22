from gdeltdoc import GdeltDoc, Filters
import datetime

f = Filters(
    keyword = "ethereum, eth",
    start_date = "2017-08-14",
    end_date = "2022-08-14"
)

gd = GdeltDoc()

# Search for articles matching the filters
articles = gd.article_search(f)

# Get a timeline of the number of articles matching the filters
timeline_vol = gd.timeline_search("timelinevolraw", f)
print('Extracted Volume data')

# Tone calculation described in 10.1109/eScience.2012.6404440
timeline_tone = gd.timeline_search("timelinetone", f)
print('Extracted Tone data')

# timeline_vol['datetime'] = timeline_vol.datetime.apply(lambda x: datetime.datetime.strptime(x, '%Y%m%dT%H%M%SZ'))
# articles['seendate'] = articles.seendate.apply(lambda x: datetime.datetime.strptime(x, '%Y%m%dT%H%M%SZ'))

timeline_tone.to_csv('data/GDELT_tone.csv')
timeline_vol.to_csv('data/GDELT_vol.csv')
articles.to_csv('data/GDELT_articles.csv')

print('Wrote into csv files')

