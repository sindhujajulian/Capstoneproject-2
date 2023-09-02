import pytest
from test_utilities.login_page import Orangehrm


class TestCaseAdmin:

    def test_case_admin(self):
        """
        Test case to test header validation on Admin Page of OrangeHRM
        :return:
        """
        _expected_text = "Successful"
        validation_text = Orangehrm().admin_page()
        assert validation_text == _expected_text
        print("Header validation on admin page done successfully")
