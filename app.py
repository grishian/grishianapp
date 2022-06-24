import sys
from myapp import create_app, db

sys.dont_write_bytecode = True

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SECRET_KEY'] = 'my secret key'
# db = SQLAlchemy(app)
