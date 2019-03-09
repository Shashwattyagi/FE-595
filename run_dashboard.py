from app import flask_app as app


if __name__ == "__main__":
    app.run(
        "0.0.0.0",
        port=11732,
        debug=True,
        threaded=True
    )