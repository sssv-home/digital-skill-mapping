import csv


class Skill:
    def __init__(self, title, type, description, alt_labels, digital, source="ESCO", esco_class="Skill"):
        self.title = title
        self.type = type
        self.description = description
        self.alt_labels = alt_labels
        self.alt_labels_list = self.alt_labels.split(";")
        self.alt_labels_list = list(filter(None, self.alt_labels_list))
        self.source = source
        self.esco_class = esco_class
        self.digital = digital

def load_skills(file_path):
    skills_list = []
    with open(file_path, newline='') as skills_file:
        reader = csv.DictReader(skills_file)
        for row in reader:
            skill = Skill(row["title"], row["skill_type"], row["description"], row["alt_labels"], True, source="ESCO",
                          esco_class=row["class_type"])
            skills_list.append(skill)
        skills_file.close()
    return skills_list


class Occupation:
    def __init__(self, job_id, job_title, job_category):
        self.job_id = job_id
        self.job_title = job_title
        self.job_category = job_category


def load_occupations(file_path):
    occupations = []
    with open(file_path, newline='', encoding='utf-8-sig') as occu_file:
        reader = csv.DictReader(occu_file)
        for row in reader:
            occu = Occupation(row["job_id"], row["job_title"].strip('"'), row["category"])
            occupations.append(occu)
        occu_file.close()
    return occupations


class JobPosting:
    def __init__(self, job_id, job_title, job_category, posting_job_description):
        self.job_id = job_id
        self.job_title = job_title
        self.job_category = job_category
        self.posting_job_description = posting_job_description


def load_job_postings(file_path):
    job_postings = []
    with open(file_path, newline='', encoding='utf-8-sig') as jobs_file:
        reader = csv.DictReader(jobs_file)
        for row in reader:
            posting = JobPosting(row["job_id"], row["job_title"].strip('"'), row["category"],
                                 row["posting_job_description"])
            job_postings.append(posting)
        jobs_file.close()
    return job_postings


class SkillToOccuMap:
    def __init__(self, skill, related_jobs):
        self.skill = skill
        self.related_jobs = related_jobs


class OccuToSkillMap:
    def __init__(self, occupation, related_skills):
        self.occu = occupation
        self.related_skills = related_skills


