"""data/*.json을 web/template.html에 넣어 web/index.html을 만든다."""
import json
from datetime import date
from pathlib import Path

root = Path(__file__).resolve().parent.parent
data = (root / "data/my-cosmetics.json").read_text(encoding="utf-8")
cats = (root / "data/categories.json").read_text(encoding="utf-8")
html = (root / "web/template.html").read_text(encoding="utf-8")
html = (html.replace("__DATA__", json.dumps(json.loads(data), ensure_ascii=False))
            .replace("__CATS__", json.dumps(json.loads(cats), ensure_ascii=False))
            .replace("__UPDATED__", date.today().isoformat()))
(root / "web/index.html").write_text(html, encoding="utf-8")
print("web/index.html")
