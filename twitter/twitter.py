import twint
#configuration
config = twint.Config()
config.Search = "ethereum"
config.Lang = "en"
config.Limit = 1000000
config.Since = "2022-04-29"
config.Until = "2022-06-20"
config.Store_json = True
config.Output = "historical_tweets2.json"
#running search
twint.run.Search(config)