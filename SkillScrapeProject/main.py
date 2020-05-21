from scrapy import cmdline

urls = [

    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/82dea303-26e1-4bbc-a07c-cff3cac6b50e&language=en"
]

for url in urls:
    cmdline.execute(f"scrapy crawl esco -a url={url} -o ../output/esco.json".split())
