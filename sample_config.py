HEROKU = True # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["6526097069:AAEWQPVW9Wa9DRITUZYOUg2mCmrrAdVOEuc"]
    ARQ_API_KEY = environ["https://arq.hamker.in"]
    LANGUAGE = environ["Indonesia"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "6526097069:AAEWQPVW9Wa9DRITUZYOUg2mCmrrAdVOEuc"
    ARQ_API_KEY = "Get this from @AIRARobot"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "en"

# Leave it as it is
ARQ_API_BASE_URL = "https://arq.hamker.in"
