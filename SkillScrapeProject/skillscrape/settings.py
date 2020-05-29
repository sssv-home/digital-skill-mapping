BOT_NAME = 'SkillScrape'

SPIDER_MODULES = ['skillscrape.spiders']
NEWSPIDER_MODULE = 'skillscrape.spiders'

LOG_LEVEL = 'INFO'

FEEDS = {
    'output/esco.json': {
        'format': 'jsonlines'
    }
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
