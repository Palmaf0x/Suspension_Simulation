from pathlib import Path

from fastapi.staticfiles import StaticFiles

from api.routes import app


FRONTEND_DIR = Path(__file__).resolve().parent / "fontend_learn"

# Keep explicit page routes for predictable navigation, then serve all relative
# CSS, JavaScript, and image assets from the same frontend directory.
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
