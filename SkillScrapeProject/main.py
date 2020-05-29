from scrapy import cmdline
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

urls = [
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/4f2f2539-3e38-4393-9dac-a9a48af7cd32&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/89a0af2a-edf4-4d1a-8526-f4a8f476cea2&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/4d4b243f-6c3b-48c3-a564-2e7f2d592a3c&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/faed05c0-c1d1-4e34-b575-0dea96459e56&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/2a22ff9e-de3b-408d-b312-5034896cc4f4&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/4ed36f4c-9d5b-4a01-bf59-7f3c7844ce95&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/374d925a-107b-4c99-bc8b-75483441f062&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/d1b1dfdf-7d60-430a-b569-7dd71b2ebeaa&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/b3b79192-f6e0-4aa0-92d1-f876508e05b3&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/5dd01019-3999-4d90-bc8a-7a04b0b208b0&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/49713da4-4e97-4f82-bd1c-16ce7f9179b7&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/4d102082-8d43-4c59-81ab-08a7509f3c40&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/6ba25e0f-7fb8-4879-a1f9-d4f8945966be&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/6fed206a-ac4d-492b-a81a-5a3a0f2b67bc&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/5df63943-f1bc-4438-90f1-92768a7a23c8&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/cadbf9af-1da0-406f-8282-b6d27a7e1a74&language=en",
    "http://suraj-pc:8080/resource/occupation?uri=http://data.europa.eu/esco/occupation/82dea303-26e1-4bbc-a07c-cff3cac6b50e&language=en"
]

process = CrawlerProcess(get_project_settings())
# cmdline.execute(f"scrapy crawl esco -a url={url} -o ../output/esco.json".split())

for url in urls:
    process.crawl('esco', url=url)

process.start()  # the script will block here until the crawling is finished
