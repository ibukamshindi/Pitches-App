from flask_script import Manager,Shell,Server
from app import create_app,db
from app.models import User
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Comments, PitchCategory, Pitches

# Creating app instance
app = create_app('development')


manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Comments=Comments, PitchCategory=PitchCategory, Pitches=Pitches )
if __name__ == '__main__':
    manager.run()