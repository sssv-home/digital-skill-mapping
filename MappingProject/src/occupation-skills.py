import csv
import jsonpickle as jsonpickle
from MappingProject.src.components import Skill, Occupation, JobPosting, SkillToOccuMap

skills_list = []
job_postings = []
occupations = []
map_output = []


def found_text(text, text_to_find):
    return text.find(text_to_find) > -1


with open("../data/digital_skills_esco.csv", newline='') as skills_file:

    reader = csv.DictReader(skills_file)
    for row in reader:
        skill = Skill(row["title"], row["skill_type"], row["description"], row["alt_labels"], True, source="ESCO", esco_class=row["class_type"])
        skills_list.append(skill)
    skills_file.close()

with open("../data/screenskills_occupations.csv", newline='', encoding='utf-8-sig') as occu_file:
    reader = csv.DictReader(occu_file)
    for row in reader:
        occu = Occupation(row["job_id"], row["job_title"].strip('"'), row["category"])
        occupations.append(occu)
    occu_file.close()

with open("../data/screenskills_occupations.csv", newline='', encoding='utf-8-sig') as jobs_file:
    reader = csv.DictReader(jobs_file)
    for row in reader:
        posting = JobPosting(row["job_id"], row["job_title"].strip('"'), row["category"], row["posting_job_description"])
        job_postings.append(posting)
    jobs_file.close()

#occupations = [occupation for ]

progress_count = 0
with open("../map/occu-skill-mapping.json", "w") as outfile:
    outfile.write("[\n")
    try:
        for skill in skills_list:
            progress_count += 1
            skill_job_map = SkillToOccuMap(skill, [])
            is_job_related = False
            for ad in job_postings:
                job = Occupation(ad.job_id, ad.job_title, ad.job_category)
                is_job_related = found_text(ad.posting_job_description, skill.title)
                if not is_job_related:
                    for label in skill.alt_labels_list:
                        if found_text(ad.posting_job_description, label):
                            is_job_related = True
                            break
                if is_job_related:
                    skill_job_map.related_jobs.append(job)
            unique_jobs = {item.job_id: item for item in skill_job_map.related_jobs}
            skill_job_map.related_jobs = list(unique_jobs.values())

            if len(skill_job_map.related_jobs) > 0:
                mapJSON = jsonpickle.encode(skill_job_map, unpicklable=False)
                outfile.write(f"{mapJSON},\n")
            if progress_count % 20 == 0:
                print(f"Mapped {progress_count} skills")
    finally:
        outfile.write("]")
        outfile.close()
