import csv
import jsonpickle
from MappingProject.src.components import Skill, Occupation, JobPosting, SkillToOccuMap, OccuToSkillMap, load_skills, \
    load_job_postings, load_occupations

skills_list = load_skills("../data/digital_skills_esco.csv")
job_postings = load_job_postings("../data/job_postings.csv")
occupations = load_occupations("../data/screenskills_occupations.csv")
map_output = []


def found_text(text, text_to_find):
    return text.find(text_to_find) > -1


progress_count = 0

with open("../map/occu-skill-mapping.json", "w") as outfile:
    outfile.write("[\n")
    try:
        for occu in occupations:
            progress_count += 1
            occu_skill_map = OccuToSkillMap(occu, [])
            ads = [ad for ad in job_postings if ad.job_id == occu.job_id]
            combined_job_ads = "\n".join(str(x.posting_job_description) for x in ads)
            is_skill_related = False
            for skill in skills_list:
                is_skill_related = found_text(combined_job_ads, skill.title)
                if not is_skill_related:
                    for label in skill.alt_labels_list:
                        if found_text(combined_job_ads, label):
                            is_skill_related = True
                            break
                if is_skill_related:
                    occu_skill_map.related_skills.append(skill)
            if len(occu_skill_map.related_skills) > 0:
                mapJSON = jsonpickle.encode(occu_skill_map, unpicklable=False)
                outfile.write(f"{mapJSON},\n")
            if progress_count % 10 == 0:
                print(f"Mapped {progress_count} occupations")
    finally:
        outfile.write("]")
        outfile.close()
