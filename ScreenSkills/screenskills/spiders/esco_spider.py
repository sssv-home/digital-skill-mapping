import json
import scrapy
import logging

from ScreenSkills.screenskills import items


class EscoSpider(scrapy.Spider):
    name = "esco"

    def start_requests(self):
        urls = [
            "http://localhost:8080/resource/skill?uri=http://data.europa.eu/esco/skill/aeecc330-0be9-419f-bddb-5218de926004&language=en",
            "http://localhost:8080/resource/concept?uri=http://data.europa.eu/esco/isco/C25&language=en",
            "http://localhost:8080/resource/concept?uri=http://data.europa.eu/esco/isco/C2166&language=en"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: scrapy.http.Response):
        body = json.loads(response.text)
        links = body["_links"]

        title = body["preferredLabel"]["en"]
        labels = body.get("alternativeLabel", {}).get("en", [])
        description = body["description"]["en"]["literal"]
        skill_types = [s_type["title"] for s_type in links.get("hasSkillType", [])]

        className = body["className"]
        if className == "Skill":
            yield items.Skill(title, skill_types, labels, description)
        elif className == "Concept":
            yield items.Concept(title, labels, description)
        elif className == "Occupation":
            yield items.Occupation(title, labels, description)

        link_types = ["narrowerSkill", "narrowerConcept", "narrowerOccupation", "hasEssentialSkill", "hasOptionalSkill"]
        for link_type in link_types:
            for link in links.get(link_type, []):
                logging.info("Following '%s' '%s'", link_type, link["title"])
                yield response.follow(link["href"])
