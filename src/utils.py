import os, yaml, time
from functools import wraps
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.yaml")
EXAMPLE_PATH = os.path.join(os.path.dirname(__file__), "config_example.yaml")

def load_config():
    path = CONFIG_PATH if os.path.exists(CONFIG_PATH) else EXAMPLE_PATH
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        print(f"[!] Could not load config ({path}): {e}")
        return {}

def rate_limited(min_interval_seconds=1.0):
    def decorator(func):
        last_time = {"t": 0.0}
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time(); diff = now - last_time["t"]
            if diff < min_interval_seconds:
                time.sleep(min_interval_seconds - diff)
            result = func(*args, **kwargs)
            last_time["t"] = time.time()
            return result
        return wrapper
    return decorator
