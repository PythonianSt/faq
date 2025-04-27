import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load FAQ data once at startup
with open('faq.json', 'r', encoding='utf-8') as f:
    faq_data = json.load(f)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '').strip()

    best_score = 0
    best_answer = "ขออภัย ไม่พบคำตอบที่ตรงกับคำถามของคุณ"

    for q, a in faq_data.items():
        score = fuzz.token_set_ratio(question, q)
        if score > best_score:
            best_score = score
            best_answer = a

    return jsonify({'answer': best_answer})

if __name__ == "__main__":
    app.run(debug=True)

