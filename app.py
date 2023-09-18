from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data analyst',
        'location': 'abu dhabi',
        'salary': 'USD 1000'
    },
    {
        'id': 2,
        'title': 'Data scientist',
        'location': 'warszawa',
        'salary': 'USD 3000'
    },
    {
        'id': 3,
        'title': 'Data admin',
        'location': 'oslo',
        'salary': 'USD 2000'
    },
    {
        'id': 4,
        'title': 'Database engineer',
        'location': 'zurich',
        'salary': 'USD 1500'
    },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
