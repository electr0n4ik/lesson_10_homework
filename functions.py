# 1
def load_candidates():
    import json

    with open("candidates.json", encoding="utf-8") as file:
        candidates = json.load(file)
    return candidates


# 2
def get_all():

    return load_candidates()


# 3
def get_by_pk(pk):
    for candidate in load_candidates():
        if pk == candidate["pk"]:
            return candidate


# 4
def get_by_skill(skill_name):
    list_candidates = []
    for candidate in load_candidates():
        skills = candidate["skills"].split(", ")

        for skill in skills:
            if skill_name == skill:
                list_candidates.append(candidate)
                break

    return list_candidates
