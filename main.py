from flask import Flask
from functions import * # load_candidates, get_all, get_by_pk, get_by_skill
import json

app = Flask(__name__)

@app.route("/candidates/<x>")

def candidate_page(x):
    x = int(x)
    url_male = "https://winaero.com/blog/wp-content/uploads/2018/08/Windows-10-user-icon-big.png"
    url_female = ""
    for candidate in get_all():

        if x == candidate["pk"]:
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
    result = []
    candidates = load_candidates()

    for i in candidates:
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

app.run()
