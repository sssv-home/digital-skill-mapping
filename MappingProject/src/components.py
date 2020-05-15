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


class Occupation:
    def __init__(self, job_id, job_title, job_category, job_ads=[]):
        self.job_id = job_id
        self.job_title = job_title
        self.job_category = job_category
        self.job_ads = job_ads


class JobPosting:
    def __init__(self, job_id, job_title, job_category, posting_job_description):
        self.job_id = job_id
        self.job_title = job_title
        self.job_category = job_category
        self.posting_job_description = posting_job_description


class SkillToOccuMap:
    def __init__(self, skill, related_jobs):
        self.skill = skill
        self.related_jobs = related_jobs


class OccuToSkillMap:
    def __init__(self, occupation, related_skills):
        self.occu = occupation
        self.related_skills = related_skills


