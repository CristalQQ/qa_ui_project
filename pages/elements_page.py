import os
import random
import shutil
import time

import requests
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablesPageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators
from config.links import ElementsPageLinks
from generator.generator import generated_person, generated_file


class TextBoxPage(BasePage):
    PAGE_URL = ElementsPageLinks.TEXT_BOX
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permananet_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permananet_address)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return full_name, email, current_address, permananet_address

    def check_filled_form(self):
        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permananet_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permananet_address


class CheckBoxPage(BasePage):
    PAGE_URL = ElementsPageLinks.CHECK_BOX
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEMS_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM).text
            data.append(title_item)
        return str(data).replace(" ", "").replace(".doc", "").lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = [result.text for result in result_list]
        return str(data).replace(" ", "").lower()


class RadioButtonPage(BasePage):
    PAGE_URL = ElementsPageLinks.RADIO_BUTTON
    locators = RadioButtonPageLocators()

    def click_yes_radio_button(self):
        self.element_is_visible(self.locators.YES_RADIO_ACTIVE).click()

    def click_impressive_radio_button(self):
        self.element_is_visible(self.locators.IMPRESSIVE_RADIO_ACTIVE).click()

    def click_no_radio_button(self):
        self.element_is_visible(self.locators.NO_RADIO_ACTIVE).click()

    def check_status_yes_radio_button(self):
        return self.element_is_present(self.locators.YES_RADIO_STATUS).is_selected()

    def check_status_impressive_radio_button(self):
        return self.element_is_present(self.locators.IMPRESSIVE_RADIO_STATUS).is_selected()

    def check_status_no_radio_button(self):
        return self.element_is_present(self.locators.NO_RADIO_STATUS).is_selected()


class WebTablesPage(BasePage):
    PAGE_URL = ElementsPageLinks.WEB_TABLES
    locators = WebTablesPageLocators()

    def add_new_person(self, count=1):
        added_persons = []
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(firstname)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.AGE).send_keys(age)
            self.element_is_visible(self.locators.SALARY).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

            new_person = [firstname, lastname, str(age), email, str(salary), department]
            added_persons.append(new_person)
            count -= 1
        return added_persons

    def check_new_added_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = [person.text.splitlines() for person in person_list]
        return data

    def search_some_person(self, key_word):
        search_field = self.element_is_visible(self.locators.SEARCH_FIELD)
        search_field.click()
        search_field.clear()
        search_field.send_keys(key_word)

    def check_search_person(self):
        return self.element_is_visible(self.locators.ROW_PERSON).text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        fields = {
            'firstname': person_info.firstname,
            'lastname': person_info.lastname,
            'age': person_info.age,
            'email': person_info.email,
            'salary': person_info.salary,
            'department': person_info.department
        }
        field_to_update = random.choice(list(fields.keys()))
        field_index = list(fields.keys()).index(field_to_update)

        self.element_is_visible(self.locators.UPDATE_BUTTON).click()

        if field_to_update == 'firstname':
            self.element_is_visible(self.locators.FIRST_NAME).clear()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(fields['firstname'])
        if field_to_update == 'lastname':
            self.element_is_visible(self.locators.LAST_NAME).clear()
            self.element_is_visible(self.locators.LAST_NAME).send_keys(fields['lastname'])
        if field_to_update == 'email':
            self.element_is_visible(self.locators.EMAIL).clear()
            self.element_is_visible(self.locators.EMAIL).send_keys(fields['email'])
        if field_to_update == 'age':
            self.element_is_visible(self.locators.AGE).clear()
            self.element_is_visible(self.locators.AGE).send_keys(fields['age'])
        if field_to_update == 'salary':
            self.element_is_visible(self.locators.SALARY).clear()
            self.element_is_visible(self.locators.SALARY).send_keys(fields['salary'])
        if field_to_update == 'department':
            self.element_is_visible(self.locators.DEPARTMENT).clear()
            self.element_is_visible(self.locators.DEPARTMENT).send_keys(fields['department'])
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return field_index, str(fields[field_to_update])

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_PERSON_BUTTON).click()

    def check_deleted(self):
        return self.element_is_visible(self.locators.NO_ROWS_FOUND).text

    def select_up_to_some_rows(self):
        data = []
        count_row_select = self.element_is_visible(self.locators.COUNT_ROW_LIST)
        dropdown = Select(count_row_select)
        all_options = dropdown.options
        for option in all_options:
            dropdown.select_by_index(all_options.index(option))
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)

    def add_20_rows_to_the_table(self):
        count_row_select = self.element_is_visible(self.locators.COUNT_ROW_LIST)
        dropdown = Select(count_row_select)
        dropdown.select_by_value('20')

