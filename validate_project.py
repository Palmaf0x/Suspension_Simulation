from fastapi.testclient import TestClient

from api.routes import app
from optimizer.parameter_solver import parameter_solver


def assert_response(response, expected_status=200):
    assert response.status_code == expected_status, (response.status_code, response.text)


client = TestClient(app)
assert_response(client.get("/health"))

for regime, params in [
    ("sous", [300, 30000, 3000]),
    ("critique", [300, 30000, (300 * 30000) ** 0.5 * 2]),
    ("sur", [300, 30000, 7000]),
]:
    response = client.post(
        "/send_data",
        json={"parameters": params, "initial_position": 0.1, "initial_speed": 0.0, "regime_wanted": regime},
    )
    assert_response(response)
    payload = response.json()
    assert len(payload["x_values"]) == len(payload["y_values"]) == 1000
    assert payload["matches"] >= 1
    assert_response(client.get("/get_data"))
    assert_response(client.get("/download_csv"))

for parameters in ([300, 30000, None], [None, 30000, 3000], [None, None, 3000], [None, None, None]):
    matches = parameter_solver({"parameters": parameters, "regime_wanted": "sous"})
    assert matches

assert client.get("/get_data").status_code == 200
print("all end-to-end validations passed")
