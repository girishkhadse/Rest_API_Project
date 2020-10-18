from flask import Flask,jsonify,request
from db_module import insert , select, logincheck ,update


app = Flask(__name__)


@app.route('/adduser',methods=['POST'])
def adduser():
    data = request.get_json()
    insert(data['id'],data['password'])
    return jsonify({'message':'user Registed'})

@app.route('/viewall')
def viewall():
    output = select()
    return jsonify({'users':output})

@app.route('/login',methods = ['POST'])
def login():
    data = request.get_json()
    output = logincheck(data['id'],data['password'])
    if len(output)>0:
        return jsonify({'message':"Login Succesful"})
    else:
        return jsonify({"message":'Login Failed'})

@app.route('/updatepass',methods = ['POST'])
def updatepass():
    data = request.get_json()
    update(data['id'],data['password'])
    return jsonify({"message":"password updated"})


app.run(port=5000)