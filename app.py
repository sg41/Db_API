import redis
from flask import Flask, jsonify, request

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, db=0)


@app.route('/key-value', methods=['POST'])
def create_key_value():
    data = request.get_json()
    key = data['key']
    value = data['value']

    try:
        redis_client.set(key, value)
        return jsonify({'message': 'Key-value pair created successfully'})
    except redis.RedisError as e:
        return jsonify({'message': 'Failed to create key-value pair', 'error': str(e)})


@app.route('/key-value/<key>', methods=['PUT'])
def update_key_value(key):
    data = request.get_json()
    value = data['value']

    try:
        if redis_client.exists(key):
            redis_client.set(key, value)
            return jsonify({'message': 'Key-value pair updated successfully'})
        else:
            return jsonify({'message': 'Key-value pair not found'})
    except redis.RedisError as e:
        return jsonify({'message': 'Failed to update key-value pair', 'error': str(e)})


@app.route('/key-value/<key>', methods=['GET'])
def read_key_value(key):
    try:
        if redis_client.exists(key):
            value = redis_client.get(key).decode('utf-8')
            return jsonify({'key': key, 'value': value})
        else:
            return jsonify({'message': 'Key-value pair not found'})
    except redis.RedisError as e:
        return jsonify({'message': 'Failed to read key-value pair', 'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
