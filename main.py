from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def Templates():
  return render_template('index002.html')

@app.route('/unifran')
def outra():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0')