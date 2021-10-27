# TODO: Clean this up please.
# optimize some segment.


# import all libraries
# from bs4 import BeautifulSoup
#import requests
# import time
import os
import pandas as pd
from pip._internal.utils import logging
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import re
from datetime import datetime

start = datetime.now()


# Starts the web driver with the given link and pass it back to be used elsewhere.


def get_driver(url):
    #from selenium.webdriver.common.action_chains import ActionChains

    # path to the chromedriver executable
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    # 1- Go to "fifaindex website"
    #page = requests.get(url).text
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    driver.implicitly_wait(4)
    driver.maximize_window()
    return driver


# Fetches the players name, page url in the current page and returns two lists of names, urls with size 30 each


def get_player_name_url(driver):
    # We iterate the whole table of players in the page
    # get table size
    # selenium player list to be converted to text by for loop
    player_list_sel = driver.find_elements_by_class_name("link-player")
    player_list = [0] * (len(player_list_sel))
    url_list_sel = driver.find_elements_by_class_name("link-player")
    url_list = [0] * (len(url_list_sel))

    i = int(0)
    for name in player_list_sel:
        player_list[i] = str(name.text)
        url_list[i] = name.get_attribute("href")
        i += 1

    # TODO: find a better way to do this lol
    # clean empty rows
    player_list = list(filter(None, player_list))
    # remove duplicates (why are we getting duplicates in the first place?)
    url_list = list(dict.fromkeys(url_list))
    # print(player_list)
    # print(url_list)
    return player_list, url_list


# Loops over all specified pages and returns all players at the end in a dataframe.


def get_players(driver, starting_page, no_of_pages):
    # just to calculate how long it takes
    start_fun = datetime.now()
    page_players = pd.DataFrame()
    current_players = []
    # Change to 600 to get all players which = 18k
    _starting_page = starting_page  # start from this page number
    _no_of_pages = no_of_pages  # if we use 600 it stops at 599
    for page_number in range(_starting_page, _no_of_pages):
        # page_number is page number
        page_url = "https://www.fifaindex.com/players/?page=" + str(page_number)
        driver.get(page_url)
        # get players table as two lists of players names and url_list
        names, urls = get_player_name_url(driver)

        # gets all players info in current page
        for i in range(len(urls)):
            # click player and go to player page
            # # FIXME:
            # click_player(urls[i],driver,action)
            # get player info
            player = get_player_info(names[i], urls[i], driver)
            current_players.append(player)
            # return to page to get next players
            # # FIXME: with click_player
            # driver.back()
            print("Player ", names[i], " is Done!")
            i += 1
        page_players = pd.DataFrame(current_players)
        print("Page ", page_number, " is Done!")
        # update driver to grab next page?
        print(datetime.now() - start)
        page_number += 1

    print(datetime.now() - start_fun)
    return page_players

    # call get player info and pass the name and url

    # FIXME
    # def click_player(player_url,page_driver,action):
    #    actions.click(player_url)
    #    actions.perform()


# Fetches the player data and returns all info and attributes in a dict.


def get_player_info(player_name, player_url, driver):
    # the function takes the player name to append it to the player player_dict
    # the function takes the player url to open that page
    # TODO: change this to user selenium without passing player's url
    driver.get(player_url)

    # get player basic info append to dict
    info = driver.find_elements_by_xpath(
        "/html/body/main/div/div/div[2]/div[2]/div[2]/div/div/p"
    )
    player_rating = driver.find_element_by_xpath(
        "/html/body/main/div/div/div[2]/div[2]/div[2]/div/h5/span/span[1]"
    ).text
    i = 1
    player_dict = {
        "Name" : player_name,
        "Overall-Rating" : player_rating
    }
   # player_dict["Name"] = player_name
    #player_dict["Overall-Rating"] = player_rating

    for inf in info:
        # print(i)
        # print(inf.text)
        try:
            info, ivalue = inf.text.splitlines()
            player_dict[info] = ivalue
        except ValueError:
            print("There's not text value for attribute ", inf.text)

    # get all attributes append to dict then return
    attributes = driver.find_elements_by_xpath(
        "/html/body/main/div/div/div[2]/div[4]/div/div/div/p"
    )
    # get all attributes
    i = 1
    for attribute in attributes:
        if i < 35:  # break after we get all numerical attributes
            # print(i)
            # print(pa.text)
            # some values don't have a pair of attribute & value and throws an exception
            # theres probably a better way to do this
            try:
                att, avalue = attribute.text.splitlines()
                player_dict[(re.sub(r"\d+", "", att)).strip()] = avalue
            except ValueError:
                logging.exception("There's no readable value for attribute ", attribute.text)

        i += 1
    # TODO :
    # drop birthdate(4), 11, 12,14,15
    # read skill moves & weak foot?
    # testing
    print(player_dict)

    driver.back()
    return player_dict


def main():
    # TODO : make the url,starting page and range readable from the user and pass it to get_driver function
    fifaindex = "https://www.fifaindex.com/players/"
    starting_page = int(input('Enter starting page: '))
    no_of_pages = int(input('Enter the range ( How many pages you want to scrap?): '))
    # We call the driver first to open the web page with the given link
    driver = get_driver(fifaindex)
    # pass the driver to fetch players info in the all pages (which calls other functions and returns a dataframe)
    # TODO : edit the function to take starting page, range from user and rename the whole function
    players = get_players(driver, starting_page, no_of_pages)
    # test
    players.head()
    # edit the file name to be named from starting page - ending
    players.to_csv("Data/Fifa_22_players_ratings_" + str(starting_page) + "-" + str(no_of_pages) + ".csv")
    driver.close()




main()
