import pgdb
from flask import Flask, request, send_from_directory
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return send_from_directory('app/public', 'index.html')

if __name__ == '__main__':
    app.run()

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify({'posts': posts})
