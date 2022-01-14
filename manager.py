from server import create_app

app = create_app('ProductionConfig')


# 디버그모드 => 파이선 파일을 저장하면, 서버도 자동 재시작
app.run(host='0.0.0.0')