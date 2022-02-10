#!/usr/bin/python
import os
import connexion
from flask import g
from flask_cors import CORS

app = connexion.App(__name__, options={"swagger_ui": True})


@app.app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()

CORS(app.app)

if __name__ == "__main__":  # pragma: no cover
    app.run(port=os.environ.get("PORT", 5005), specification_dir='./openapi/')
