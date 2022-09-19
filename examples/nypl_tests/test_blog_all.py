from examples.nypl_pages.blog_all_page import BlogAllPage


class BlogAllTests(BlogAllPage):

    # https://www.nypl.org/blog/all

    def setUp(self):
        super().setUp()
        print("\nRUNNING BEFORE EACH TEST")

        # open blog page
        self.open_blog_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        super().tearDown()

    def test_page_elements(self):
        # assert Explore By:
        self.assert_element(self.explore_by)

    def test_channels(self):
        # asserting 'Channels' tab
        self.click(self.channels)
        self.wait_for_element(self.channels)
        self.assert_element(self.channels)
        print(self.get_attribute(self.channels, "Class"))
        self.wait_for_element(self.channels)
        self.wait_for_attribute(self.channels, "Class", "MultiSelect_menuButton__27biZ MultiSelect_active__zICuC")
        self.assert_attribute(self.channels, "Class", "MultiSelect_menuButton__27biZ MultiSelect_active__zICuC")

        # asserting channel categories
        # creating a list for Channel Filters
        li = ["asian_american", "biography", "black_culture", "book_lists", "comics_graphic", "digital_collections",
              "doc_chat", "early_literacy", "espanol_spanish", "for_kids", "for_teachers", "for_teens",
              "francais_french", "hispanic_latinx", "horror", "lgbtq+", "library_stories", "library_talks",
              "mysteries_crime", "nonfiction", "poetry", "popular_culture", "research_at_nypl", "romance",
              "science_fiction", "the_librarian", "women's_history", "work_cited", "chinese_language"]
        # keywords for the Channel Filters, we use these keywords to look in the every link text
        keywords = ["Asian", "Memoir", "Black", "Book Lists", "Comic", "Digital", "Doc", "Early Literacy", "de",
                    'for kids', 'for teachers', 'for teens', 'de', 'Hispanic', 'Horror', 'LGBTQ', 'Library Stories',
                    'Library Talks', 'Mysteries', 'Nonfiction', 'Poetry', 'Popular Culture', 'Research at nypl',
                    'Romance', 'Science Fiction', 'Librarian', 'Women', 'Work/Cited', 'Chinese']

        # optional- the number of Channel Categories, to make sure link numbers match the Channel filters numbers
        numbers = len(self.find_elements('//*[@id="multiselect-channel"]/div/ul/li'))
        print(str(numbers) + " number of the links")
        print(str(len(li)) + " length of the links")
        # asserting the number of Channel elements by comparing them to the length of the list
        self.assert_(len(li) == numbers)
        print(numbers == len(li))

        # for loop to go over every Chanel filter applied and look for the keywords from the Dictionary above
        # if the keywords were found for more than the selected 'count' number, the tests pass
        for x in range(0, 29):
            count = 0
            # categories that do not have significant keyword amount in this list, will be skipped testing
            low_amount = [3, 7, 9, 10, 11, 15, 16, 17, 18, 19, 21, 22, 24, 25]
            if x in low_amount:
                continue
            self.click(self.li_dic["" + li[x] + ""])
            # change the apply_**** filter accordingly
            self.click(self.apply_channel)
            for y in range(1, 11):
                # optional print of the Links
                # print(self.get_current_url())
                links = '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[' + str(y) + ']/div/div[2]/h3/a'

                link_text = self.get_text(links)
                # optional print of the link texts
                # print(link_text)
                if keywords[x] in link_text:
                    count += 1
            print(keywords[x])
            print(str(count))
            # asserting count number for the keyword appears more than expected (3 for now)
            # count number set as 1, optional to change
            self.assert_true(count >= 1,
                             str(count) + " times selected " + keywords[x] + " channel and the content matches")
            self.click(self.channels)
            self.click(self.li_dic["" + li[x] + ""])

    def test_subjects(self):
        """
        this method tests if the keywords from a list appeared more than the desired amount (count) in the link-texts
        """

        # assert subjects button
        self.click(self.subjects)
        self.wait_for_element(self.subjects)
        self.assert_element(self.subjects)

        # creating a list for Channel Filters
        li = ['art', 'business', 'genealogy', 'history', 'nyc_history', 'performing_arts',
              'science']
        # keywords for the Channel Filters, we use these keywords to look in the every link text
        keywords = ["Art", "Business", "Genealogy", "History", "History", "Music", "Science"]

        # for loop to go over every Chanel filter applied and look for the keywords from the Dictionary above
        # if the keywords were found for more than the selected 'count' number, the tests pass
        for x in range(0, 7):
            count = 0
            # categories that do not have significant keyword amount in this list, will be skipped testing
            low_amount = [3, 4]
            if x in low_amount:
                continue
            self.click(self.li_dic["" + li[x] + ""])
            # change the apply_**** filter accordingly
            self.click(self.apply_subject)
            for y in range(1, 11):
                # optional print of the Links
                # print(self.get_current_url())
                links = '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[' + str(y) + ']/div/div[2]/h3/a'

                link_text = self.get_text(links)
                # optional print of the link texts
                # print(link_text)
                if keywords[x] in link_text:
                    count += 1
            print(keywords[x])
            print(str(count))
            # count number set as 1, optional to change
            self.assert_true(count >= 1,
                             str(count) + " times selected " + keywords[x] + " channel and the content don't match")
            self.click(self.subjects)
            self.click(self.li_dic["" + li[x] + ""])

    def test_libraries(self):
        """ this method tests all 92 (as of May 2022) library filters by searching
        a keyword from their link texts in their library location links """

        # assert Libraries button
        self.assert_element(self.libraries)

        # finding length/number of the libraries in the filter
        self.click(self.libraries)
        library_filter_len = len(self.find_elements('//*[@id="multiselect-library"]/div/ul/li'))
        self.click(self.libraries)

        count = 0
        for x in range(1, library_filter_len + 1):
            no_data_libraries = [3, 15, 18, 26, 35, 49, 54, 68, 76, 89, 92]
            if x in no_data_libraries:
                x += 1
                count += 1
                continue
            else:
                count += 1

            # get the text of the filter and put them in a dictionary
            # y = self.get_text('//*[@id="multiselect-library"]/div/ul/li[' + str(x) + ']').split()
            # click the filter
            self.click(self.libraries)
            self.click('//*[@id="multiselect-library"]/div/ul/li[' + str(x) + ']/label/span[2]')
            self.click(self.apply_library)

            # retrieving each word from the library links and putting them in a dictionary
            print("x is = " + str(x))
            self.wait_for_element('/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[1]/div'
                                  '/div['
                                  '2]/div[1]/div[2]')
            library_links_text = self.get_text('/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[1]/div'
                                               '/div['
                                               '2]/div[1]/div[2]')

            library_words_dic = library_links_text.split()
            print(library_words_dic)  # optional print of the dictionary

            # asserting that the dictionary contains the first text of the library filter
            print(library_words_dic[0])  # optional print of the first word of the dictionary
            self.assert_true(library_words_dic[0] in library_words_dic, "the library filter not found in the links")
            x += 1
            print(count)  # optional print of the count

            # resetting/going back to the next link
            print(self.get_current_url())  # optional print of the current url
            self.click(self.libraries)
            self.click(self.clear_library)

    def test_divisions(self):
        """
        this method gets the filter name from division and also gets its corresponding
        location from the page when the filters applied and asserts they match
        e.g. Art & Architecture Collection  ---->   Stephen A. Schwarzman Building
        :return:
        """
        # assert Divisions button
        self.assert_element(self.divisions)

        # click 'divisions' tab
        self.click(self.divisions)

        # find divisions filter amount
        divisions_filter_length = len(self.find_elements('//*[@id="multiselect-division"]/div/ul/li'))
        print(divisions_filter_length)
        self.click(self.divisions)

        # counter for the length/amount of the division filters in the for loop
        count = 0

        # for loop to go over filters individually and count the amount
        for x in range(1, divisions_filter_length):
            self.click(self.divisions)

            # xpath for each division filter
            filter_link = '//*[@id="multiselect-division"]/div/ul/li[' + str(x) + ']/label/span[2]'

            self.click(filter_link)
            self.click(self.apply_division)

            locations_with_no_first_links = [6, 9, 23]
            if x in locations_with_no_first_links:
                location_link = '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[2]/div/div[2]/div[1]/div[' \
                                '2]/div/a'
            elif x == 24:
                self.click(self.divisions)
                self.click(self.clear_division)
                continue
            else:
                location_link = '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[1]/div/div[2]/div[1]/div[' \
                                '2]/div/a'
            location_text = self.get_text(location_link.strip())

            '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[1]/div/div[2]/div[1]/div[2]/div/a'
            '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[1]/div/div[2]/div[1]/div[2]/div/a'

            # print("x is = " + str(x))
            # print(self.get_current_url())
            self.click(self.divisions)
            self.click(self.clear_division)

            # list of filters and their locations
            locations = ['Art & Architecture Collection', 'Art and Artifacts Division', 'Billy Rose Theatre Division',
                         'Carl H. Pforzheimer Collection of Shelley and His Circle', 'DeWitt Wallace Periodical Room',
                         'Dorot Jewish Division', 'General Research Division', 'George Arents Collection',
                         'Henry W. and Albert A. Berg Collection of English and American Literature',
                         'Irma and Paul Milstein Division of United States History, Local History and Genealogy',
                         'Jean Blackwell Hutson Research and Reference Division',
                         'Jerome Robbins Dance Division', 'Lionel Pincus and Princess Firyal Map Division',
                         'Manuscripts and Archives Division', 'Manuscripts, Archives and Rare Books Division',
                         'Moving Image and Recorded Sound Division', 'Music Division',
                         'Photographs and Prints Division',
                         'Photography Collection', 'Picture Collection', 'Print Collection', 'Rare Book Division',
                         'Spencer Collection', 'The Rodgers and Hammerstein Archives of Recorded Sound',
                         'Theatre on Film and Tape Archive']

            print("------------------------------------------")
            print(locations[x - 1])
            print("expected location = \t" + self.location_dic["" + locations[x - 1] + ""])
            print("actual location   = \t" + location_text)
            expected_loc = self.location_dic["" + locations[x - 1] + ""].strip()
            actual_loc = location_text
            self.assert_true(expected_loc == actual_loc)

            count += 1

            print("going back to X loop")

    def test_audience(self):
        # assert Audience button
        self.assert_element(self.audience)

        # click 'Audience' tab
        self.click(self.audience)

        # click 'Adults' filter
        self.click('//*[@id="multiselect-audience_by_age"]/div/ul/li[1]/label/span[2]')
        self.click(self.apply_audience)
        # url for the filter
        url_text = self.get_current_url()
        # assert the url has the given text
        self.assert_true('audience_by_age=216' in url_text)
        self.click(self.audience)
        self.click(self.clear_audience)

        self.click(self.audience)
        # click 'Kids' filter
        self.click('//*[@id="multiselect-audience_by_age"]/div/ul/li[2]/label/span[2]')
        self.click(self.apply_audience)
        # url for the filter
        url_text = self.get_current_url()
        # assert the url has the given text
        self.assert_true('audience_by_age=217' in url_text)
        self.click(self.audience)
        self.click(self.clear_audience)

        self.click(self.audience)
        # click 'Teens' filter
        self.click('//*[@id="multiselect-audience_by_age"]/div/ul/li[3]/label/span[2]')
        self.click(self.apply_audience)
        # url for the filter
        url_text = self.get_current_url()
        # assert the url has the given text
        self.assert_true('audience_by_age=222' in url_text)
        self.click(self.audience)
        self.click(self.clear_audience)

    # some reusable methods for the blogs automation


