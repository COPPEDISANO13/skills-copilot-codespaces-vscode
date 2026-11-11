import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Your cloud server is running</title>
    <style>
      body { font: 16px system-ui, sans-serif; margin: 0; min-height: 100vh; display: grid; place-items: center; background: #f3f6fb; color: #172033; }
      main { max-width: 38rem; margin: 2rem; padding: 2.5rem; background: white; border-radius: 1rem; box-shadow: 0 1rem 3rem #17203318; }
      h1 { margin-top: 0; }
      code { background: #eef1f7; padding: .15rem .4rem; border-radius: .3rem; }
    </style>
  </head>
  <body>
    <main>
      <h1>Your cloud server is running 🎉</h1>
      <p>This starter app is deployed on Render and ready for you to customize.</p>
      <p>Server health check: <a href="/health"><code>/health</code></a></p>
    </main>
  </body>
</html>"""


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
