# Suspension Simulation

A Python application for simulating and optimizing a vehicle suspension model. It includes a FastAPI backend, a browser interface, damping-regime parameter search, and CSV export.

## Run locally

From the project directory, install the dependencies and start the application:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a browser. The configuration page accepts mass, stiffness, damping, initial position, initial speed, and the requested regime. At least one of the three physical parameters may be left blank; the solver searches the configured ranges for valid combinations.

## API endpoints

| Endpoint | Method | Purpose |
|---|---:|---|
| `/health` | GET | Check that the service is running. |
| `/send_data` | POST | Run a simulation and return chart data. |
| `/get_data` | GET | Retrieve the most recent simulation series. |
| `/download_csv` | GET | Download candidate parameters, amplitudes, and stop times as CSV. |

Example request body:

```json
{
  "parameters": [300, 30000, 3000],
  "initial_speed": 0,
  "initial_position": 0.1,
  "regime_wanted": "sous"
}
```

The supported regimes are `sous` for underdamped, `critique` for critically damped, and `sur` for overdamped behavior.

## Project structure

| Directory | Responsibility |
|---|---|
| `physics/` | Numerical suspension equations. |
| `optimizer/` | Parameter validation and regime-constrained search. |
| `analysis/` | Amplitude and time-stop calculations for export. |
| `api/` | FastAPI routes and request models. |
| `fontend_learn/` | Static browser interface and chart scripts. |
| `utils/` | CSV formatting helpers. |

## Validation

The repository includes `smoke_test.py` and `validate_project.py`. Run them with `python3 smoke_test.py` and `python3 validate_project.py` to check imports, numerical paths, all damping regimes, API responses, and CSV export.
