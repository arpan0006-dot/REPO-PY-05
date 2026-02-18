from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.ac = ActionChains(driver)

    def find_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element

    def find_elements(self, locator):
        elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
        return elements

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def select_radio_button(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        if not element.is_selected():
            element.click()

    def is_radio_selected(self, locator):
        element = self.find_element(locator)
        return element.is_selected()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def double_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.ac.double_click(element).perform()

    def move_to_element(self, locator):
        element = self.find_element(locator)
        self.ac.move_to_element(element).perform()

    def get_url(self, url):
        self.driver.get(url)

    def select_from_dropdown(self, locator, option, method="text"):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        select = Select(element)
        if method == "text":
            select.select_by_visible_text(option)
        elif method == "value":
            select.select_by_value(option)
        elif method == "index":
            select.select_by_index(int(option))

    def get_all_dropdown_options(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        select = Select(element)
        return [option.text for option in select.options]

    def handle_alert(self, action="accept", text=None):
        try:
            alert = self.wait.until(EC.alert_is_present())
            if text:
                alert.send_keys(text)

            if action == "accept":
                alert.accept()
            elif action == "dismiss":
                alert.dismiss()
            elif action == "get_text":
                return alert.text
        except TimeoutException:
            return None

    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.wait.until(EC.visibility_of_element_located(source_locator))
        target_element = self.wait.until(EC.visibility_of_element_located(target_locator))
        self.ac.drag_and_drop(source_element, target_element).perform()

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_by_amount(self, x, y):
        self.driver.execute_script(f"window.scrollBy({x}, {y});")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def get_window_handle(self):
        return self.driver.current_window_handle

    def get_all_window_handles(self):
        return self.driver.window_handles

    def switch_to_window_by_handle(self, handle):
        self.driver.switch_to.window(handle)

    def switch_to_window_by_title(self, title):
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                break

    def open_new_tab(self):
        self.driver.execute_script("window.open('');")

    def switch_to_new_window(self, current_handles):
        self.wait.until(EC.new_window_is_opened(current_handles))
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle not in current_handles:
                self.driver.switch_to.window(handle)
                break

    def close_current_tab_and_switch_back(self, original_handle):
        self.driver.close()
        self.driver.switch_to.window(original_handle)

    def switch_to_frame(self, locator):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def get_shadow_root(self, host_locator):
        host_element = self.wait.until(EC.presence_of_element_located(host_locator))
        return self.driver.execute_script("return arguments[0].shadowRoot", host_element)

    def find_element_in_shadow_root(self, host_locator, css_selector):
        shadow_root = self.get_shadow_root(host_locator)
        element_script = "return arguments[0].querySelector(arguments[1])"
        element = self.driver.execute_script(element_script, shadow_root, css_selector)
        if element:
            return element
        return None
