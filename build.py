"""Builds deployable pages for Cloudflare Pages from the fragments in src/.

Each fragment has its <title>/<link>/<style> above the <!--BODY--> marker and
the page body below it. The output in dist/ is a complete HTML document.
"""
from pathlib import Path

ROOT = Path(__file__).parent
SRC, DIST = ROOT / "src", ROOT / "dist"
DIST.mkdir(exist_ok=True)

FAVICON_OLD = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
    "%3Crect width='64' height='64' rx='8' fill='black'/%3E"
    "%3Cg fill='none' stroke='white' stroke-width='2.4'%3E"
    "%3Ccircle cx='17' cy='17' r='11'/%3E%3Ccircle cx='47' cy='17' r='11'/%3E"
    "%3Ccircle cx='17' cy='47' r='11'/%3E%3Ccircle cx='47' cy='47' r='11'/%3E%3C/g%3E"
    "%3Cg fill='white'%3E%3Ccircle cx='17' cy='17' r='3'/%3E%3Ccircle cx='47' cy='17' r='3'/%3E"
    "%3Ccircle cx='17' cy='47' r='3'/%3E%3Ccircle cx='47' cy='47' r='3'/%3E%3C/g%3E%3C/svg%3E"
)

DESCRIPTION = (
    "Turing Robotics S.A.S.: plataformas robóticas de investigación para universidades "
    "y robots de servicio a la medida para empresas. Medellín, Colombia."
)

for name in ("index", "privacidad"):
    frag = (SRC / f"{name}.fragment.html").read_text(encoding="utf-8")
    head, body = frag.split("<!--BODY-->", 1)
    page = (
        "<!doctype html>\n<html lang=\"es\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        f"<meta name=\"description\" content=\"{DESCRIPTION}\">\n"
        "<link rel=\"icon\" type=\"image/png\" href=\"img/isotipo.png\">\n"
        f"{head.strip()}\n</head>\n<body>\n{body.strip()}\n</body>\n</html>\n"
    )
    (DIST / f"{name}.html").write_text(page, encoding="utf-8")
    print("wrote", DIST / f"{name}.html")
