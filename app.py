from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/index.html')
def rxn():
    return render_template('index.html')

@app.route('/GetStarted.html')
def output():
    return render_template('GetStarted.html')

    

if __name__ == "__main__":
    app.run(debug=True)
    