from scrapy import cmdline

cmdline.execute("scrapy crawl esco -o ../output/esco.json".split())
