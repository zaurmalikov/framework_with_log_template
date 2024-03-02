import pytest

from page_objects.main_page import MainPage
from test_data.test_data_excel import TestDataExcel
from utilities.base_class import BaseClass


class TestCase2(BaseClass):

    @pytest.fixture(params=TestDataExcel.data_list)  # this will pull data from Excel file in test data
    def value(self, request):
        return request.param

    def test_case2(self, value):
        main_page = MainPage(self.driver)


