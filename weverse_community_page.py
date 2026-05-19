class WeverseCommunityPage:
    def __init__(self, page):
        self.page = page
        
    # ==================================================
    # [1. 로그인 화면 요소]
    # ==================================================
        self.login_btn = page.get_by_role("button", name="로그인") 
        self.email_login_start_btn = page.get_by_role("button", name="이메일로 로그인")
        self.email_input = page.get_by_role("textbox", name="your@email.com")
        self.pw_input = page.get_by_role("textbox", name="비밀번호")
        self.login_submit_btn = page.get_by_role("button", name="로그인")
        self.auth_code_input = page.get_by_role("textbox", name="인증코드")
        self.validity_check = page.locator("span[class*='text-field_validity']")
        self.verify_code_btn = page.get_by_role("button", name="인증코드 확인")
        self.modal_confirm_btn = page.get_by_role("dialog").get_by_role("button", name="확인", exact=True)

    # ==================================================
    # [2. 커뮤니티 화면 요소]
    # ==================================================
        self.community_find = page.get_by_role("button").filter(has_text="커뮤니티 찾기")
        self.artist_search = page.get_by_role("textbox", name="search")
        self.artist_btn = page.get_by_role("link", name="aespa 카리나 지젤 윈터 닝닝")
        self.join_btn = page.get_by_role("button", name="가입하기").first
        self.modal_join_btn = page.get_by_label("wev3 modal").locator("button").filter(has_text="가입하기")
        self.post_link = page.locator("span.placeholder-_-wrap.placeholder-_--avatar")

    # ==================================================
    # [3. 포스트 등록 / 수정 / 삭제 요소]
    # ==================================================
        self.post_creation_btn = page.locator(
            ".avatar-_-image_wrap.avatar-_--outline.avatar-_--circle.avatar-_--icon_small > .avatar-_-image_area"
            )
        self.post_content_input = page.get_by_label("false")
        self.attach_photo_label = page.get_by_label("attach photo", exact=True)
        self.more_btn = page.get_by_role("button", name="more", exact=True)
        self.edit_btn = page.get_by_role("button", name="수정하기 수정하기", exact=True)
        self.delete_image_btn = page.locator("button").filter(has_text="delete image")
        self.message_edit_btn = page.get_by_label("false")
        self.attach_video_label = page.get_by_label("attach video", exact=True)
        self.delete_post_btn = page.get_by_role("button", name="삭제하기 삭제하기", exact=True)
        self.delete_confirm_btn = page.locator("button").filter(has_text="확인")
        self.no_post_message = page.get_by_text("아직 작성한 포스트가 없습니다")
        
        # 사진 및 동영상 첨부 시 확인 및 등록 버튼(중복되는 요소로 별도 정의)
        self.action_confirm_btn = page.get_by_text("확인")
        self.register_submit_btn = page.locator("button").filter(has_text="등록")

    # ==================================================
    # [4. 포스팅 등록, 수정, 삭제 로직 메서드]
    # ==================================================
    def login(self, email, password):
        self.page.goto("https://weverse.io/")
        self.login_btn.click()
        self.email_login_start_btn.click()
        self.email_input.fill(email)
        self.pw_input.fill(password)
        self.login_submit_btn.click()
        self.auth_code_input.click()
        self.validity_check.wait_for(state="visible", timeout=0)
        self.verify_code_btn.click()
        self.modal_confirm_btn.click()

    def enter_and_join_community(self):
        self.community_find.click()
        self.artist_search.click()
        self.artist_search.fill("aespa")
        self.artist_btn.click()
        self.join_btn.click()
        self.modal_join_btn.click()
        self.post_link.click()

    def write_post_with_image(self, text, file_path):
        self.post_creation_btn.click()
        self.post_content_input.fill(text)
        self.attach_photo_label.set_input_files(file_path)
        self.action_confirm_btn.click()
        self.register_submit_btn.click()

    def modify_post_with_video(self, new_text, video_path):
        self.page.wait_for_timeout(2000)
        self.more_btn.click()
        self.edit_btn.click()
        self.delete_image_btn.click()
        self.post_content_input.fill(new_text)
        self.attach_video_label.set_input_files(video_path)
        self.action_confirm_btn.click()
        self.register_submit_btn.click()

    def remove_post(self):
        self.page.wait_for_timeout(2000)
        self.more_btn.click()
        self.delete_post_btn.click()
        self.delete_confirm_btn.click()