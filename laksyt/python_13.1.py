
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/alkuluku/<int:luku>")
def alkuluku(luku):
    on_alkuluku = luku >= 2

    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            on_alkuluku = False
            break

    return jsonify({
        "Number": luku,
        "isPrime": on_alkuluku
    })

if __name__ == "__main__":
    app.run(port=3000)
