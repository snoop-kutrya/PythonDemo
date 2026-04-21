import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.reservationpage import ReservationPage
from pages.homepage import HomePage
from conftest import browserinstance
from Tests.TestData import booking_with_invalid_email_format as TestData


checkin_date = TestData.checkindate
checkout_date = TestData.checkoutdate
room_name = TestData.roomname
first_name = TestData.first_name
last_name = TestData.last_name
email = TestData.email
phone_number = TestData.phone_number


# @pytest.mark.parametrize
def test_BookingWithInvalidEmailFormat(browserinstance):
    driver = browserinstance
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(2)

    home_page = HomePage(driver)
    home_page.enter_checkin_date(checkin_date)  # Pass the check-in date as a string
    home_page.enter_checkout_date(checkout_date)  # Pass the check-out date as a string
    time.sleep(2)

    home_page.click_check_availability()
    time.sleep(2)
    home_page.select_room(room_name)  # Pass the room name as a string
    time.sleep(2)

    reservation_page = ReservationPage(driver)
    time.sleep(2)
    name = reservation_page.get_room_name()
    assert name in room_name + " " + "Room"

    reservation_page.check_calendar_label(checkin_date)
    reservation_page.check_price_calculation()
    reservation_page.click_reserve_now()
    time.sleep(2)
    for i in range(6):
        reservation_page.input_guest_details(first_name, last_name, email[i], phone_number)  # pass first name, last name, email and phone number as strings
        time.sleep(2)
        reservation_page.click_confirm_reserve()
        message = reservation_page.get_email_alert_message()
        assert message == "must be a well-formed email address"
