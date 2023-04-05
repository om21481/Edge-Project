from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

from time import sleep
import pyautogui as gui

array = ['Default','Profile 1']

edge_options = Options()
edge_options.use_chromium = True     
edge_options.add_argument("user-data-dir=/Users/omgarg/Library/Application Support/Microsoft Edge")

def open_drivers(profile):
        print(f"{profile}")
        edge_options.add_argument(f"profile-directory={profile}")
        edge_options.add_argument("--start-maximized")
        try:
                driver = webdriver.Edge(options = edge_options, executable_path="msedgedriver.exe")
        except:
                print(f"Error {profile}")

                #Now main code starts
                make_searches()

def make_searches():
        sleep(2)
        gui.click(1141, 84)            # for Abs 
        sleep(0.5)
        gui.click(907, 350)
        sleep(0.5)

        gui.click(390, 46)              # for opening new tab

        sleep(150)      #for searches to happen

        gui.click(321, 88)            # for opening rewards tab
        sleep(0.5)
        gui.typewrite("https://rewards.bing.com/ \n")
        sleep(2)

        gui.click(1181, 84)             # this is for vpn
        sleep(0.5)
        gui.click(1031, 220)            #connected to US 
        sleep(2)

        #Now reload again
        gui.click(321, 88)            # for opening rewards tab
        sleep(0.5)
        gui.typewrite("https://rewards.bing.com/ \n")
        sleep(2)

        # Now start searches again
        gui.click(1141, 84)            # for Abs 
        sleep(0.5)
        gui.click(907, 350)

        sleep(150)      #for searches to happen

        #Now close the server
        gui.click(1181, 84)             # this is for vpn
        sleep(0.5)
        gui.click(1054, 461)            
        sleep(0.5)

        #Now reload again
        gui.click(321, 88)            # for opening rewards tab
        sleep(0.5)
        gui.typewrite("https://rewards.bing.com/ \n")
        sleep(2)

        # Now exit the window
        gui.click(26, 50)

        # print(gui.position())


for i in array:
        open_drivers(i)