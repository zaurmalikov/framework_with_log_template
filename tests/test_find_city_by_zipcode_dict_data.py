import pytest

from page_objects.main_page import MainPage
from test_data.test_data_dict import TestData
from utilities.base_class import BaseClass


class TestCase1(BaseClass):

    @pytest.fixture(params=TestData.test_data_values)  # this will pull data from mentioned dictionary in test data
    def value(self, request):
        return request.param

    def test_case_1(self, value):
        main_page = MainPage(self.driver)

        main_page.perform_some_action()
        #etc.......



