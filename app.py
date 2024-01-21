from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

Jobs = [
    {
        'title': 'Software Engineer',
        'location': 'remote',
        'salary': '1000'   
    },

    {
        'title': 'Data Scientist',
        'location': 'remote',
        'salary': '200'
    },
    {
        'title': 'Data Engineer',
        'location': 'remote',
        'salary': '300'
    },
    {
        'title': 'DevOps Engineer',
        'location': 'remote',
        'salary': '400'
    }
]


@app.route('/')
def index():
    return render_template('index.html', jobs=Jobs)

@app.route('/api/jobs')
def jobs():
    return jsonify(Jobs)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 8081,debug=True)