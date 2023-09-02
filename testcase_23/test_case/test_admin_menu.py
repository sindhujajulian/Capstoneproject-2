import pytest
from test_utilities.login_page import Orangehrm


class TestCaseMenu:

    def test_tc_pim_03(self):
        """
        Test case to test main menu validation on admin page
        :return:
        """
        _expected_text = "Successful"
        validation_text = Orangehrm().admin_page_menu()
        assert validation_text == _expected_text
        print("Main menu validation on admin page is successful")