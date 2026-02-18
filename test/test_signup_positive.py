from pages.signup_page import SignupPage

def test_valid_signup(driver):
    page = SignupPage(driver)
    page.load()

    page.enter_first_name("John")
    page.enter_last_name("Doe")
    page.enter_email("john.unique123@test.com")
    page.enter_phone("9272128543")
    page.enter_password("StrongPwd@123")
    page.enter_confirm_password("StrongPwd@123")
    page.select_gender("male")
    page.accept_terms()
    page.click_signup()

    assert "Thank" in driver.page_source