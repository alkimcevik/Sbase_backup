from examples.nypl_pages.exhibitions_page import ExhibitionsPage
from random import randrange


class Exhibitions(ExhibitionsPage):
    # https://www.nypl.org/events/exhibitions
    # https://www.nypl.org/events/exhibitions/upcoming
    # https://www.nypl.org/events/exhibitions/past
    # https://www.nypl.org/events/exhibitions/archived-exhibition-resources
    # https://www.nypl.org/events/exhibitions/community-showcases
    # https://www.nypl.org/events/exhibitions/online
    # https://www.nypl.org/events/exhibitions/stonewall50

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open exhibitions page
        self.open_exhibitions_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_exhibitions_main_page_elements(self):
        # https://www.nypl.org/events/exhibitions
        print("test_exhibitions_main_page_elements()\n")

        # assert breadcrumbs and page elements
        self.assert_element(self.home)
        self.assert_element(self.events)
        self.assert_element(self.exhibitions_h1)
        self.assert_element(self.main_paragraph)
        self.assert_element(self.current_exhibitions)

        # asserting 'Current Exhibitions' list, and it is number of elements
        # current exhibition length
        curr_exh_list_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/div/div/div/ul/li'))
        print('Current exhibition amount is = ' + str(curr_exh_list_length))  # optional print
        # asserting the exhibition length is more than expected amount
        self.assert_true(curr_exh_list_length >= 5, "Current exhibition amount is not greater than 5")

        # asserting 'current exhibitions' in a for loop by clicking every exhibition
        # comparing each exhibition link text with the hero header on their own page
        for x in range(1, curr_exh_list_length + 1):
            exhibition_link_text = self.get_text(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/div/div/div/ul/li[' + str(
                    x) + ']/h3/a/span')
            print(exhibition_link_text)  # optional print
            self.click('//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/div/div/div/ul/li[' + str(x) + ']')
            # title_text = self.get_text(self.get_title())
            # print(title_text)  # optional print
            hero_header_text = self.get_text('//*[@id="block-content-hero-header"]/div/div[2]/div[1]/h1/span')
            print(hero_header_text)  # optional text
            self.assert_true(exhibition_link_text in hero_header_text,
                             "Exhibition Page title does not match Exhibition link text")
            self.go_back()

            # checking if the images on the exhibition links are present/visible
            self.assert_element_visible(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/div/div/div/ul/li[' + str(x) + ']/a/img')

        # asserting 'See All' for 'Coming Soon', 'Community Showcases', 'Online Exhibitions', 'Past Exhibitions'
        # As of June 2022, there is only 4 'see all' to assert, from 3 to 6
        for x in range(3, 7):
            self.click('//*[@id="block-nypl-emulsify-content"]/div/div/div[' + str(x) + ']/div[1]/div/a')
            self.go_back()

        # todo: might want to assert the exhibition dates for all kind of exhibitions, with regex
        # e.g. for coming soon, dates have to be in future, for past, dates has to be in the past

        # *****************************************
        # asserting 'Coming Soon' element
        self.assert_element(self.coming_soon)

        # getting the length of the list to use it in the for loop
        coming_soon_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/div[2]/div/div/div/ul/li'))
        # clicking each exhibition in 'Coming Soon' and asserting their own page
        for x in range(1, coming_soon_length + 1):
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

            # asserting images on the links/exhibitions
            self.is_element_visible(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/div[2]/div/div/div/ul/li[' + str(
                    x) + ']/a/img')

            # asserting 'Coming Soon' content
            coming_soon_link_text = self.get_text(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/div[2]/div/div/div/ul/li[' + str(
                    x) + ']/h3/a/span')
            print(coming_soon_link_text)
            self.click('//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/div[2]/div/div/div/ul/li[' + str(
                x) + ']/h3/a/span')
            coming_soon_hero_text = self.get_text('//*[@id="block-content-hero-header"]/div/div[2]/div[1]/h1/span')
            print(coming_soon_hero_text)
            self.assert_true(coming_soon_link_text in coming_soon_hero_text)
            self.go_back()

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

        # *****************************************

        # *****************************************
        # asserting 'Community Showcase' element
        self.assert_element(self.community_showcase)

        # getting the length of the list to use it in the for loop
        community_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div[4]/div[2]/div/div/ul/li'))
        # clicking each exhibition in 'Community Showcases' and asserting their own page
        for x in range(1, community_length + 1):
            # asserting images on the links/exhibitions
            self.is_element_visible(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[4]/div[2]/div/div/ul/li[' + str(
                    x) + ']/a/figure/img')

            # asserting 'Community Showcases' content
            community_showcase_link_text = self.get_text(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[4]/div[2]/div/div/ul/li[' + str(
                    x) + ']/h3/a/span')
            print(community_showcase_link_text)
            self.click(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[4]/div[2]/div/div/ul/li[' + str(
                    x) + ']/h3/a/span')
            community_showcase_hero_text = self.get_text(
                '//*[@id="block-nypl-emulsify-content"]/div/div[1]/h1/span')
            print(community_showcase_hero_text)
            self.assert_true(community_showcase_link_text in community_showcase_hero_text)
            self.go_back()

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

        # *****************************************

        # *****************************************
        # asserting 'Online Exhibitions' element
        self.assert_element(self.online_exhibitions)

        # getting the length of the list to use it in the for loop
        online_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div[5]/div[2]/div/div/div/ul/li'))
        # clicking each online exhibition in 'Online Exhibition' and asserting their own page
        for x in range(1, online_length + 1):
            # asserting images on the links/exhibitions
            self.is_element_visible(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[5]/div[2]/div/div/div/ul/li[' + str(
                    x) + ']/a/img')

            # asserting 'online only' is displayed
            exhibition_text = self.get_text(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[5]/div[2]/div/div/div/ul/li[' + str(x) + ']/div')
            self.assert_true("Online Only" in exhibition_text)

            # asserting 'Online Exhibition' content
            online_exhibition_link_text = self.get_text(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[5]/div[2]/div/div/div/ul/li[' + str(
                    x) + ']/h3/a/span')
            print(online_exhibition_link_text)
            self.click(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[5]/div[2]/div/div/div/ul/li[' + str(
                    x) + ']/h3/a/span')
            online_exhibition_hero_text = self.get_text('//*[@id="block-content-hero-header"]/div/div[2]/div[1]')
            print(online_exhibition_hero_text)
            self.assert_true(online_exhibition_link_text in online_exhibition_hero_text)
            self.go_back()

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

        # *****************************************

        # *****************************************
        # asserting 'Past Exhibitions' element
        self.assert_element(self.past_exhibitions)

        # asserting 'Past Exhibitions' grid
        # getting the length for the for loop
        past_exh_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/ul/div'))

        print("URL before the loop")
        print(self.get_current_url())
        for x in range(1, past_exh_length + 1):
            # asserting the images
            self.is_element_visible(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/ul/div[' + str(x) + ']/a/img')
            # asserting the 'past exhibitions' (3 of them as May 2022)
            self.click('//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/ul/div[' + str(x) + ']/div/a')
            self.go_back()

            # asserting 'Past Exhibitions' content
            past_exhibitions_link_text = self.get_text(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/ul/div[' + str(
                    x) + ']/div/a/h3/span')
            print(past_exhibitions_link_text)
            self.click(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/ul/div[' + str(x) + ']/div/a')
            print(self.get_current_url())
            past_exhibitions_hero_text = self.get_text('//*[@id="block-content-hero-header"]/div/div[2]/div[1]/h1/span')
            print(past_exhibitions_hero_text)
            self.assert_true(past_exhibitions_link_text in past_exhibitions_hero_text)
            self.go_back()

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    def test_exhibitions_upcoming(self):
        # https://www.nypl.org/events/exhibitions/upcoming
        print("test_exhibitions_upcoming()\n")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/events/exhibitions/upcoming")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/events/exhibitions/upcoming")

        # assert breadcrumbs and page elements
        self.assert_element(self.home)
        self.assert_element(self.events)
        self.assert_element(self.exhibitions)
        self.assert_element(self.upcoming_exhibitions_h1)
        self.assert_element(self.header_paragraph)

        # *****************************************

        # getting the length of the list to use it in the for loop
        exhibition_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div/li'))
        # clicking each exhibition and asserting their own page
        for x in range(1, exhibition_length + 1):
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

            # asserting images on the links/exhibitions
            self.is_element_visible(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div/li[' + str(x) + ']/a/img')

            # asserting exhibition contents
            exhibition_link_text = self.get_text(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div/li[' + str(x) + ']/h3/a/span')
            print(exhibition_link_text)
            self.click('//*[@id="block-nypl-emulsify-content"]/div/div/div/li[' + str(x) + ']/h3/a/span')
            exhibition_hero_text = self.get_text('//*[@id="block-content-hero-header"]/div/div[2]/div[1]/h1/span')
            print(exhibition_hero_text)
            self.assert_true(exhibition_link_text in exhibition_hero_text)
            self.go_back()

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    def test_exhibitions_past(self):
        # https://www.nypl.org/events/exhibitions/past
        print("test_exhibitions_past()\n")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/events/exhibitions/past")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/events/exhibitions/past")

        # assert breadcrumbs and page elements
        self.assert_element(self.home)
        self.assert_element(self.events)
        self.assert_element(self.exhibitions)
        self.assert_element(self.past_exhibitions_h1)

        # asserting the forward button > and ellipsis '...'
        self.assert_element(self.right_icon)
        self.assert_element(self.ellipsis_2)

        # *****************************************

        # getting the length of the list to use it in the for loop
        exhibition_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div/ul/li'))
        # clicking each exhibition and asserting their own page
        for x in range(1, exhibition_length + 1):
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

            # asserting images on the links/exhibitions
            self.is_element_visible(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div/ul/li[' + str(x) + ']/a/img')

            # asserting exhibition contents
            exhibition_link_text = self.get_text(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div/ul/li[' + str(x) + ']/h3/a/span')
            print(exhibition_link_text)
            self.click('//*[@id="block-nypl-emulsify-content"]/div/div/div/ul/li[' + str(x) + ']/h3/a/span')
            exhibition_hero_text = self.get_text('//*[@id="block-content-hero-header"]/div/div[2]/div[1]/h1/span')
            print(exhibition_hero_text)
            self.assert_true(exhibition_link_text in exhibition_hero_text)
            self.go_back()

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

        # asserting the pager links at the bottom of the page
        pager_length = 9  # as of June 2022

        for x in range(1, pager_length + 1):
            self.click('//*[@id="block-nypl-emulsify-content"]/div/div/nav/ul/li[' + str(x) + ']/a')
            url_text = self.get_current_url()
            print(url_text)  # optional print  # optional print
            # asserting if the url text contains page=random_number
            self.assert_true('page=' + str(x - 1) in url_text)
            print('page=' + str(x - 1))
            self.go_back()

    def test_exhibitions_archived_exhibition_resources(self):
        # https://www.nypl.org/events/exhibitions/archived-exhibition-resources
        print("test_exhibitions_archived_exhibition_resources()\n")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/events/exhibitions/archived-exhibition-resources")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/events/exhibitions/archived-exhibition-resources")

        # assert breadcrumbs and page elements
        self.assert_element(self.home)
        self.assert_element(self.events)
        self.assert_element(self.exhibitions)
        self.assert_element(self.archived_h1)
        self.assert_element(self.archived_parag)
        self.assert_element(self.archived_h2)

        # asserting the forward button > and ellipsis '...'
        self.assert_element(self.right_icon_2)

        # *****************************************

        # getting the length of the list to use it in the for loop
        exhibition_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/div/div/ul/li'))
        # clicking each exhibition and asserting their own page
        for x in range(1, exhibition_length + 1):
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

            # asserting images on the links/exhibitions
            self.is_element_visible(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/div/div/ul/li[' + str(
                    x) + ']/a/figure/img')

            # asserting exhibition headings/link-texts
            exhibition_link_text = self.get_text(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/div/div/ul/li[' + str(x) + ']/div/h3/a')
            print(exhibition_link_text)
            self.click(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/div/div/ul/li[' + str(x) + ']/div/h3/a')
            self.go_back()
            # asserting the content
            self.click('//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/div/div/ul/li[' + str(x) + ']/div')
            exhibition_hero_text = self.get_text('//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div['
                                                 '2]/div/div/ul/li[1]/div/div/p')

        # asserting the pager links at the bottom of the page
        pagination_length = int(str(len(
            self.find_elements(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/div/div/nav/ul/li')) - 1))
        # print(pagination_length)  # optional print of the page numbers at the bottom

        for x in range(1, pagination_length + 1):
            self.click(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/div/div/nav/ul/li[' + str(x) + ']/a')
            url_text = self.get_current_url()
            print(url_text)  # optional print  # optional print
            # asserting if the url text contains page=random_number
            self.assert_true('page=' + str(x - 1) in url_text)
            print('page=' + str(x - 1))
            self.go_back()

        # asserting right-icon
        self.assert_element(self.right_icon_3)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    def test_exhibitions_community_showcases(self):
        # https://www.nypl.org/events/exhibitions/archived-exhibition-resources
        print("test_exhibitions_community_showcases()\n")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/events/exhibitions/community-showcases")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/events/exhibitions/community-showcases")

        # assert breadcrumbs and page elements
        self.assert_element(self.home)
        self.assert_element(self.events)
        self.assert_element(self.exhibitions)
        self.assert_element(self.community_h1)
        self.assert_element(self.community_parag)

        # asserting the list of exhibitions
        exhibition_list_length = len(self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div['
                                                        '2]/div/div/div/ul/li'))
        print("Exhibition list length is " + str(exhibition_list_length))

        for x in range(1, exhibition_list_length + 1):
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

            # asserting images on the links/exhibitions
            self.is_element_visible(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div/ul/li[' + str(x) + ']/a/img')

            # asserting exhibition contents
            exhibition_link_text = self.get_text(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div/div/div/ul/li[' + str(x) + ']/h3/a/span')
            print(exhibition_link_text)
            self.click(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div/div/div/ul/li[' + str(x) + ']/h3/a/span')
            exhibition_hero_text = self.get_text('//*[@id="block-nypl-emulsify-content"]/div/div[1]/h1/span')
            print(exhibition_hero_text)
            self.assert_true(exhibition_link_text in exhibition_hero_text)
            self.go_back()

        # asserting the pager links at the bottom of the page
        pagination_length = int(str(len(
            self.find_elements(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div/div/div/nav/ul/li')) - 1))
        print("\nPage amount on the default page is " + str(
            pagination_length))  # optional print of the page numbers at the bottom

        for x in range(1, pagination_length + 1):
            self.click(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div/div/div/nav/ul/li[' + str(x) + ']/a')
            url_text = self.get_current_url()
            print(url_text)  # optional print  # optional print
            # asserting if the url text contains page=random_number
            self.assert_true('page=' + str(x - 1) in url_text)
            print('page=' + str(x - 1))
            self.go_back()

        # asserting right-icon
        self.assert_element(self.right_icon_4)

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    def test_exhibitions_online(self):
        # https://www.nypl.org/events/exhibitions/online
        print("test_exhibitions_online()\n")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/events/exhibitions/online")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/events/exhibitions/online")

        # assert breadcrumbs and page elements
        self.assert_element(self.home)
        self.assert_element(self.events)
        self.assert_element(self.exhibitions)
        self.assert_element(self.online_h1)

        # asserting the exhibition list

        # length of the list
        exhibition_list_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div/div/div/div/div/ul/li'))
        print("Exhibition list length is " + str(exhibition_list_length))

        # for loop to go over all the list elements
        for x in range(1, exhibition_list_length + 1):
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

            # asserting images on the links/exhibitions
            self.is_element_visible(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div/div/div/div/div/ul/li[' + str(x) + ']/a/img')

            # asserting exhibition contents
            # asserting 'Online Only' text
            online_text = self.get_text('//*[@id="block-nypl-emulsify-content"]/div/div/div/div/div/div/div/ul/li[' + str(x) + ']/div')
            self.assert_true("Online Only" in online_text, "Online Only does not show up in the exhibition")
            # asserting the link text and the hero text on the next page when clicked
            exhibition_link_text = self.get_text('//*[@id="block-nypl-emulsify-content"]/div/div/div/div/div/div/div'
                                                 '/ul/li[' + str(x) + ']/h3/a/span')
            print(exhibition_link_text)
            self.click(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div/div/div/div/div/ul/li[' + str(x) + ']/h3/a/span')
            exhibition_hero_text = self.get_text('//*[@id="block-content-hero-header"]/div/div[2]/div[1]/h1/span')
            print(exhibition_hero_text)
            self.assert_true(exhibition_link_text in exhibition_hero_text, 'link text ' + exhibition_link_text + 'not '
                                                                                                                 'found in hero text ' + exhibition_hero_text)
            self.go_back()

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

