import traceback


def check(label, fn):
    try:
        value = fn()
        print(f"PASS: {label}: {type(value).__name__}")
        return value
    except Exception as exc:
        print(f"FAIL: {label}: {type(exc).__name__}: {exc}")
        traceback.print_exc()
        return None


routes = check("import api.routes", lambda: __import__("api.routes", fromlist=["app"]))
if routes:
    check("parameter_solver all known", lambda: routes.parameter_solver({"parameters": [300, 30000, 3000], "regime_wanted": "sous"}))
    check("parameter_solver one unknown", lambda: routes.parameter_solver({"parameters": [300, 30000, None], "regime_wanted": "sous"}))
    check("equation_finder", lambda: routes.equation_finder({"regime_wanted": "sous", "initial_position": 0.1, "initial_speed": 0.0}, (300, 30000, 3000)))
    check("csv_maker", lambda: routes.csv_maker([(300, 30000, 3000)], [0.1], [1.0]))
