from flask import Flask, render_template
import requests
from googletrans import Translator

app = Flask(__name__)
translator = Translator()


@app.route('/')
def index():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        quote = data['content']
        author = data['author']

        translated_quote = translator.translate(quote, dest='ru').text
        translated_author = translator.translate(author, dest='ru').text
    else:
        translated_quote = "Не удалось загрузить цитату."
        author = ""

    return render_template('index.html', quote=translated_quote, author=translated_author)


if __name__ == '__main__':
    app.run(debug=True)
