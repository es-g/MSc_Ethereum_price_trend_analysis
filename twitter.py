import twint
#configuration
config = twint.Config()
config.Search = "bitcoin"
config.Lang = "en"
config.Limit = 10000000
config.Since = "2015-04-29"
config.Until = "2022-06-20"
config.Store_json = True
config.Output = "historical_tweets.json"
#running search
twint.run.Search(config)