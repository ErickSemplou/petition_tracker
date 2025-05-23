from flask import Flask, request, jsonify
from datetime import date
from collections import defaultdict

app = Flask(__name__)

stats = defaultdict(lambda: {'visits': 0, 'clicks': defaultdict(int)})

@app.route('/track', methods=['POST'])
def track():
    data = request.json
    today = date.today().isoformat()
    if data.get("type") == "visit":
        stats[today]['visits'] += 1
        return jsonify({"message": "Visit recorded"})
    elif "id" in data:
        stats[today]['clicks'][data["id"]] += 1
        return jsonify({"message": "Click recorded"})
    return jsonify({"error": "Invalid request"}), 400

@app.route('/stats', methods=['GET'])
def get_stats():
    today = date.today().isoformat()
    return jsonify({
        "visits": stats[today]['visits'],
        "clicks": stats[today]['clicks']
    })

if __name__ == '__main__':
    app.run(debug=True)