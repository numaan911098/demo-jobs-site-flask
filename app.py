from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

Jobs = [
    {
        'title': 'Software Engineer',
        'company': 'Google',
        'salary': '1000'   
    },

    {
        'title': 'Data Scientist',
        'company': 'Facebook',
        'salary': '200'
    }
]


@app.route('/')
def index():
    return render_template('index.html', jobs=Jobs)

@app.route('/api/jobs')
def about():
    return jsonify(Jobs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 8081,debug=True)