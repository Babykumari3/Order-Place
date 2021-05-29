
from flask import Flask, request, jsonify
app=flask(__name__)

app.route('/')
def hello_world():
    return "Hello, World!"
@app.route('/webhook', methods=['post'])

def webhook():
    #print(request.data)
    data=json.loads(request.data)

    print(data['ticker'])
    print(data["bar"])
    
    return{
        "code":"success",
        "message": data
    }