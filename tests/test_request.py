import os
import unittest

from marinetrafficapi.client import Client


class TestRequest(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self._base_url = 'https://services.marinetraffic.com/en/api/exportroutes/_api_key_'
        self._url = self._base_url + '/msgtype:simple/protocol:jsono/port_start_id:1/' \
                                     'port_target_id:10/includealternatives:1/includeinland:0'
        self.fake_ok_response_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'routes_ok.json'
        )
        self._request_params = {
            'port_start_id': 1,
            'port_target_id': 10,
            'include_alternatives': True,
            'include_in_land': False,
            'timeout': 10
        }

    def test_set_parameters(self):
        request = Client(
            self._api_key,
            fake_response_path=self.fake_ok_response_path)\
            .port_distances_and_routes(**self._request_params)

        parameters = {
            'query': {
                'msgtype': 'simple',
                'protocol': 'jsono',
                'port_start_id': 1,
                'port_target_id': 10,
                'includealternatives': '1',
                'includeinland': '0'
            },
            'path': [self._base_url]
        }
        self.assertEqual(request.api_reguest.parameters, parameters)
        self.assertEqual(request.api_reguest._timeout, 10)

    def test_prepare_url(self):
        request = Client(
            self._api_key,
            fake_response_path=self.fake_ok_response_path)\
            .port_distances_and_routes(**self._request_params)

        self.assertEqual(request.api_reguest.url, self._url)
