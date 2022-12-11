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
    candidates = load_candidates()
    list_candidates = []

    for candidate in candidates:
        if skill_name == candidate["skills"]:
            list_candidates.append(candidate["skills"])

    return list_candidates
