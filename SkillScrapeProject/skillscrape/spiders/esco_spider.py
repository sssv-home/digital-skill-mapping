import json
import scrapy
import logging
import csv
from skillscrape.urls import digital_set, set1

from skillscrape import items


class EscoSpider(scrapy.Spider):
    name = "esco"

    def start_requests(self):
        # urls = set1
        urls = digital_set
        # urls = [
        #   "http://suraj-pc:8080/resource/skill?uri=http://data.europa.eu/esco/skill/aeecc330-0be9-419f-bddb-5218de926004&language=en",
        #  "http://suraj-pc:8080/resource/concept?uri=http://data.europa.eu/esco/isco/C25&language=en",
        # "http://suraj-pc:8080/resource/concept?uri=http://data.europa.eu/esco/isco/C2166&language=en"
        # ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: scrapy.http.Response):
        body = json.loads(response.text)
        links = body["_links"]

        title = body["preferredLabel"]["en"]
        labels = body.get("alternativeLabel", {}).get("en", [])
        description = body["description"]["en"]["literal"]
        skill_types = [s_type["title"] for s_type in links.get("hasSkillType", [])]

        class_name = body["className"]
        if class_name == "Skill":
            yield {"type": "Skill", "title": title, "skill_type": skill_types, "labels": labels, "description": description}
        elif class_name == "Concept":
            yield {"type": "Concept", "title": title, "labels": labels, "description": description}
        elif class_name == "Occupation":
            yield {"type": "Occupation", "title": title, "labels": labels, "description": description}
        # hasOptionalSkill
        link_types = ["narrowerSkill", "narrowerConcept", "narrowerOccupation", "hasEssentialSkill"]
        for link_type in link_types:
            for link in links.get(link_type, []):
                logging.info("Following '%s' '%s'", link_type, link["title"])
                yield response.follow(link["href"])
