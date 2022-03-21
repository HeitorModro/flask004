from flask import Flask
app = Flask('app')

@app.route('/')
def Templates():
  return '<h1>Meu primeiro template</h1>'

@app.route('/unifran')
def Unifran():
  return '<h2>Universidade de Franca</h2>'

if __name__ == '__main__':
  app.run(host='0.0.0.0')