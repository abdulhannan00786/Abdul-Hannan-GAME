from flask import Flask  # type: ignore

app = Flask("NT SELLER")

@app.route('/')
def home():
    return 'Welcome to the shoes selling website!'

@app.route('/buy')
def buy_shoes():
    return 'Select the shoes you want to buy'

@app.route('/earn_money')
def earn_money():
    return 'Start earning money by selling shoes'

if "NT SELLER" == '_main_':
    app.run(debug=True)

