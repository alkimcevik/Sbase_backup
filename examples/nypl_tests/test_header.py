#from test.s_base.pages.header_page import Header
from examples.nypl_pages.header_page import Header


class HeaderTest(Header):

    # https://www.nypl.org/

    # todo: add Login functionality

    def setUp(self):
        super().setUp()
        print("\nRUNNING BEFORE EACH TEST")

        # open blog page
        self.open_home_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        super().tearDown()

    def test_header_page(self):
        # assert NYPL LOGO
        self.assert_element(self.lion_logo)

        # assert LOGIN tab
        self.assert_element_present(self.login)
        self.click(self.login)
        self.assert_element(self.login_close)

        # assert LOCATIONS tab
        self.assert_element(self.locations)
        self.click(self.locations)
        self.assert_true(self.get_current_url() == 'https://www.nypl.org/locations')
        self.go_back()

        # assert GET A LIBRARY CARD tab
        self.assert_element(self.get_a_library_card)
        self.click(self.get_a_library_card)
        self.assert_true(self.get_current_url() == 'https://www.nypl.org/library-card')
        self.go_back()

        # assert GET EMAIL UPDATES tab
        self.assert_element(self.get_email_updates)
        self.click(self.get_email_updates)
        self.assert_title(self.get_email_updates_page_title)
        self.go_back()

        # assert DONATE tab
        self.assert_element(Header.donate)
        self.click(self.donate)
        self.assert_true("Donation" in self.get_current_url())
        self.go_back()

        # assert SHOP tab
        self.assert_element(self.shop)
        self.click(self.shop)
        self.assert_title(self.shop_page_title)
        self.go_back()

        # assert Books/Music/Movies
        self.assert_element(self.books_music_movies)
        self.click(self.books_music_movies)
        self.assert_title(self.books_music_movies_title)
        self.go_back()

        # assert Research
        self.assert_element(self.research)
        self.click(self.research)
        self.assert_title(self.research_title)
        self.go_back()

        # assert Education
        self.assert_element(self.education)
        self.click(self.education)
        self.assert_title(self.education_title)
        self.go_back()

        # assert Events
        self.assert_element(self.events)
        self.click(self.events)
        self.assert_title(self.events_title)
        self.go_back()

        # assert Connect
        self.assert_element(self.connect)
        self.click(self.connect)
        self.assert_title(self.connect_title)
        self.go_back()

        # assert Give
        self.assert_element(self.give)
        self.click(self.give)
        self.assert_title(self.give_title)
        self.go_back()

        # assert Get Help
        self.assert_element(self.get_help)
        self.click(self.get_help)
        self.assert_title(self.get_help_title)
        self.go_back()

        # assert Search
        self.assert_element(self.search)
        self.click(self.search)
        self.assert_text("Close")


