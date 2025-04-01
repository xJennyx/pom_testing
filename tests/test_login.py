from time import sleep
import pytest
from pages.customer_login import CustomerLogin


@pytest.mark.smoke
def test_incorrect_login(login_page):
    sleep(10)
    login_page.open_page()
    login_page.fill_login_form('asdasd@dsfs.com', 'ads3sttt5e5e34ad')
    sleep(5)
    login_page.check_error_alert_text_is(
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    )

