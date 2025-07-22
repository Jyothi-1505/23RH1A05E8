from flask import Flask, jsonify, request

app = Flask(__name__)

# sample data (like a small menoery)
data = [
    {"id": 1, "name": "Alice", "age": 24},
    {"id": 2, "name": "Bob", "age": 30}
]

@app.route('/',methods=['GET'])
def get_users():
    return jsonify(data), 200

#Add the users
@app.route('/users',methods=['POST'])
def add_users():
    new_user = request.json
    new_user['id'] = data[-1]['id']+ 1 if data else 1
    data.append(new_user)
    return jsonify(new_user), 201


#update the users
@app.route('/users/<int:user_id>',methods=['PUT'])
def update_users(user_id):
    user = next((u for u in data if u['id'] == user_id), None)
    if not user:
         return jsonify({'error': 'User not found'}), 404
    
    updated_info = request.json
    user.update(updated_info)
    return jsonify(user)


# Delete the data
@app.route('/user/<int:user_id>', methods=['DELETE']) 

def delete_user(user_id):
    global data
    data = [u for u in data if u['id'] != user_id]
    return jsonify({'message': 
                    f'User with id {user_id} deleted'}), 200
#run the app
if __name__  == '__main__':
    app.run(port=5000)