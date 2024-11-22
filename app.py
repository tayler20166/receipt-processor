from flask import Flask, request, jsonify, abort
import uuid, math, datetime, re
from modules.validation.ReceiptSchema import ReceiptSchema
from decimal import Decimal
from marshmallow import ValidationError


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key_here'
receipts = {}


@app.route('/receipts/process', methods=['POST'])
def process_receipts():
    if request.is_json:
        req = request.get_json()
        schema = ReceiptSchema()
        try:
            data = schema.load(req)
        except ValidationError as err:
            return jsonify({"error": "The receipt is invalid"}), 400
        
        id = str(uuid.uuid4())
     
        global receipts
        receipts[id] = req
       
        return jsonify({'id': id})
       
    return jsonify({"error": "The receipt is invalid"}), 400


@app.route('/receipts/<id>/points')
def get_receipt_points(id):
    check_for_uuid(id)
    global global_data
    receipt = receipts.get(id)
    print(receipt)
    if receipt:
        points = 0
        alphanumeric_len = 0;
    
        alphanumeric_len = count_alphanumeric_filter(receipt["retailer"])
        points += alphanumeric_len
        
        if is_round_number(receipt["total"]):
            points += 50

        if is_multiple_of_decimal(receipt["total"], 0.25):
            points += 25

        items_len = len(receipt["items"])
        items_len_points = math.floor(items_len / 2)*5
        points += items_len_points

        description_points = get_items_description_points(receipt["items"])
        points += description_points

        if is_odd(int(receipt["purchaseDate"][-2:])):
            points += 6

        if is_needed_time(receipt["purchaseTime"]):
            points += 10
    else:
        return jsonify({"error": "No receipt found for that id"}), 404  
    return jsonify({ "points": points })


def count_alphanumeric_filter(s):
    return len(list(filter(str.isalnum, s)))

def is_round_number(num):
    num = float(num)
    return num % 1 == 0

def is_multiple_of_decimal(num, divisor):
    num = Decimal(str(num))
    divisor = Decimal(str(divisor))
    return num % divisor == 0

def is_odd(num):
    return num % 2 != 0

def is_needed_time(time_data):
    time_parts = time_data.split(':', 1)
    hours = time_parts[0]
    mins = time_parts[1]
    start_time = datetime.time(14, 0)
    end_time = datetime.time(16, 0)
    purchase_time = datetime.time(int(hours), int(mins))

    if start_time <= purchase_time <= end_time:
        return True
    return False

def get_items_description_points(items):
    points = 0
    for item in items:
        trimmed_text = item["shortDescription"].strip()
        text_len = len(trimmed_text)
        if text_len % 3 == 0:
            points += math.ceil(float(item["price"]) * 0.2)
    return points

def check_for_uuid(string):
    uuid_regex = r'^\S+$'
    if not re.match(uuid_regex, string):
        abort(404, description="No receipt found for that id")

if __name__ == '__main__':
    app.run(debug=True, hostz='0.0.0.0', port=5000)