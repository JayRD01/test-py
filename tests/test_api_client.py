import unittest
from src.api_client import get_location
from unittest.mock import patch 
import requests

class ApiClientTests(unittest.TestCase):

    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "products": [
                {"id": 1, "title": "Essence Mascara Lash Princess"},
                {"id": 2, "title": "Eyeshadow Palette with Mirror"}
            ]
        }

        result = get_location()
        self.assertEqual(result.get(1), "Essence Mascara Lash Princess")
        self.assertEqual(result.get(2), "Eyeshadow Palette with Mirror")
        mock_get.assert_called_once_with("https://dummyjson.com/products")

    @patch('src.api_client.requests.get')
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavaible"),
            unittest.mock.Mock(
                status_code = 200,
                json=lambda: {
             "products": [
                {"id": 1, "title": "Essence Mascara FALLO INTENCIONAL"},
                {"id": 2, "title": "Eyeshadow Palette FALLO INTENCIONAL"}
            ]
        }
            )
        ]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "products": [
                {"id": 1, "title": "Essence Mascara Lash Princess"},
                {"id": 2, "title": "Eyeshadow Palette with Mirror"}
            ]
        }

        with self.assertRaises(requests.exceptions.RequestException):
            get_location()

        #result = get_location()
        # self.assertEqual(result.get(1), "Essence Mascara Lash Princess")
        # self.assertEqual(result.get(2), "Eyeshadow Palette with Mirror")
        # mock_get.assert_called_once_with("https://dummyjson.com/products")

