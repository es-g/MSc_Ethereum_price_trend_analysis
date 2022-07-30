import twint
#configuration
config = twint.Config()
config.Search = "ethereum"
config.Lang = "en"
config.Limit = 1000000
config.Since = "2017-04-29"
config.Until = "2018-06-20"
config.Store_json = True
config.Output = "historical_tweets.json"
#running search
twint.run.Search(config)