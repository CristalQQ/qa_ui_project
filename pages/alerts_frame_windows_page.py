from config.links import AlertsFrameWindowsPageLinks
from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    PAGE_URL = AlertsFrameWindowsPageLinks.BROWSER_WINDOWS
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        list_handles = self.get_list_windows_handles()
        self.switch_to_new_windows(list_handles[1])
        text_title = self.element_is_visible(self.locators.NEW_TAB_TEXT).text
        return text_title

    def check_opened_new_windows(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        list_handles = self.get_list_windows_handles()
        self.switch_to_new_windows(list_handles[1])
        text_title = self.element_is_visible(self.locators.NEW_TAB_TEXT).text
        return text_title


class AlertsPage(BasePage):
    PAGE_URL = AlertsFrameWindowsPageLinks.ALERTS
    locators = AlertsPageLocators()

    def check_button_to_see_alert(self):
        self.element_is_visible(self.locators.CLICK_BUTTON_TO_SEE_ALERT).click()
        alert = self.driver.switch_to.alert
        return alert.text

