# 1
def load_candidates():
    """
    ЗАгрузка списка кандитатов из файла
    :return: возвращаем полученный список кандидатов
    """
    import json

    with open("candidates.json", encoding="utf-8") as file:
        candidates = json.load(file)
    return candidates


# 2
def get_all():
    """
    :return: возвращаем готовый список кандидатов с помощью функции load_candidates
    """
    return load_candidates()


# 3
def get_by_pk(pk):
    """
    Получает номер кандидата и возвращает кандидата с этим номером
    :param pk: номер кандидата
    :return: кандидат под номером pk
    """
    for candidate in load_candidates():
        if pk == candidate["pk"]:
            return candidate


# 4
def get_by_skill(skill_name):
    """
    Получает навык и возвращает список кандидатов, с данным навыком
    :param skill_name: навык для отбора кандидатов
    :return: список кандидатов с определенным навыком
    """
    list_candidates = []
    for candidate in load_candidates():
        skills = candidate["skills"].split(", ")
        for skill in skills:
            if skill_name.lower() == skill:
                list_candidates.append(candidate)
                break

    return list_candidates
