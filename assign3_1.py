from flask import Flask,render_template,jsonify
import json

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api',methods=['GET'])
def api():
  with open('data.json','r') as file:
    data = json.load(file)

    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)