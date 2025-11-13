import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    df = pd.read_csv("ai_job_trends_dataset.csv", sep=",")
    return render_template(
        "display.html", tables=[df.to_html(classes="data")], titles=df.columns.values
    )


if __name__ == "__main__":
    app.run(debug=True)
