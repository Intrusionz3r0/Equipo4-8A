from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('Login.html')

@app.route('/template')
def principal():
    return render_template('template.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 3000, debug = True)