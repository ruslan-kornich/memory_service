import unittest

import requests
from werkzeug.datastructures import ImmutableMultiDict


class TestAPI(unittest.TestCase):
    url = "http://127.0.0.1:8080"

    def test_get_all_records(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_404_url(self):
        response = requests.get(self.url + "/api/v1/")
        self.assertEqual(response.status_code, 404)

    def test_post_with_data(self):
        response = requests.post(self.url, ImmutableMultiDict([("value_used", "5 Kb")]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["value_used"], "5 Kb")

    def test_post_without_data(self):
        response = requests.post(self.url, ImmutableMultiDict())
        self.assertEqual(response.status_code, 404)

    def test_put_change_record(self):
        response = requests.post(
            self.url, ImmutableMultiDict([("value_used", "11111 Kb")])
        )
        record_id = response.json()["_id"]
        data = {"value_used": "7777 Kb"}
        url = self.url + "/" + record_id
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 200)
