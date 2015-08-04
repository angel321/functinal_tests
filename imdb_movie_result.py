# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class ImdbTest(unittest.TestCase):
    def setUp(self):

        """ You can access the classes like this-
           webdriver.Firefox
           webdriver.FirefoxProfile
           webdriver.Chrome
           webdriver.ChromeOptions
           webdriver.Ie
           webdriver.Opera
           webdriver.PhantomJS
           webdriver.Remote
           webdriver.DesiredCapabilities
           webdriver.ActionChains
           webdriver.TouchActions
           webdriver.Proxy

        """

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def _get_page(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'sort')))

    def _assert_search_result(self):
        movieList = self.driver.find_elements_by_css_selector('.lister-list tr')
        assert len(movieList) > 1, 'No result found'

    # Returns at least one result for top page
    def test_top_result(self):
        self._get_page('http://www.imdb.com/chart/top')
        self._assert_search_result()

    # Returns at least one result for every option in the drop down pull on top page
    def test_top_sort_results(self):
        self._get_page('http://www.imdb.com/chart/top')

        select = Select(self.driver.find_element_by_name('sort'))

        sort_options = select.options
        for option in sort_options:
            select.select_by_index(sort_options.index(option))
            self._assert_search_result()

    def _get_another_page(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'results')))

    def _assert_search_result2(self):
        movieList2 = self.driver.find_elements_by_css_selector('.results tr')
        assert len(movieList2) > 1, 'No result found'

    # Returns at least one result for western page
    def test_western_result(self):
        self._get_another_page('http://www.imdb.com/genre/western?ref_=chttp_gnr_23')
        self._assert_search_result2()


if __name__ == '__main__':
    unittest.main()



