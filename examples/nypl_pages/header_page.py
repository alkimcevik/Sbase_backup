from seleniumbase import BaseCase


class Header(BaseCase):
    lion_logo = '//*[@id="Logo"]'

    login = ".myNyplButton-wrapper"
    login_close = '//*[@id="nyplHeader"]/div[2]/div[2]/nav/ul/li[1]/div/a'
    locations = ".locationsTopLink"
    get_a_library_card = ".libraryCardButton"
    get_email_updates = ".subscribeButton-wrapper"
    get_email_updates_page_title = 'Subscription Center | The New York Public Library'
    donate = ".donateButton"
    donate_page_title = 'Make Your Tax-Deductible Gift Today - New York Public Library'
    shop = ".shopTopLink"
    shop_page_title = 'The New York Public Library Shop'

    books_music_movies = '//*[@id="navMenuItem-link-488afdf5-7a3c-4cee-8c89-1667be3032f7"]'
    books_music_movies_title = 'Books/Music/Movies | The New York Public Library'
    research = '//*[@id="navMenuItem-4a8ee293-2e42-4f3f-8f62-8ab9d11a688a"]'
    research_title = 'Research | The New York Public Library'
    education = '//*[@id="navMenuItem-17eb88cf-08cb-4b08-89bb-f835c3c032b1"]'
    education_title = 'Education | The New York Public Library'
    events = '//*[@id="navMenuItem-1a56e236-b251-477c-b87c-9b6588aad6b8"]'
    events_title = 'Events | The New York Public Library'
    connect = '//*[@id="navMenuItem-a77fd2d8-dc15-45b3-bee6-13e76375ffe8"]'
    connect_title = 'Connect | The New York Public Library'
    give_title = 'Give | The New York Public Library'
    give = '//*[@id="navMenuItem-793f73d4-0ed8-458e-87de-896bee17043c"]'
    get_help = '//*[@id="navMenuItem-link-ca639f96-6d00-4dd4-b0c4-33f1653f6b2c"]'
    get_help_title = 'Get Help | The New York Public Library'
    search = '//*[@id="header-navMenu-searchButton"]/span'

    def open_home_page(self):
        self.open("https://www.nypl.org/")