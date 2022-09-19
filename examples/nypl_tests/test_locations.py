#from test.s_base.pages.locations_page import LocationsPage
from examples.nypl_pages.locations_page import LocationsPage
from random import randrange
import time


class Locations(LocationsPage):
    # https://www.nypl.org/locations

    def setUp(self):
        super().setUp()
        print("\nRUNNING BEFORE EACH TEST")

        # open locations page
        self.open_locations_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        super().tearDown()

    def test_main_page_elements(self):
        # assert page elements
        self.assert_element(self.locations)
        self.assert_element(self.welcome_text)
        self.assert_element(self.find_your_library)
        self.assert_element(self.search_text)
        self.assert_element(self.search)
        self.assert_element(self.open_now)
        self.assert_element(self.filters)
        self.assert_element(self.research_filters)

        # asserting 'Clear all search terms' Web-element
        self.click(self.borough)
        self.click(self.bronx)
        self.click(self.apply_boro)
        self.assert_element(self.clear_all_search)
        self.click(self.borough)
        self.click(self.clear_boro)

        # assert if the 'Open now' check box works by...
        # ...comparing the total number of libraries vs open libraries
        total_library_number = len(self.find_elements('//*[@id="locations-list"]/div/ul/li'))
        self.click(self.open_now)
        open_library_number = len(self.find_elements('//*[@id="locations-list"]/div[2]/ul/li'))
        time.sleep(3)
        self.wait_for_element('//*[@id="locations-list"]/div[2]/ul/li')
        print("total library number = " + str(total_library_number),
              "open library number = " + str(open_library_number))
        self.assert_true(total_library_number > open_library_number)

        # clear all search terms
        self.click(self.clear_all_search)
        self.check_if_unchecked(self.open_now_check_box)
        self.assert_true(total_library_number > open_library_number)

        # map iframe, switch to iframe
        self.switch_to_frame('//*[@id="locations-gmap"]/div[2]/div[1]/div/div/iframe')
        self.switch_to_default_content()

        # lower page elements
        # 2 locations assertion and BK and Queens web-elements. Checking if the web-elements exist
        self.assert_element('/html/body/div[1]/div/div[2]/main/div[2]/div[2]/div[1]/div/div[1]/div/div['
                            '1]/a/figure/figcaption/div')
        self.assert_element(
            '//*[@id="main-content"]/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/a/figure/figcaption/div')
        self.assert_element('//*[@id="main-content"]/div[2]/div[2]/div[1]/div/div[2]')

    def test_borough(self):
        self.assert_element(self.borough)

        # assert bronx for a random(randrange(1, 35)) location
        self.click(self.borough)
        self.click(self.bronx)
        self.click(self.apply_boro)

        print(self.get_text('//*[@id="locations-list"]/div[2]/ul/li[' + str(randrange(1, 35)) + ']/div/div[1]'))
        self.assert_true("Bronx" in self.get_text(self.bronx_location))
        self.click(self.borough)
        self.click(self.clear_boro)

        # assert manhattan for a random(randrange(1, 76)) location
        self.click(self.borough)
        self.click(self.manhattan)
        self.click(self.apply_boro)

        print(self.get_text('//*[@id="locations-list"]/div[2]/ul/li[' + str(randrange(1, 76)) + ']/div/div[1]'))
        self.assert_true("New York" in self.get_text(self.manhattan_location))
        self.click(self.borough)
        self.click(self.clear_boro)

        # assert Staten Island for a random(randrange(1, 14)) location
        self.click(self.borough)
        self.click(self.richmond)
        self.click(self.apply_boro)

        print(self.get_text('//*[@id="locations-list"]/div[2]/ul/li[' + str(randrange(1, 14)) + ']/div/div[1]'))
        self.assert_true("Staten" in self.get_text(self.richmond_location))
        self.click(self.borough)
        self.click(self.clear_boro)

    def test_accessibility(self):
        # assert "Full Accessibility"
        self.assert_(self.accessibility)

        # assert fully access
        self.click(self.accessibility)
        self.click(self.full_access)
        self.click(self.apply_access)
        time.sleep(3)

        # total number of libraries with full accessibility
        total_lib = len(self.find_elements('//*[@id="locations-list"]/div[2]/ul/li'))
        print("Total fully accessible library number is " + str(total_lib))

        # for loop to iterate locations and find the ones without "Fully Accessible" text
        count = 0  # count = libraries that don't have accessibility
        for x in range(1, total_lib + 1):
            y = [6, 7, 11, 14, 16, 19, 23, 25, 29, 32, 33, 40, 46, 47, 50, 53, 55, 56, 58, 65, 68, 73, 75, 76,
                 77, 78, 79, 87, 93, 94, 96, 97, 98]
            if x in y:
                text = self.get_text('//*[@id="locations-list"]/div[2]/ul/li[' + str(x) + ']/div/div[4]/div[2]')
                if 'Fully Accessible' in text:
                    continue
                else:
                    print(
                        self.get_text('/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div/div[1]/div[2]/ul/li[' + str(
                            x) + ']/div/h2/a'))
                    count += 1

            text = self.get_text('//*[@id="locations-list"]/div[2]/ul/li[' + str(x) + ']/div/div[3]/div[2]')
            if 'Fully Accessible' in text:
                continue
            else:
                print(self.get_text('/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div/div[1]/div[2]/ul/li[' + str(
                    x) + ']/div/h2/a'))
                count += 1
        print(str(count) + " libraries don't have full access yet listed on the 'Fully Accessible' filter")
        self.assert_(count < 1)

    def test_partial_accessibility(self):
        # assert "Partially Accessibility"
        self.assert_(self.accessibility)

        # assert partial access
        self.click(self.accessibility)
        self.click(self.partial_access)
        self.click(self.apply_access)
        time.sleep(1)

        # total number of libraries with partial accessibility
        total_partial_lib = len(self.find_elements('//*[@id="locations-list"]/div[2]/ul/li'))
        print(total_partial_lib)

        # for loop to assert locations have "partially accessible" text
        count = 0
        for x in range(1, total_partial_lib + 1):
            text = self.get_text('//*[@id="locations-list"]/div[2]/ul/li[' + str(x) + ']/div/div[3]/div[2]')
            print(text)
            self.assert_("Partially Accessible" in text)
            count += 1
        print(str(count) + " libraries with Partial Accessibility")

    # TODO: finish this after the bug fixed for
    #  https://jira.nypl.org/browse/RENO-2961
    '''
    def test_not_accessible(self):
        # TODO: finish this after the bug fixed for
        #  https://jira.nypl.org/browse/RENO-2961
        self.click(self.accessibility)
        self.click(self.not_access)
        self.click(self.apply_access)
        time.sleep(1)

        # fill the locator after the bugs fixed
        total_no_access_lib = len(self.find_elements(' "li" locator here'))
        print(total_no_access_lib)

        count = 0
        for x in range(1, total_no_access_lib + 1):
            text = self.get_text('no access locator here' + str(x) + ' and here')
            print(text)
            self.assert_("Not Accessible" in text)
            count += 1
        print(str(count) + " libraries with No Accessibility")
        
    '''

    def test_amenities(self):
        # assert amenities
        self.assert_(self.amenities)

        # assert 'amenities' length, which is 42 as of June 2022
        amenities_len = len(self.find_elements('/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/form/div['
                                               '2]/div[2]/div[1]/div/div[3]/div/div/div[1]/ul/li'))

        self.assert_true(amenities_len > 10, "amenities filter smaller than expected")

    def test_subject_specialties(self):
        # assert subject_specialties
        self.assert_(self.subject_specialties)

        # assert 'art' filter number
        self.click(self.subject_specialties)
        self.click(self.art)
        self.click(self.apply_specialties)

        # length of the filter == 10 aas of June 2022
        art_filter_len = len(self.find_elements('/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div/div[1]/div['
                                                '2]/ul/li'))

        # assert art filter length is larger than 8
        print("Art filter length is " + str(art_filter_len))
        self.assert_true(art_filter_len > 8)

        self.click(self.subject_specialties)
        self.click(self.clear_specialties)

        # assert history filter
        self.click(self.subject_specialties)
        self.click(self.history)
        self.click(self.apply_specialties)

        history_filter_len = len(self.find_elements('/html/body/div[1]/div/div[2]/main/div[1]/div['
                                                    '2]/div/div/form/div[2]/div[2]/div[2]/div/div[1]/div/div/div['
                                                    '1]/ul/li'))

        # assert history filter length greater than 8, currently 11 as of June 2022
        self.assert_true(history_filter_len > 8)
        print("History filter length is " + str(history_filter_len))
        self.click(self.subject_specialties)
        self.click(self.clear_specialties)

        # assert social sciences filter
        self.click(self.subject_specialties)
        self.assert_(self.social_sciences)

        # length of the filter
        social_length = len(self.find_elements('/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/form/div[2]/div[2]/div[2]/div/div[1]/div/div/div[1]/ul/li'))

        # assert social sciences length, as of June 2022 it is 10
        print("Social Sciences length is " + str(social_length))
        self.assert_true(social_length > 8)
        self.click(self.clear_specialties)

    def test_media_types(self):
        # assert media types button
        self.assert_(self.media_types)

        # assert 'Manuscripts and Archives Division' is listed after 'Archives' clicked
        self.click(self.media_types)
        self.click(self.archives)
        self.click(self.apply_media)
        self.assert_element('//*[@id="lid-manuscripts-division"]/a')

        # assert 'media types' filter length, as of June 2022 it is 13
        self.click(self.media_types)
        media_types_len = len(self.find_elements('//*[@id="search-form"]/div[2]/div[2]/div[2]/div/div[2]/div/div/div['
                                                 '1]/ul/li'))
        print("Media types length is " + str(media_types_len))
        self.assert_true(media_types_len > 10)
        self.click(self.clear_media)

    def test_open_hours(self):
        """
        //TODO ask John hours where to get the "open hours" of the library, e.g.
        https://d8.nypl.org/node/41/edit?destination=/admin/content/locations

        "John: They are affected by closings entered here. Math is done to subtract closed hours from open hours.
        https://d8.nypl.org/admin/content/callout-manager

        I don't think it would be worth your while to parse it. I'd maybe check it using regular expressions
        just to check if there is something valid there. it should be either "CLOSED" or "* AM–* PM" (edited)"
        :return:
        """


