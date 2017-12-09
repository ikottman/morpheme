from flask_script import Manager

from src import create_app


app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()