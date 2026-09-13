#!/usr/bin/env python3
"""app.html(본문 조각) -> index.html(단독 실행 문서)로 감싼다."""
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(HERE, "app.html"), encoding="utf-8").read()
i = src.index("</style>") + len("</style>")
head, body = src[:i].strip(), src[i:].strip()

RESET = """  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    html { color-scheme: light; }
    body { margin: 0; }
    img { max-width: 100%; }
    [hidden] { display: none !important; }
  </style>
"""

doc = '<!doctype html>\n<html lang="ko">\n<head>\n' + RESET + head + "\n</head>\n<body>\n" + body + "\n</body>\n</html>\n"
io.open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(doc)
print("index.html written (%d bytes)" % len(doc))
