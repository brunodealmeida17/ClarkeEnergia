from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from graphene_file_upload.flask import FileUploadGraphQLView
import os
from dotenv import load_dotenv
from flask_cors import CORS

from models import db
from schema.fornecedor_schema import schema
from config import Config, TestConfig


load_dotenv
DEBUG = os.getenv('MODE_DEBUG')

def create_app(debug):
    app = Flask(__name__)
    

    if debug == "True":
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(Config)

    print(debug)
    print(type(debug))
    db.init_app(app)    
    Migrate(app, db)
    
    CORS(app, resources={r"/graphql": {"origins": os.getenv('CORS_URI')}})
    app.add_url_rule(
        "/graphql",
        view_func=FileUploadGraphQLView.as_view(
            "graphql",
            schema=schema,
            graphiql=True
        )
    )

    return app

if __name__ == "__main__":
    app = create_app(DEBUG)
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
