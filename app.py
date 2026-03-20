from flask import Flask, render_template, request
import json
import io

app = Flask(__name__, static_folder="static", template_folder="templates")


def load_json(file_storage):
    return json.load(io.TextIOWrapper(file_storage, encoding="utf-8"))


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/resultado", methods=["POST"])
def resultado():
    followers_file = request.files.get("followers")
    following_file = request.files.get("following")

    result = {
        "nao_seguem_de_volta": [],
        "voce_nao_segue": [],
        "followers_list": [],
        "following_list": [],
        "counts": {
            "followers": 0,
            "following": 0,
            "not_following_back": 0
        }
    }

    if followers_file and following_file:
        followers_data = load_json(followers_file)
        following_data = load_json(following_file)

        followers = {
            item["string_list_data"][0]["value"]
            for item in followers_data
            if item.get("string_list_data")
        }

        following = {
            item["string_list_data"][0]["value"]
            for item in following_data["relationships_following"]
            if item.get("string_list_data")
        }

        nao_seguem_de_volta = sorted(following - followers)
        voce_nao_segue = sorted(followers - following)
        followers_list = sorted(followers)
        following_list = sorted(following)

        result = {
            "nao_seguem_de_volta": nao_seguem_de_volta,
            "voce_nao_segue": voce_nao_segue,
            "followers_list": followers_list,
            "following_list": following_list,
            "counts": {
                "followers": len(followers_list),
                "following": len(following_list),
                "not_following_back": len(nao_seguem_de_volta)
            }
        }

    return render_template("resultado.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)