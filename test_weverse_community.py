import os
import pathlib
from dotenv import load_dotenv
from weverse_community_page import WeverseCommunityPage

load_dotenv()

def test_weverse_post(page):
    community_page = WeverseCommunityPage(page)
    
    # 0. 테스트 데이터 불러오기
    test_id = os.getenv("TEST_ID")
    test_pw = os.getenv("TEST_PW")
    
    # 1. 로그인 및 커뮤니티 가입
    print("\n1. 인증코드 입력 대기 중...")
    community_page.login(test_id, test_pw)
    community_page.enter_and_join_community()
    print("\n2. 커뮤니티 가입 완료 및 프로필 엔드 진입 중...")
    
    # 2.미디어 파일 경로 변환(assets 폴더 기준)
    image_file = str(pathlib.Path("assets/Test_Image.jpg").absolute())
    video_file = str(pathlib.Path("assets/Test_Video.mp4").absolute())
    
    # 3. 포스트 생성 (텍스트 + 이미지)
    initial_msg = "이미지 포스팅"
    community_page.write_post_with_image(initial_msg, image_file)
    assert page.get_by_text(initial_msg).is_visible()
    print("\n3. 포스트 등록 완료 및 수정 진행 중...")
    
    # 4. 포스트 수정 (이미지 삭제 → 비디오 교체)
    edited_msg = "비디오 교체"
    community_page.modify_post_with_video(edited_msg, video_file)
    assert page.get_by_text(edited_msg).is_visible()
    print("\n4. 포스트 수정 및 삭제 진행 중...")
    
    # 5. 포스트 삭제
    community_page.remove_post()
    page.wait_for_timeout(2000) # 삭제 처리 애니메이션 대기
    print("\n5. 포스트 삭제 완료 및 최종 결과 도출")
    
    assert community_page.no_post_message.is_visible()
    print("\n==============================")
    print("[과제 2-2 테스트 결과]")
    print("커뮤니티 가입 및 프로필 엔드 진입 완료")
    print("포스트 등록 완료 (텍스트 + 이미지)")
    print("포스트 수정 완료 (이미지 삭제 -> 비디오 교체)")
    print("포스트 삭제 완료")
    print(f"포스트 삭제 및 안내 메시지 확인: '{community_page.no_post_message.inner_text()}'")
    print("==============================\n")