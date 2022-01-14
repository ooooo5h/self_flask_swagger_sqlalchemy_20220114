from flask_restful import Resource
from flask_restful_swagger_2 import swagger

class User(Resource):
    
    @swagger.doc({
        'tags' : ['user'],
        'description' : '사용자 정보 조회',
        'parameters' : [
            # dict로 파라미터들 명시
        ],
        'responses' : {
            '200' : {
                'description' : '사용자 정보 조회 성공',
            },
            '400' : {
                'description' : '사용자 정보 조회 실패',
            }
        }
    })
    def get(self):
        """사용자 정보 조회"""
        return {
            '임시' : '사용자 정보 조회'
        }
 
 
    @swagger.doc({
        'tags' : ['user'],
        'description' : '로그인',
        'parameters' : [
            
        ],
        'responses' : {
            '200' : {
                'description' : '로그인 성공',
            },
            '400' : {
                'description' : '아이디 없는 상황',
            }
        }
    })    
    def post(self):
        """로그인"""
        return{
            '임시' : '로그인 기능'
        }
    
    
    @swagger.doc({
        'tags' : ['user'],
        'description' : '회원가입',
        'parameters' : [
            
        ],
        'responses' : {
            '200' : {
                'description' : '회원가입 성공',
            },
            '400' : {
                'description' : '이메일 중복으로 가입 실패',
            }
        }
    })        
    def put(self):
        """회원 가입"""
        return{
            '임시' : '회원가입'
        }