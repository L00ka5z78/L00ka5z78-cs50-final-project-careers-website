from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data analyst',
        'location': 'abu dhabi',
        'salary': 'USD 5000'
    },
    {
        'id': 2,
        'title': 'Data scientist',
        'location': 'warszawa',
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
  return render_template('home.html', jobs=JOBS, company_name='Lukasz')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
