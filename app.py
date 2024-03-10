from flask import Flask, render_template, request
import subprocess
import client
import random as rand

MESSAGES = ""

app = Flask(__name__,template_folder='templates')



@app.route('/')

def index():

    return render_template('index.html')


@app.route('/process_form', methods=['POST'])

def process_form():

    file_path = "messages.txt"
    msg = request.form['Message']
    
    out = ""

    client.client_f("Arc",msg,1)
  
    print(msg)

    with open(file_path,'a') as f:
        f.write("|"+msg + "|\n")

    with open(file_path, 'r') as f:
        out = f.read()
        
    return render_template('index.html', msg=out)

    


if __name__ == '__main__':
    app.run(debug=True)

    
