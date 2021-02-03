import pytest


def test_valid_crentials_login(vdc_driver):
    vdc_driver.get('https://www.saucedemo.com')

    vdc_driver.find_element_by_id('user-name').send_keys('standard_user')
    vdc_driver.find_element_by_id('password').send_keys('secret_sauce')
    vdc_driver.find_element_by_css_selector('.btn_action').click()

    assert "/nope.html" in vdc_driver.current_url
