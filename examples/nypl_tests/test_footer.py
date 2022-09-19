#from test.s_base.pages.footer_page import Footer
from examples.nypl_pages.footer_page import Footer


class FooterTest(Footer):

    # https://www.nypl.org/

    def setUp(self):
        super().setUp()
        print("\nRUNNING BEFORE EACH TEST")

        # open blog page
        self.open_home_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        super().tearDown()

    def test_footer(self):
        # assert nypl logo
        self.assert_element(self.nypl_logo)
        # assert main building image
        self.assert_element(self.main_building_image)

        # assert links
        links_list = ["accessibility", "press", "careers", "space_rental", "privacy_policy"
            , "other_policies", "terms_conditions", "governance", "rules_regulations"
            , "about_nypl", "language"]

        # print(self.dic["press"])
        # self.assert_element(self.dic[0])

        x = 0
        while x < len(links_list):
            self.assert_element(self.footer_links_dic["" + links_list[x] + ""])
            print(self.assert_element(self.footer_links_dic["" + links_list[x] + ""])
                  )
            x += 1

        # social media assertions
        social_media = ["facebook", "twitter", "instagram", "youtube"]

        self.wait(2)
        self.assert_element(self.facebook)
        self.click(self.facebook)
        self.wait(2)
        print(self.get_current_url())
        self.assert_true("facebook" in self.get_current_url())
        self.go_back()
        self.wait(2)

        self.assert_element(self.twitter)
        self.click(self.twitter)
        self.assert_true('twitter' in self.get_current_url())
        self.go_back()
        self.wait(2)

        self.assert_element(self.instagram)
        self.click(self.instagram)
        self.assert_true('instagram' in self.get_current_url())
        self.go_back()
        self.wait(2)

        self.assert_element(self.youtube)
        self.click(self.youtube)
        self.assert_true('youtube' in self.get_current_url())
        self.go_back()
