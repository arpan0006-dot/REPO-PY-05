import pytest
from page.signup_page import SignupPage

@pytest.mark.parametrize("first, last, phone, email, gender, pwd, conf, accept_terms, expected_error", [
    ("", "", "", "", "", "", "", False, "Required fields"),
    ("John", "Doe", "1234", "john", "male", "pw", "pw", True, "Invalid email"),
    ("John", "Doe", "9876543210", "john.doe@example.com", "", "StrongPwd!1", "StrongPwd!1", True, "Select gender"),
    ("John", "Doe", "abcdef", "john.doe@example.com", "male", "StrongPwd!1", "StrongPwd!1", True, "Invalid phone"),
    ("John", "Doe", "9876543210", "john.doe@example.com", "female", "Pwd1", "Pwd2", True, "Passwords must match"),
    ("John", "Doe", "9876543210", "existing@mail.com", "male", "StrongPwd!1", "StrongPwd!1", True, "Email already in use"),
    ("John", "Doe", "9876543210", "test@mail.com", "female", "StrongPwd!1", "StrongPwd!1", False, "Please accept Terms"),
])
def test_signup_errors(driver, first, last, phone, email, gender, pwd, conf, accept_terms, expected_error):
    page = SignupPage(driver)
    page.load()
    page.fill_personal_details(first, last, phone, email)

    if gender:
        page.select_gender(gender)

    if pwd:
        page.fill_passwords(pwd, conf)

    if accept_terms:
        page.accept_terms()

    page.submit_form()

    errors = page.get_errors()
    assert any(expected_error in err for err in errors)
