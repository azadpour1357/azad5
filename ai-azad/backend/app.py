from flask import Flask, request, jsonify
from services.search_service import perform_search
from services.document_service import add_document, get_documents
from models.bert_model import classify_text
from services.tax_calculation_service import calculate_tax

app = Flask(__name__)

# اندپوینت جستجو
@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    results = perform_search(query)
    return jsonify(results)

# اندپوینت اضافه کردن مستند
@app.route('/add-document', methods=['POST'])
def add_document_endpoint():
    data = request.json
    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({"message": "Title and content are required."}), 400

    response = add_document(title, content)
    return jsonify(response), 201

# اندپوینت لیست مستندات
@app.route('/get-documents', methods=['GET'])
def get_documents_endpoint():
    documents = get_documents()
    return jsonify(documents)

# اندپوینت طبقه‌بندی متن با BERT
@app.route('/classify-text', methods=['POST'])
def classify_text_endpoint():
    text = request.json.get('text')
    classification = classify_text(text)
    return jsonify({"classification": classification})

# اندپوینت محاسبات مالیاتی
@app.route('/calculate-tax', methods=['POST'])
def calculate_tax_endpoint():
    income = request.json.get('income')
    tax_rate = request.json.get('tax_rate')

    if not income or not tax_rate:
        return jsonify({"message": "Income and tax rate are required."}), 400

    tax_amount = calculate_tax(income, tax_rate)
    return jsonify({"tax_amount": tax_amount})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')