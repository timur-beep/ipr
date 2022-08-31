import json

import numpy as np
import pytest
import requests
import ast

@pytest.fixture
def generate_data_for_tests():
    return {
  "p_res": 250,
  "wct": 50,
  "pi": 1,
  "pb": 150
}

def test_calc_model_success(api_client, generate_data_for_tests):
    response = requests.post(url="http://localhost:8002/ipr/calc",
                              json=generate_data_for_tests)
    answer = {
  "q_liq": [
    190.04,
    187.46,
    184.88,
    182.12,
    177.57,
    171.27,
    163.6,
    154.82,
    145.13,
    134.67,
    123.54,
    111.83,
    99.6,
    87.15,
    74.7,
    62.25,
    49.8,
    37.35,
    24.9,
    12.45,
    0
  ],
  "p_wf": [
    1,
    13.45,
    25.9,
    38.35,
    50.8,
    63.25,
    75.7,
    88.15,
    100.6,
    113.05,
    125.5,
    137.95,
    150.4,
    162.85,
    175.3,
    187.75,
    200.2,
    212.65,
    225.1,
    237.55,
    250
  ]
}
    text = response.text
    print()
    text = json.loads(text)
    assert response.status_code == 200
    assert dict(text) == answer
