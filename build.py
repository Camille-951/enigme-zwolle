"""Génère docs/index.html (servi par GitHub Pages) : un seul fichier autonome avec l'image intégrée en base64."""
import base64
from pathlib import Path

root = Path(__file__).parent
img = base64.b64encode((root / "src/enigme.jpg").read_bytes()).decode()
html = (root / "src/template.html").read_text(encoding="utf-8")
out = root / "docs/index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html.replace("__IMAGE__", "data:image/jpeg;base64," + img), encoding="utf-8")
print(f"{out} ({out.stat().st_size // 1024} Ko)")
