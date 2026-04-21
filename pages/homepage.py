import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.checkin_input = (By.XPATH, "//label[normalize-space()='Check In']/../div/div/input")
        self.checkout_input = (By.XPATH, "//label[normalize-space()='Check Out']/../div/div/input")
        self.Check_Availability = (By.XPATH, "//button[normalize-space()='Check Availability']")
        self.Room_Options = (By.XPATH, "//div[@class='card h-100 shadow-sm room-card']")


    def enter_checkin_date(self, checkin_date):
        self.driver.find_element(*self.checkin_input).clear()
        self.driver.find_element(*self.checkin_input).send_keys(11 * Keys.BACKSPACE)
        self.driver.find_element(*self.checkin_input).send_keys(checkin_date)

    def enter_checkout_date(self, checkout_date):
        self.driver.find_element(*self.checkout_input).clear()
        self.driver.find_element(*self.checkout_input).send_keys(11 * Keys.BACKSPACE)
        self.driver.find_element(*self.checkout_input).send_keys(checkout_date)

    def click_check_availability(self):
        self.driver.find_element(*self.Check_Availability).click()

    def select_room(self, room_name):
        rooms = self.driver.find_elements(*self.Room_Options)

        for room in rooms:
            try:
                room_available = room.find_element(By.XPATH, "div/h5[@class='card-title']").text
                if room_available == room_name:
                    room.find_element(By.XPATH, "div/a").click()
                    break
            except NoSuchElementException:
                print("Room details not found in this card.")

    def checke_room_options(self):
        if len(self.driver.find_elements(*self.Room_Options)) > 0:
            return True
