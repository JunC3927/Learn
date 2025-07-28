from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return 'HellO cj'

@app.route('/greet')
def great():
    name = request.args.get('name','Guest')
    return f'Hello,{name}!'

@app.route('/api',methods=['POST'])
def api():
    # 接收JSON数据
    data = request.json
    name = data.get('name')
    return f'Hello,{name}!'

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')