class ButtonsPage(BasePage):
    PAGE_URL = ElementsPageLinks.BUTTONS
    locators = ButtonsPageLocators()

    def double_click_on_the_button(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_ME_BUTTON))

    def right_click_on_the_button(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_ME_BUTTON))

    def click_on_the_button(self):
        self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()

    def check_double_click_on_the_button(self):
        return self.element_is_present(self.locators.DOUBLE_CLICK_MESSAGE).text

    def check_right_click_on_the_button(self):
        return self.element_is_present(self.locators.RIGHT_CLICK_MESSAGE).text

    def check_click_on_the_button(self):
        return self.element_is_present(self.locators.CLICK_ME_MESSAGE).text


class LinksPage(BasePage):
    PAGE_URL = ElementsPageLinks.LINKS
    locators = LinksPageLocators()

    def click_on_the_home_link(self):
        self.element_is_visible(self.locators.HOME_LINK).click()

    def click_on_the_dynamic_link(self):
        self.element_is_visible(self.locators.DYNAMIC_HOME_LINK).click()

    def check_on_the_api_created(self):
        response = requests.get(ElementsPageLinks.API_CREATED)
        return response.status_code, response.reason

    def check_on_the_api_no_content(self):
        response = requests.get(ElementsPageLinks.API_NO_CONTENT)
        return response.status_code, response.reason

    def check_on_the_api_moved(self):
        response = requests.get(ElementsPageLinks.API_MOVED)
        return response.status_code, response.reason

    def check_on_the_api_bad_request(self):
        response = requests.get(ElementsPageLinks.API_BAD_REQUEST)
        return response.status_code, response.reason

    def check_on_the_api_unauthorized(self):
        response = requests.get(ElementsPageLinks.API_UNAUTHORIZED)
        return response.status_code, response.reason

    def check_on_the_api_forbidden(self):
        response = requests.get(ElementsPageLinks.API_FORBIDDEN)
        return response.status_code, response.reason

    def check_on_the_api_not_found(self):
        response = requests.get(ElementsPageLinks.API_NOT_FOUND)
        return response.status_code, response.reason


class UploadAndDownloadPage(BasePage):
    PAGE_URL = ElementsPageLinks.UPLOAD_AND_DOWNLOAD
    locators = UploadAndDownloadPageLocators()

    def create_download_dir(self):
        dir_path = os.path.join(os.getcwd(), "downloads")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def click_of_the_download_button(self):
        self.element_is_visible(self.locators.DOWNLOAD_BUTTON).click()
        time.sleep(1)

    def get_name_download_file(self):
        dir_path = os.path.join(os.getcwd(), "downloads")
        files = os.listdir(dir_path)
        return files[0]

    def delite_download_file(self):
        dir_path = os.path.join(os.getcwd(), "downloads")
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            shutil.rmtree(dir_path)

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_visible(self.locators.CHOOSE_FILE_BUTTON).send_keys(path)
        return file_name

    def getting_name_of_the_uploaded_file(self):
        file_path = self.element_is_visible(self.locators.UPLOADED_FILE_PATH).text
        return file_path.split('\\')[-1]


class DynamicPropertiesPage(BasePage):
    PAGE_URL = ElementsPageLinks.DYNAMIC_PROPERTIES
    locators = DynamicPropertiesPageLocators()

    def click_the_button_after_5_seconds(self):
        self.element_is_clickable(self.locators.WILL_ENABLE_5_SECONDS_BUTTON).click()

    def check_click_the_button_after_5_seconds(self):
        return self.element_is_visible(self.locators.WILL_ENABLE_5_SECONDS_BUTTON).is_enabled()

    def checking_for_button_color_changes(self):
        color_button = self.element_is_visible(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    def check_button_is_invisible(self):
        return self.elements_is_not_visible(self.locators.INVISIBLE_BUTTON)

    def check_button_is_visible(self):
        return self.element_is_visible(self.locators.INVISIBLE_BUTTON).is_displayed()
