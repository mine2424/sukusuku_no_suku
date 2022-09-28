import html
import json
from flask import Flask, render_template, url_for, request
from src.scraping_service import *

app = Flask(__name__)
ss = ScrapingService()


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/scraping', methods=['GET', 'POST'])
def scraping():
    if request.method == 'POST':
        init_url = request.form.get('init_url')
        init_tag_name = request.form.get('init_tag_name')
        init_attrs_key = request.form.get('init_attrs_key')
        init_attrs_value = request.form.get('init_attrs_value')

        bs_res = ss.init_BeautifulSoup(url=init_url)

        res = ss.find_all(
            bs=bs_res,
            tag_name=init_tag_name,
            attrs_key=init_attrs_key,
            attrs_value=init_attrs_value
        )

        input_data = [
            init_url,
            init_tag_name,
            init_attrs_key,
            init_attrs_value,
        ]

        return render_template('scraping.html', posts=res, input_data=input_data)
    else:
        return render_template('scraping.html')

# TODO: DBを使って過去の検索履歴を見れるようにする
