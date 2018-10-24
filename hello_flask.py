from flask import Flask

print(__name__)

app = Flask(__name__)

def search4() -> str:
  return 'New route.'
  
@app.route('/')
def hello() -> str:
  return 'Hello world from Flask!'

@app.route('/search4')
def do_search() -> str:
  return search4()

app.run()


