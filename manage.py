from app import create_app, db
from flask_script import Manager, Shell
from sqlalchemy.sql import func
from app.models import *

# production
app = create_app('development')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, func=func,
                City=TblCity,
                Institution=TblInstitution,
                InstitutionGroup=TblInstitutionGroup,
                TblInstitutionReserve=TblInstitutionReserve, )

manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
