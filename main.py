from flask import Flask
from functions import * # load_candidates, get_all, get_by_pk, get_by_skill
import json

app = Flask(__name__)

@app.route("/candidates/<x>")
def candidate_page(x):
    """
    Выводит кандидата под номером x
    :param x: номер кандидата для вывода
    :return: картинка, в зависимости от гендера
             Имя кандидата -
             Позиция кандидата
             Навыки через запятую
    """
    x = int(x)
    url_male = "https://cdn-icons-png.flaticon.com/512/432/432693.png"
    url_female = "https://cdn-icons-png.flaticon.com/512/554/554857.png"
    for candidate in get_all():

        if x == candidate["pk"]:
            if candidate["gender"] == "male":
                url = url_male
                return f"""
    <img src={url}>
    
    <pre>
    Имя кандидата - {get_by_pk(x)["name"]}
    Позиция кандидата {get_by_pk(x)["pk"]}
    Навыки через запятую {get_by_pk(x)["skills"]}
    </pre>"""
            else:
                url = url_female
                return f"""
    <img src={url}>
    
    <pre>
    Имя кандидата - {get_by_pk(x)["name"]}
    Позиция кандидата {get_by_pk(x)["pk"]}
    Навыки через запятую {get_by_pk(x)["skills"]}
    </pre>"""

    return f"<h1>Такого кандидата не существует!</h1>"


@app.route("/")
def main_page():
    """
    Главная страница сайта
    :return: Все кандидаты по типу
             Имя кандидата -
             Позиция кандидата
             Навыки через запятую
    """
    result = []

    for i in get_all():
        text = f"""
    Имя кандидата - {i["name"]}
    Позиция кандидата {i["pk"]}
    Навыки через запятую {i["skills"]}
    """
        result.append(text)
    result = '\n'.join(result)
    return f"""<pre>
    {result}
    </pre>"""


@app.route("/skills/<x>")
def skills_page(x):
    """
    Выводит кандидатов с определенным навыком
    :param x: навык для отбора кандидатов
    :return: список кандидатов по определенном навыку по типу:
             Имя кандидата -
             Позиция кандидата
             Навыки через запятую
    """
    result = []
    if len(get_by_skill(x)) == 0:
        return f"<h1>Такого кандидата не существует!</h1>"
    else:
        for candidate in get_by_skill(x):
            text = f"""
        Имя кандидата - {candidate["name"]}
        Позиция кандидата {candidate["pk"]}
        Навыки через запятую {candidate["skills"]}
        """
            result.append(text)
        result = '\n'.join(result)

        return f"""<pre>
            {result}
            </pre>"""


app.run()
