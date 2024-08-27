from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get-url', methods=['GET'])
def get_url():
    return jsonify({"url": "https://my-server-lilac.vercel.app/"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
