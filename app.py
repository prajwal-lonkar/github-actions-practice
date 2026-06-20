# Code changed to auto run ci/cd pipeline for linter to check python code
from flask import Flask, render_template
app = Flask(_name_)

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/health')
def health():
  return 'Server is up and running'
