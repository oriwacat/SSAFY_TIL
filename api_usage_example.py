'''
print("--- 스크립트 시작 ---")
import os
print("--- os 모듈 임포트 완료 ---")

try:
    from openai import OpenAI
    print("--- openai 모듈 임포트 완료 ---")
except Exception as e:
    print(f"--- 임포트 중 오류 발생: {e} ---")

print("--- 스크립트 종료 ---")
'''