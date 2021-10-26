# TODO: Clean this up please.
# optimize some segement.


# import all libraries
from bs4 import BeautifulSoup
import requests
import time, os
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from datetime import datetime

start = datetime.now()

# Starts the web driver and pass it back to be used elsewhere.
def get_driver(url):
    from selenium.webdriver.common.action_chains import ActionChains

    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver"  # path to the chromedriver executable
    os.environ["webdriver.chrome.driver"] = chromedriver
    # 1- Go to "fifaindex website"
    page = requests.get(url).text
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    driver.implicitly_wait(4)
    driver.maximize_window()
    return driver

# Fetches the players name, page url in the current page and returns two lists of names, urls
def get_name_url(driver):
    # We iterate the whole table of players in the page
    # get table size
    # selenium player list to be converted to text by for loop
    player_list_sel = driver.find_elements_by_class_name("link-player")
    player_list = [0] * (len(player_list_sel))
    url_list_sel = driver.find_elements_by_class_name("link-player")
    url_list = [0] * (len(url_list_sel))

    i = 0
    for name in player_list_sel:
        player_list[i] = str((name.text))
        url_list[i] = name.get_attribute("href")
        i += 1

    # TODO: find a better way to do this lol
    # clean empty rows
    player_list = list(filter(None, player_list))
    # remove duplicates
    url_list = list(dict.fromkeys(url_list))
    # print(player_list)
    # print(url_list)
    return player_list, url_list

# Loops over all specified pages and returns all players at the end in a dataframe.
def get_players_in_page(driver):
    start = datetime.now()
    page_players = pd.DataFrame()
    current_players = []
    # Change to 600 to get all players which = 18k
    no_of_pages = 601  # if we use 600 it stops at 599
    # iterate over 34 pages
    for j in range(1, no_of_pages):
        page_url = "https://www.fifaindex.com/players/?page=" + str(j)
        driver.get(page_url)
        # get players table as two lists of players names and url_list
        names, urls = get_name_url(driver)

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
        print("Page ", j, " is Done!")
        # update driver to grab next page?
        print(datetime.now() - start)
        j += 1

    print(datetime.now() - start)
    return page_players

    # call get player info and pass the name and url

    # FIXME
    # def click_player(player_url,page_driver,action):
    #    actions.click(player_url)
    #    actions.perform()

# Fetches the player data and returns all info and attributes in a dict.
def get_player_info(player_name, player_url, driver):
    driver.get(player_url)

    # get player basic info append to dict
    info = driver.find_elements_by_xpath(
        "/html/body/main/div/div/div[2]/div[2]/div[2]/div/div/p"
    )
    player_rating = driver.find_element_by_xpath(
        "/html/body/main/div/div/div[2]/div[2]/div[2]/div/h5/span/span[1]"
    ).text
    i = 1
    player_dict = {}
    player_dict["Name"] = player_name
    player_dict["Overall-Rating"] = player_rating

    for inf in info:
        # print(i)
        # print(inf.text)
        try:
            info, ivalue = (inf.text).splitlines()
            player_dict[info] = ivalue
        except ValueError:
            print("There's not text value for attribute ", inf.text)

    # get all attributes append to dict then return
    par = driver.find_elements_by_xpath(
        "/html/body/main/div/div/div[2]/div[4]/div/div/div/p"
    )
    # get all attributes
    i = 1
    for pa in par:
        if i < 35:  # break after we get all numerical attributes
            # print(i)
            # print(pa.text)
            try:
                att, avalue = (pa.text).splitlines()
                # TODO solve extra columns split string and remove integers
                # maybe

                player_dict[(re.sub(r"\d+", "", att)).strip()] = avalue
            except ValueError:
                print("There's no readable value for attribute ", pa.text)

        i += 1

    # drop birthdate(4), 11, 12,14,15
    # read skill moves & weak foot?

    print(player_dict)
    ## TODO:  add method to grab all features and careful with numerical and non numerical
    # for pa in par:
    #    print(pa.text)
    #    attribute_name, attribute_value =

    # store in dict then append to dataframe
    # player_dict[attribute_name] = attribute_value
    # player_dict["name"] =str(name)
    driver.back()
    return player_dict


fifaindex = "https://www.fifaindex.com/players/"

# We call the driver first to open the web page
page_driver = get_driver(fifaindex)
# pass the driver to fetch players info in the all pages (which calls other functions and returns a dataframe)
players = get_players_in_page(page_driver)
players.head()
players.to_csv("Fifa_22_players_ratings_6.csv")
page_driver.close()
# chrome Driver is the PATH to our folder containing the driver