'''
    def test_filter_template(self):
        # asserting channel categories
        # creating a list for Channel Filters
        li = []
        # keywords for the Channel Filters, we use these keywords to look in the every link text
        keywords = []

        # for loop to go over every Chanel filter applied and look for the keywords from the Dictionary above
        # if the keywords were found for more than the selected 'count' number, the tests pass
        for x in range(0, 1):
            count = 0
            # categories that do not have significant keyword amount in this list, will be skipped testing
            low_amount = []
            if x in low_amount:
                continue
            self.click(self.li_dic["" + li[x] + ""])
            # change the filter accordingly
            self.click(self.apply_filter)
            for y in range(1, 11):
                # optional print of the Links
                # print(self.get_current_url())
                links = '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[' + str(y) + ']/div/div[2]/h3/a'

                link_text = self.get_text(links)
                # optional print of the link texts
                # print(link_text)
                if keywords[x] in link_text:
                    count += 1
            print(keywords[x])
            print(str(count))
            # count number set as 3, optional to change
            self.assert_true(count >= 3,
                             str(count) + " times selected " + keywords[x] + " channel and the content matches")
            self.click(self.channels)
            self.click(self.li_dic["" + li[x] + ""])

    def test_word_counts(self):
        # this method is used to count and sort the most used words on the link text
        # update dictionary (li-dic) in blog_all_page with new locators
        # update apply_**** in blog_all_page
        # change the list in according to new tab
        li = ["art", "business", "genealogy", "history", "nyc_history",
              "performing_arts", "science"]
        # change the 'self.click(self.*****)'
        self.click(self.subjects)

        # update the range(0, X) of the filters
        for x in range(0, 7):
            count = 0
            low_amount = []
            if x in low_amount:
                continue
            counts = dict()
            self.click(self.li_dic["" + li[x] + ""])
            # apply the filter for the specific tab, e.g. apply_channel or apply_subject
            self.click(self.apply_subject)
            for y in range(1, 11):
                # optional print of the Links
                # print(self.get_current_url())
                links = '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[' + str(y) + ']/div/div[2]/h3/a'

                link_text = self.get_text(links)
                # optional print of the link texts
                # print(link_text)

                # for loop to see which word used most in each channels' blog links
                # this helps to decide which keyword to look for if the clicked channel content is displayed
                # used a dictionary inside a for loop
                words = link_text.split()
                junk_words = ['to', 'To', 'the', 'The', 'of', 'Of', 'and', 'And', 'in', 'In', 'from', 'From', 'for',
                              'For', 'by', 'By', 'with']

                for word in words:
                    if word in junk_words:
                        continue
                    elif word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1
            # sorting the Count items in Reverse order to get the most used words in a decremental way
            var = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}
            print(str(x) + "- " + li[x])
            print(self.get_current_url())
            print(var)
            # change the 'self.click(self.*****)'
            self.click(self.subjects)
            self.click(self.li_dic["" + li[x] + ""])

    def test_lib_sample(self):
        # assert Libraries button
        self.assert_element(self.libraries)

        a = 1  # variable to iterate for each the library_list below

        # finding length/number of the libraries in the filter
        self.click(self.libraries)
        library_filter_len = len(self.find_elements('//*[@id="multiselect-library"]/div/ul/li'))
        self.click(self.libraries)

        x = 1  # starting point of the loop
        count = 0
        for x in range(1, library_filter_len + 1):
            no_data_libraries = [3, 15, 18, 26, 35, 49, 54, 68, 76, 89, 92]
            if x in no_data_libraries:
                x += 1
                count += 1
                continue
            else:
                count += 1
            # get the text of the filter and put them in a dictionary
            # y = self.get_text('//*[@id="multiselect-library"]/div/ul/li[' + str(x) + ']').split()
            # click the filter
            self.click(self.libraries)
            self.click('//*[@id="multiselect-library"]/div/ul/li[' + str(x) + ']/label/span[2]')
            self.click(self.apply_library)

            # retrieving each word from the library links and putting them in a dictionary
            self.wait_for_element('/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[1]/div'
                                  '/div['
                                  '2]/div[1]/div[2]')
            library_links_text = self.get_text('/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[1]/div'
                                               '/div['
                                               '2]/div[1]/div[2]')

            library_words_dic = library_links_text.split()
            print(library_words_dic)  # optional print of the dictionary

            # asserting that the dictionary contains the first text of the library filter
            print(library_words_dic[0])  # optional print of the first word of the dictionary
            self.assert_true(library_words_dic[0] in library_words_dic, "the library filter not found in the links")
            x += 1
            print(count)  # optional print of the count

            # resetting/going back to the next link
            print(self.get_current_url())  # optional print of the current url
            self.click(self.libraries)
            self.click(self.clear_library)

    def test_division_spot_finder(self):
        """
        this method gets the filter name from division and also gets its corresponding
        location from the page when the filters applied
        e.g. Art & Architecture Collection  ---->   Stephen A. Schwarzman Building
        :return:
        """

        for x in range(1, 2):
            self.click(self.divisions)

            filter_link = '//*[@id="multiselect-division"]/div/ul/li[' + str(x) + ']/label/span[2]'

            # get filter name
            filter_text = self.get_text(filter_link)

            # get location for the filter
            self.click(filter_link)
            self.click(self.apply_division)

            locations_with_no_first_links = [6, 9, 23]
            if x in locations_with_no_first_links:
                location_link = '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[2]/div/div[2]/div[1]/div[' \
                                '2]/div/a'
            elif x == 24:
                self.click(self.divisions)
                self.click(self.clear_division)
                continue
            else:
                location_link = '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[1]/div/div[2]/div[1]/div[' \
                                '2]/div/a'
            location_text = self.get_text(location_link)

            # reset filters for the next loop
            self.click(self.divisions)
            self.click(self.clear_division)

            print(filter_text, "\t", location_text)
'''
