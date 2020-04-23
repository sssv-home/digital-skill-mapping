from typing import List


def Skill(title: str, skill_types: List[str], labels: List[str], description: str) -> dict:
    return {"type": "Skill", "title": title, "types": skill_types, "labels": labels, "description": description}


def Concept(title: str, labels: List[str], description: str) -> dict:
    return {"type": "Concept", "title": title, "labels": labels, "description": description}


def Occupation(title: str, labels: List[str], description: str) -> dict:
    return {"type": "Occupation", "title": title, "labels": labels, "description": description}
