# 사용자에 관련된 기능을 수행하는 클래스
# 메쏘드를 만들 때, get/post/put/patch/delete로 만들면, 알아서 메쏘드로 세팅되도록
from flask_restful import Resource
from flask_restful_swagger_2 import swagger

class User(Resource):
    
    @swagger.doc({
      'tags' : ['user'], # 어떤 종류의 기능인지 분류
      'description' : '사용자 정보 조회',
      'parameters' : [
          # dict로 파라미터들을 명시
      ],
      'responses' : {
          # 200 일때의 응답 예시, 400일때의 예시 등
          '200' : {
              'description' : '사용자 정보 조회에 성공'
          },
          '400' : {
              'description' : '사용자 정보 조회 실패' 
          }
      }
    })
    def get(self):
        """사용자 정보 조회"""
        return {
            '임시' : '사용자 정보 조회'
        }

    @swagger.doc({
      'tags' : ['user'], # 어떤 종류의 기능인지 분류
      'description' : '로그인',
      'parameters' : [
          # dict로 파라미터들을 명시
      ],
      'responses' : {
          # 200 일때의 응답 예시, 400일때의 예시 등
          '200' : {
              'description' : '로그인 성공'
          },
          '400' : {
              'description' : '아이디 없는 상황' 
          }
      }
    })
    def post(self):
        """로그인"""
        return {
            '임시' : '로그인 기능'
        }    
    
    @swagger.doc({
      'tags' : ['user'], # 어떤 종류의 기능인지 분류
      'description' : '회원가입',
      'parameters' : [
          # dict로 파라미터들을 명시
      ],
      'responses' : {
          # 200 일때의 응답 예시, 400일때의 예시 등
          '200' : {
              'description' : '회원가입 성공'
          },
          '400' : {
              'description' : '이메일 중복 가입 실패' 
          }
      }
    })  
    def put(self):
        """회원가입"""
        return {
            '임시' : '회원가입 기능'
        }