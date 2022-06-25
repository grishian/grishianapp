import sys
from myapp import create_app, db
from myapp.bp_user.model_user import Users

sys.dont_write_bytecode = True

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'Users': Users}


if __name__ == "__main__":
    app.run(debug=True)


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SECRET_KEY'] = 'my secret key'
# db = SQLAlchemy(app)
