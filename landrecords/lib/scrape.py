# -*- coding: utf-8 -*-

import time
import os
import re
import glob
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import timedelta  # , datetime

from landrecords.config import Config
from landrecords.lib.mail import Mail
from landrecords.lib.log import Log

log = Log('initialize').logger


class Scrape(object):

    # todo: write function with rewrite = False that ignores any
    # sales previously scraped.
    def __init__(self,
                 initial_date=Config().OPENING_DATETIME,
                 until_date=Config().YESTERDAY_DATETIME,
                 rewrite=True):

        self.initial_date = initial_date
        self.until_date = until_date

        self.driver = webdriver.PhantomJS(
            executable_path='%s/bin/phantomjs' % Config().PROJECT_DIR,
            service_log_path='%s/ghostdriver.log' % Config().LOG_DIR,
            port=0)
        # self.driver = webdriver.Firefox(timeout=60)

    '''
    Login page
    '''

    def load_homepage(self):
        log.info('Load homepage')
        self.driver.get("http://onlinerecords.orleanscivilclerk.com/")
        time.sleep(2.2)

    def find_login_link(self):
        log.info('Find login link')
        login_link_elem = self.driver.find_element_by_id("Header1_lnkLogin")
        log.info('Click login link')
        login_link_elem.click()
        time.sleep(1.2)

    def enter_username(self):
        log.info('Find username field')
        unsername_elem = self.driver.find_element_by_id("Header1_txtLogonName")
        log.info('Enter username')
        unsername_elem.send_keys(Config().LRD_USERNAME)

    def enter_password(self):
        log.info('Find password field')
        password_elem = self.driver.find_element_by_id("Header1_txtPassword")
        log.info('Enter password')
        password_elem.send_keys(Config().LRD_PASSWORD)
        log.info('Return')
        password_elem.send_keys('\n')  # To trigger search function
        time.sleep(2.2)

        log.debug(self.driver.title)

    def login(self):
        self.load_homepage()
        self.find_login_link()
        self.enter_username()
        self.enter_password()

    '''
    Navigate search page
    '''

    def load_search_page(self):
        self.driver.get(
            "http://onlinerecords.orleanscivilclerk.com/RealEstate/" +
            "SearchEntry.aspx")
        time.sleep(2.2)

    def find_permanent_date_range(self):
        date_range_elem = self.driver.find_element_by_id(
            "cphNoMargin_lblSearchSummary")

        date_range = date_range_elem.text
        log.debug(date_range)

        first_date = re.match(r"Permanent\ Index From ([0-9/]*) to ([0-9/]*)",
                              date_range).group(1)  # 02/18/2014
        first_date = first_date.replace('/', '')
        log.debug(first_date)

        second_date = re.match(r"Permanent\ Index From ([0-9/]*) to ([0-9/]*)",
                               date_range).group(2)  # 02/25/2015
        second_date = second_date.replace('/', '')
        log.debug(second_date)

        return first_date, second_date

    def get_date_range_html(self):
        date_range_html = self.driver.page_source

        return date_range_html

    def delete_permanent_date_range_when_scraped_file(self, year, month, day):
        log.info('Delete old permanent-date-range-when-scraped*.html')
        for fl in glob.glob("%s/raw/" % (Config().DATA_DIR) +
                            "%s-%s-%s/" % (year, month, day) +
                            "permanent-date-range-when-scraped*.html"):
            os.remove(fl)

    def save_permanent_date_range_when_scraped_file(self,
                                                    year,
                                                    month,
                                                    day,
                                                    date_range_html,
                                                    first_date,
                                                    second_date):
        # Save permanent date range for this individual sale.
        log.info('Save new permanent-date-range-when-scraped*.html file')
        individual_html_out = open(
            "%s/raw/%s-%s-%s/permanent-date-range-when-scraped_%s-%s.html" % (
                Config().DATA_DIR, year, month, day,
                first_date, second_date
            ), "w")
        individual_html_out.write(date_range_html.encode('utf-8'))
        individual_html_out.close()

    def delete_permanent_date_range_file(self):
        # Delete old file first
        log.info(
            'Delete old most-recent-permanent-date-range/*.html file')
        for fl in glob.glob("%s/most-recent-permanent-date-range/*.html"
                            % (Config().DATA_DIR)):
                os.remove(fl)

    def save_permanent_date_range_file(self,
                                       date_range_html,
                                       first_date,
                                       second_date):
        log.info('Save new most-recent-permanent-date-range/*.html file')
        overall_html_out = open("%s/" % (Config().DATA_DIR) +
                                "most-recent-permanent-date-range/" +
                                "%s-%s.html" % (first_date, second_date),
                                "w")
        overall_html_out.write(date_range_html.encode('utf-8'))
        overall_html_out.close()

        time.sleep(2.2)

    def navigate_search_page(self, year, month, day):
        self.load_search_page()
        first_date, second_date = self.find_permanent_date_range()
        date_range_html = self.get_date_range_html()
        self.delete_permanent_date_range_when_scraped_file(year, month, day)
        self.save_permanent_date_range_when_scraped_file(
            year, month, day, date_range_html, first_date, second_date)
        self.delete_permanent_date_range_file()
        self.save_permanent_date_range_file(
            date_range_html, first_date, second_date)

    '''
    Search parameters
    '''

    def click_advanced_tab(self):
        log.info('search_parameters')

        # Advanced tab
        log.info('Find advanced tab')
        advanced_tab_elem = self.driver.find_element_by_id(
            "x:2130005445.2:mkr:ti1")
        log.info('Click on advanced tab')
        advanced_tab_elem.click()
        time.sleep(1.2)

    def enter_date_filed_from(self, search_date):
        date_file_from_elem = self.driver.find_element_by_id(
            "x:2002578730.0:mkr:3")
        date_file_from_elem.click()
        date_file_from_elem.send_keys(search_date)

    def enter_date_filed_to(self, search_date):
        date_file_to_elem = self.driver.find_element_by_id(
            "x:625521537.0:mkr:3")
        date_file_to_elem.click()
        date_file_to_elem.send_keys(search_date)

    def select_document_type(self):
        document_type_elem = self.driver.find_element_by_id(
            "cphNoMargin_f_dclDocType_291")
        log.info('Select SALE document type')
        document_type_elem.click()

    def click_search_button(self):
        log.info('Find search button')
        search_button_elem = self.driver.find_element_by_id(
            "cphNoMargin_SearchButtons2_btnSearch__2")
        log.info('Click search button')
        search_button_elem.click()
        time.sleep(2.2)

    def search_parameters(self, search_date):
        self.click_advanced_tab()
        self.enter_date_filed_from(search_date)
        self.enter_date_filed_to(search_date)
        self.select_document_type()
        self.click_search_button()

    '''
    Parse results
    '''

    def parse_results(self, year, month, day):
        # Find current page number
        try:
            log.info('Find item_list_elem')
            item_list_elem = self.driver.find_element_by_id(
                "cphNoMargin_cphNoMargin_OptionsBar1_ItemList")
            log.info('Find option')
            options = item_list_elem.find_elements_by_tag_name("option")
        except Exception, e:
            # Save table page
            log.error(e, exc_info=True)
            log.info('No sales for this day')
            html_out = open("%s/raw/%s-%s-%s/page-html/page1.html"
                            % (Config().DATA_DIR, year, month, day), "w")
            html_out.write((self.driver.page_source).encode('utf-8'))
            html_out.close()
            return

        total_pages = int(options[-1].get_attribute('value'))
        log.debug(total_pages)

        for i in range(1, total_pages + 1):
            log.debug(i)

            self.parse_page(i, year, month, day)

    def parse_page(self, i, year, month, day):

        # Save table page
        log.info('Write table page HTML')
        html_out = open("%s/raw/%s-%s-%s/page-html/page%d.html"
                        % (Config().DATA_DIR, year, month, day, i), "w")
        html_out.write((self.driver.page_source).encode('utf-8'))
        html_out.close()

        log.info('Build BeautifulSoup')
        soup = BeautifulSoup(open("%s/raw/%s-%s-%s/page-html/page%d.html"
                             % (Config().DATA_DIR, year, month, day, i)))

        log.info('Find all object IDs')

        rows = soup.find_all('td', class_="igede12b9e")  # List of Object IDs

        log.debug(len(rows))

        for j in range(1, len(rows)):
            log.debug((i - 1) * 20 + j)

            self.parse_sale(j, rows, year, month, day)

        log.info(
            'Go to http://onlinerecords.orleanscivilclerk.com/' +
            'RealEstate/SearchResults.aspx')
        self.driver.get(
            "http://onlinerecords.orleanscivilclerk.com/RealEstate/" +
            "SearchResults.aspx")

        log.info('Find next page button')
        next_button_elem = self.driver.find_element_by_id(
            "OptionsBar1_imgNext")
        log.info('Click next page button')
        next_button_elem.click()
        time.sleep(2.2)

    def parse_sale(self, j, rows, year, month, day):

        document_id = rows[j].string

        log.debug(document_id)

        single_sale_url = (
            "http://onlinerecords.orleanscivilclerk.com/" +
            "RealEstate/SearchResults.aspx?" +
            "global_id=%s" % (document_id) +
            "&type=dtl")

        log.debug(single_sale_url)

        try:
            log.info('Load %s', single_sale_url)
            self.driver.get(single_sale_url)
            time.sleep(1.2)
        except Exception, e:
            log.error(e, exc_info=True)

        log.info('Save this sale HTML')
        html_out = open("%s/" % (Config().DATA_DIR) +
                        "raw/" +
                        "%s-%s-%s/" % (year, month, day) +
                        "form-html/%s.html" % (document_id),
                        "w")
        html_out.write((self.driver.page_source).encode('utf-8'))
        html_out.close()

        time.sleep(1.2)

    '''
    Logout
    '''

    def logout(self):
        # No matter which page you're on, you can go back here and logout.
        log.info(
            'Load http://onlinerecords.orleanscivilclerk.com/' +
            'RealEstate/SearchEntry.aspx')
        self.driver.get(
            "http://onlinerecords.orleanscivilclerk.com/RealEstate/" +
            "SearchEntry.aspx")

        log.info('Find logout button')
        logout_elem = self.driver.find_element_by_id("Header1_lnkLogout")
        log.info('Click logout button')
        logout_elem.click()

    def cycle_through_dates(self):
        current_date = self.initial_date

        # Must search each date one at a time because there is a limit of
        # 300 results per search.
        while current_date != (self.until_date + timedelta(days=1)):
            year = current_date.strftime('%Y')  # "2014"
            month = current_date.strftime('%m')  # "09"
            day = current_date.strftime('%d')  # "09"

            log.debug(year + '-' + month + '-' + day)

            # Check if folder for this day exists. if not, then make one
            pagedir = "%s/raw/%s-%s-%s/page-html" % (
                Config().DATA_DIR, year, month, day)
            log.debug(pagedir)

            formdir = "%s/raw/%s-%s-%s/form-html" % (
                Config().DATA_DIR, year, month, day)
            log.debug(formdir)

            if not os.path.exists(pagedir):
                log.info('Making %s', pagedir)
                os.makedirs(pagedir)
            if not os.path.exists(formdir):
                log.info('Making %s', formdir)
                os.makedirs(formdir)

            search_date = month + day + year

            # The meat of this loop
            self.navigate_search_page(year, month, day)
            self.search_parameters(search_date)
            self.parse_results(year, month, day)

            current_date += timedelta(days=1)
            log.debug(current_date)

    def main(self):
        self.login()

        try:
            self.cycle_through_dates()
        except Exception, e:
            log.error(e, exc_info=True)
            Mail(
                subject="Error running Land Record's scrape.py script",
                body='Check scrape.log for more details.',
                frm='tthoren@thelensnola.org',
                to=['tthoren@thelensnola.org']).send_as_text()
        finally:
            self.logout()
            self.driver.close()
            self.driver.quit()
            log.info('Done!')

if __name__ == '__main__':
    Scrape(
        initial_date=Config().OPENING_DATETIME,
        until_date=Config().OPENING_DATETIME
    ).main()
