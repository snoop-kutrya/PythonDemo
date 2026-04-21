from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utils.date_converter import convert_date_to_month
from utils.date_converter import date_fomat_converter
from utils.letters_and_numbers_separator import separat_letter_and_number


class ReservationPage:
    def __init__(self, driver):
        self.driver = driver
        self.RoomName = (By.XPATH, "//h1[@class='fw-bold mb-2']")
        self.calendar_label = (By.XPATH, "//span[@class='rbc-toolbar-label']")
        self.room_plus_night_price = (By.XPATH, "//div[@class='d-flex justify-content-between mb-2'][1]/span[2]")
        self.room_cleaning_fee = (By.XPATH, "//div[@class='d-flex justify-content-between mb-2'][2]/span[2]")
        self.room_sevice_fee = (By.XPATH, "//div[@class='d-flex justify-content-between'][1]/span[2]")
        self.total_price = (By.XPATH, "//div[@class='d-flex justify-content-between fw-bold'][1]/span[2]")
        self.reserve_button = (By.XPATH, "//button[@id='doReservation']")
        self.first_name_input = (By.XPATH, "//input[@placeholder='Firstname']")
        self.last_name_input = (By.XPATH, "//input[@placeholder='Lastname']")
        self.email_input = (By.XPATH, "//input[@placeholder='Email']")
        self.phone_number_input = (By.XPATH, "//input[@placeholder='Phone']")
        self.confirmation_reserve_button = (By.XPATH, "//button[@class='btn btn-primary w-100 mb-3']")
        self.booking_confirmation_hader = (By.XPATH, "//h2[@class='card-title fs-4 fw-bold mb-3']")
        self.booking_confirmation_dates = (By.XPATH, "//p[@class='text-center pt-2']/strong")
        self.email_alert = (By.XPATH, "//div[@class='alert alert-danger']/ul/li")

    def get_room_name(self, room_name):
        name = self.driver.find_element(*self.RoomName).text
        return name


    def check_calendar_label(self, checkin_date):
        month = convert_date_to_month(checkin_date)
        label = self.driver.find_element(*self.calendar_label).text
        assert month + " " + "2026" in label

    def check_price_calculation(self):
        room_price_text = self.driver.find_element(*self.room_plus_night_price).text
        room_price = separat_letter_and_number(room_price_text)

        cleaning_fee_text = self.driver.find_element(*self.room_cleaning_fee).text
        cleaning_fee = separat_letter_and_number(cleaning_fee_text)

        service_fee_text = self.driver.find_element(*self.room_sevice_fee).text
        service_fee = separat_letter_and_number(service_fee_text)

        total_price_text = self.driver.find_element(*self.total_price).text
        total_price = separat_letter_and_number(total_price_text)

        calculated_total = room_price + cleaning_fee + service_fee

        assert total_price == calculated_total, "Values are equal!"

    def click_reserve_now(self):
        for i in range(100):
            try:
                element = self.driver.find_element(*self.reserve_button)

                if element.is_displayed():
                    element.click()
                    break  # stop loop after clicking

                else:
                    self.driver.execute_script("window.scrollBy(0, 500);")

            except Exception as e:
                print(f"An error occurred: {e}")

    def input_guest_details(self, first_name, last_name, email, phone_number):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.phone_number_input).send_keys(phone_number)

    def get_email_alert_message(self):
        alert_message = self.driver.find_element(*self.email_alert).text
        return alert_message

    def get_alert_message(self):
        alerts_message = self.driver.find_elements(*self.email_alert).text
        return alerts_message

    def click_confirm_reserve(self):
        self.driver.find_element(*self.confirmation_reserve_button).click()

    def check_confirmation_message(self, checkin_date, checkout_date):
        confirmation_message = self.driver.find_element(*self.booking_confirmation_hader).text
        assert "Booking Confirmed" in confirmation_message

        dates = self.driver.find_element(*self.booking_confirmation_dates).text
        final_dates = dates.split()
        assert date_fomat_converter(final_dates[0]) in checkin_date and date_fomat_converter(
            final_dates[2]) in checkout_date
