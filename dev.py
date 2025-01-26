from flask_migrate import Migrate

from main import create_app
from main import db

app = create_app()
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)