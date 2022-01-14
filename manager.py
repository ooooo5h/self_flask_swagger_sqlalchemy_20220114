from server import create_app
from flask_script import Manager

app = create_app('ProductionConfig')

manager = Manager(app)

@manager.command
def debug():
    # 추가키워드 debug
    app.config.from_object('server.config.DebugConfig')
    app.run(host='0.0.0.0')
    
@manager.command
def runserver():
    # 추가키워드 runserver
    app.run(host='0.0.0.0')

# 이 파일이 실행될때는 매니저의 커맨드를 기반으로 실행되게 해야한다
if __name__ == '__main__':
    manager.run()