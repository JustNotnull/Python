# coding:utf-8

from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from ihome import create_app,db

app = create_app("develop")

#管理工具对象
manger = Manager(app)
Migrate(app,db)
manger.add_command("db",MigrateCommand)

if __name__ == '__main__':
    print (app.url_map)
    manger.run()



