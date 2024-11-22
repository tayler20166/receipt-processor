import unittest
from flask_testing import TestCase
from app import app
import re

class TestAPI(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.data = {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6.49"
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
                }
            ],
            "total": "35.35"
        }



    def test_receipts_process_and_receipts_points_flow(self):
        process_response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(process_response.status_code, 200)
        process_data = process_response.json
        data_id = process_data['id']

        points_response = self.client.get(f'/receipts/{data_id}/points')
        self.assertEqual(points_response.status_code, 200)
        self.assertEqual(points_response.json, {'points': 28})



    def test_receipts_process_response_is_json(self):
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.content_type, 'application/json')
        try:
            response_data = response.get_json()
            self.assertIsNotNone(response_data, "Failed to parse JSON")
        except ValueError:
            self.fail("Parsing JSON failed")


    def test_receipts_process_correct_response_data(self):
        response = self.client.post('/receipts/process', json=self.data)
        pattern = r'^\S+$'
        self.assertTrue(re.match(pattern, response.json['id']))

    def test_receipts_process_invalid_JSON(self):
        self.data = ""
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_invalid_retailer(self):
        self.data["retailer"] += "%^$"
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_empty_retailer(self):
        self.data["retailer"] = ""
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_missed_retailer(self):
        del self.data["retailer"]
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_invalid_purchaseDate(self):
        self.data["purchaseDate"] += "%^$"
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_empty_purchaseDate(self):
        self.data["purchaseDate"] = ""
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_missed_purchaseDate(self):
        del self.data["purchaseDate"]
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_invalid_purchaseTime(self):
        self.data["purchaseTime"] += "%^$"
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_empty_purchaseTime(self):
        self.data["purchaseTime"] = ""
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_missed_purchaseTime(self):
        del self.data["purchaseTime"]
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_no_items(self):
        del self.data["items"]
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_invalid_items(self):
        self.data["items"] = ""
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_invalid_total(self):
        self.data["total"] += "%^$"
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_empty_total(self):
        self.data["total"] = ""
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_missed_total(self):
        del self.data["total"]
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_item_invalid_shortDescription(self):
        self.data["items"][0]["shortDescription"] += "%^$"
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_item_empty_shortDescription(self):
        self.data["items"][0]["shortDescription"] = ""
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_item_missed_shortDescription(self):
        del self.data["items"][0]["shortDescription"]
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_item_invalid_price(self):
        self.data["items"][0]["price"] += "%^$"
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_item_empty_price(self):
        self.data["items"][0]["price"] = ""
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_receipts_process_item_missed_price(self):
        del self.data["items"][0]["price"]
        response = self.client.post('/receipts/process', json=self.data)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()