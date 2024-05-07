from flask import Flask, request, render_template

from main import parse_query
from db_connection import execute_sql

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['query']
        intent, table = parse_query(user_input)
        response = execute_sql(intent, table)  # This function needs to be implemented
        return render_template('index.html', response=response)
    return render_template('index.html', response=None)

if __name__ == '__main__':
    app.run(debug=True)
