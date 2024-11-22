from flask import Blueprint, request, jsonify
import uuid, math
from schemas.receipt_schema import ReceiptSchema
from utils.numeric_utils import get_items_description_points, is_multiple_of_decimal, is_odd, is_round_number
from utils.string_utils import check_for_uuid, count_alphanumeric_filter
from utils.time_utils import is_needed_time
from marshmallow import ValidationError

receipts_bp = Blueprint('Receipts', __name__)
receipts = {}

@receipts_bp.route('/receipts/process', methods=['POST'])
def process_receipts():
    if request.is_json:
        req = request.get_json()
        schema = ReceiptSchema()
        try:
            schema.load(req)
        except ValidationError as err:
            return jsonify({"error": "The receipt is invalid"}), 400
        
        id = str(uuid.uuid4())
     
        global receipts
        receipts[id] = req
       
        return jsonify({'id': id})
       
    return jsonify({"error": "The receipt is invalid"}), 400


@receipts_bp.route('/receipts/<id>/points')
def get_receipt_points(id):
    check_for_uuid(id)
    global global_data
    receipt = receipts.get(id)
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