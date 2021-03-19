import random
from flask import Flask
app = Flask(__name__)
selected_number = random.randint(0,9)

@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media3.giphy.com/media/l378khQxt68syiWJy/' \
           'giphy.gif?cid=ecf05e47wma3aywub64uf9i0nka8wrlutb4m2cupug06yxkz&rid=giphy.gif">'


@app.route('/<int:number>')
def guess(number):
    if number > selected_number:
        return '<h1 style="color:blue;"> Your guess was too high!</h1>'\
               '<img src="https://media4.giphy.com/media/QWGuOFoq82eGx34Zhd' \
               '/giphy.gif?cid=ecf05e47gkfrrjuh20b84rkke6r3se4gqrmjzka5i4fxes3e&rid=giphy.gif">'

    elif number < selected_number:
        return '<h1 style="color:orange;"> Your guess was too low!</h1>'\
               '<img src="https://media4.giphy.com/media/5xtDarqIj5p3klmiEQo' \
               '/200w.webp?cid=ecf05e479hmlrnek30xj2tsenewrs3sdi14eib0tt2fzaf9i&rid=200w.webp">'

    else:
        return '<h1> Your guess was just right!</h1>'\
               '<img src="https://media3.giphy.com/media/xT8qBepJQzUjXpeWU8' \
               '/200w.webp?cid=ecf05e47wn25qarg8mrwptn2gb4me4c4j7z4jozs19pklc4k&rid=200w.webp">'


if __name__ == "__main__":
    app.run(debug=True)

