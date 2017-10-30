from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Role, Category, Pitch, Review

# create app instance 
app =  create_app('development')

manager = Manager(app)
manager.add_command('server', Server)
@manager.command
def test():
    '''run utitest'''
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role, Category = Category, Pitch = Pitch, Review = Review)

if __name__ == '__main__':
    manager.run()