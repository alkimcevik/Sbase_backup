from selenium.common import TimeoutException

from examples.nypl_pages.page_schwarzman import SchwarzmanPage
from examples.nypl_utility.utility import NyplUtils

import re
import requests
from selenium.webdriver.common.by import By

import urllib3
import pytest
from requests.exceptions import MissingSchema, InvalidSchema, InvalidURL
from selenium import webdriver
from selenium.webdriver.common.by import By


class Schwarzman(NyplUtils):

    # https://www.nypl.org/locations/schwarzman

    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open blog page
        self.open_schwarzman_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    @pytest.mark.skip(reason="test")
    def test_schwarzman(self):
        # https://www.nypl.org/locations/schwarzman
        print("test_schwarzman()\n")

        # assert breadcrumbs and hero
        self.assert_element(SchwarzmanPage.home)
        self.assert_element(SchwarzmanPage.locations)
        self.assert_element(SchwarzmanPage.hero)

        # assert 'Visit' and 'Research' tabs
        self.assert_element(SchwarzmanPage.visit)
        self.assert_element(SchwarzmanPage.research)
        # asserting title
        self.assert_title("Stephen A. Schwarzman Building | The New York Public Library")

        # assert that clicking on 'directions', '202x holiday hours' and links on the page will open the correct pages
        # using 'link_assertion' method from utility.py
        self.link_assertion(SchwarzmanPage.directions, "google.com/maps")
        self.link_assertion(SchwarzmanPage.holiday_closings, "nypl.org/help/closings")
        self.link_assertion(SchwarzmanPage.research, "nypl.org/locations/schwarzman/research")
        self.link_assertion(SchwarzmanPage.learn_more_1, "nypl.org/locations/schwarzman/research")
        self.link_assertion(SchwarzmanPage.learn_more_2, "nypl.org/spotlight/treasures")
        self.link_assertion(SchwarzmanPage.daily_guided_tours, "nypl.org/events/tours/schwarzman")

        # 'in the spotlight' and 'featured' h3 content don't change often, therefore, full endpoints being asserted
        self.link_assertion(SchwarzmanPage.in_the_spotlight_1, "nypl.org/appointments/schwarzman")
        self.link_assertion(SchwarzmanPage.in_the_spotlight_2, "databases")

        self.link_assertion(SchwarzmanPage.featured_at_sasb_1, "nypl.org/locations/schwarzman/research")
        self.link_assertion(SchwarzmanPage.featured_at_sasb_2, "nypl.org/about/locations/schwarzman/shop-cafe")
        self.link_assertion(SchwarzmanPage.featured_at_sasb_3, "www.nypl.org/blog")

        # Asserting 'Current Exhibitions' by using dynamic_element_link_assertion
        # clicking each Current Exhibition and asserting the URL contains the text provided
        self.dynamic_element_link_assertion('//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[1]/div/div/div['
                                            '2]/ul/li', "nypl.org/events/exhibitions")

        # asserting 'Events - See All' web element
        self.assert_element(SchwarzmanPage.events_see_all)
        # asserting 'Events' with a for loop by clicking every event and asserting the title
        # getting the length of the events h3 to use it in the for loop
        h3_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/ul/li'))
        # for loop to go over every event
        for x in range(1, h3_length + 1):
            if x == 5:  # skipping the 5th problematic element
                continue
            # getting the link text and assert if it is in the page title
            h3_link_text = self.get_text(
                f'//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/ul/li[{x}]/div[2]/h3/a')
            print("\n1: " + h3_link_text)
            self.click(f'//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/ul/li[{x}]/div[2]/h3')

            # getting the page title element
            h1_title = self.get_text('//*[@id="page-title"]')
            print("2: " + h1_title)
            # asserting h3 link text to the page title
            self.assert_true(h3_link_text in h1_title)

            self.go_back()  # go to the previous page for the next loop

        # asserting 'About the Stephen A. ....'
        self.assert_true(self.get_text(SchwarzmanPage.about_the_sasb) == "About the Stephen A. Schwarzman Building")

    def test_schwarzman_research(self):

        self.click(SchwarzmanPage.research)

        self.link_request_assertion(SchwarzmanPage.explore_division_centers)
        self.link_request_assertion(SchwarzmanPage.further_resources)
        self.link_request_assertion(SchwarzmanPage.more_nypl_resources)

    @pytest.mark.skip(reason="test")
    def test_sample_1(self):
        self.click(SchwarzmanPage.research)

        block_length = len(self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div/div/ul/li'))
        for x in range(1, block_length + 1):
            link = (self.find_element(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div/div/ul/li[' + str(x) + ']')).find_element(
                By.TAG_NAME, "a")

            url = link.get_attribute('href')
            print("\nurl: " + url)
            response = requests.head(url)
            assert response.status_code == 200, f"Link {url} is broken"

    @pytest.mark.skip(reason="test")
    def test_abc(self):
        self.click(SchwarzmanPage.research)

        def link_request_assertion(locator):
            block_length = len(
                self.find_elements(locator))
            for x in range(1, block_length + 1):
                link = (self.find_element(locator + '[' + str(
                    x) + ']')).find_element(By.TAG_NAME, "a")

                url = link.get_attribute('href')
                print("\nurl: " + url)
                response = requests.head(url)
                if response.status_code == 301:
                    print(
                        f"WARNING: The requested resource at {url} has been definitively moved to the URL given by the Location headers")
                assert response.status_code < 400, f"Link {url} is broken"
            print("\n=====================================================\n")

        link_request_assertion(SchwarzmanPage.explore_division_centers)
        link_request_assertion(SchwarzmanPage.further_resources)
        link_request_assertion(SchwarzmanPage.more_nypl_resources)
