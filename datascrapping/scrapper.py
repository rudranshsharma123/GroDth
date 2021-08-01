# # Instantiate the scraper objects 
# from instascrape import *





# # print(google.followers)
# # print(google_post['hashtags'])
# # print(google_hashtag.amount_of_posts)

hashtags_list = ["love", 'instagood', 'photooftheday', 'fashion',
"beautiful",
"happy",
"cute",
"tbt",
"like4like",
"followme",
"picoftheday",
"follow",
'me',
"selfie",
"summer",
"art",
"instadaily",
"friends",
"repost",
"nature",
"girl",
"fun",
"style",
"smile",
"food",
"instalike",
"likeforlike",
"family",
"travel",
"fitness",
"euro2020",
"tagsforlikes",
"follow4follow",
"nofilter",
"life",
"beauty",
"amazing",
"instamood",
"igers",
"instagram",
"photo",
"music",
"photography",
"makeup",
"dog",
"beach",
"sunset",
"model",
"foodporn",
"motivation",
"followforfollow",
"sky",
"lifestyle",
"design",
"gym",
"f4f",
"toofunny",
"cat",
"handmade",
"hair",
"vscocam",
"bestoftheday",
"vsco",
"funny",
"dogsofinstagram",
"drawing",
"artist",
"f4fl",
"flowers",
"baby",
"wedding",
"girls",
"instapic",
"pretty",
"photographer",
"instafood",
"party",
"inspiration",
"lol",
"cool",
"workout",
"likeforfollow",
"swag",
"fit",
"healthy",
"yummy",
"blackandwhite",
"foodie",
"moda",
"home",
"christmas",
"black",
"memes",
"winter",
"pink",
"sea",
"landscape",
"blue",
"london",
"holiday",
]
hashtags_list_Likes = [
"instadaily"
,"LikesForLikes"
,"instagram"
,"fashion"
,"me"
,"FollowMe"
,"love"
,"photography"
,"LikeForLike"
,"like"
,"followers"
,"likes"
,"LikeForLikes"
,"FollowForFollow"
,"myself"
,"f"
,"instalike"
,"comment"
,"beautiful"
,"LikeForFollow"
,"instagood"
,"l"
,"FollowBack"
,"smile"
,"PhotoOfTheDay"
,"FollowForFollowBack"
,"follow"
,"bhfyp"
,"PicOfTheDay"
]

hashtags_list_Pets = [
"CatLover"
,"of"
,"DogLovers"
,"cute"
,"cats"
,"dogstagram"
,"puppy"
,"catstagram"
,"dogs"
,"animal"
,"animals"
,"DogLife"
,"cachorro"
,"instagram"
,"DogOfTheDay"
,"love"
,"pets"
,"petstagram"
,"PetLovers"
,"DogsOfInstagram"
,"dog"
,"doglover"
,"instagood"
,"instapet"
,"PetsOfInstagram"
,"CatsOfInstagram"
,"pet"
,"cat"
,"instadog"
]

hashtags_list_Travel = [
"TravelPhotography"
,"PicOfTheDay"
,"NaturePhotography"
,"TravelBlogger"
,"beautiful"
,"landscape"
,"adventure"
,"explore"
,"instatravel"
,"photo"
,"trip"
,"summer"
,"travelgram"
,"photography"
,"art"
,"travel"
,"wanderlust"
,"nature"
,"instagood"
,"PhotoOfTheDay"
]

hashtags_list_Fashion = [
"bhfyp"
,"smile"
,"OutfitOfTheDay"
,"FashionPhotography"
,"FollowBack"
,"ootd"
,"FashionBlogger"
,"WhatIWore"
,"follow"
,"fashionista"
,"PhotoOfTheDay"
,"StyleInspo"
,"instastyle"
,"love"
,"CurrentlyWearing"
,"FashionBlog"
,"ShoppingAddict"
,"LookGoodFeelGood"
,"FashionAddict"
,"FashionStyle"
,"BeautyDoesntHaveToBePain"
,"style"
,"fashion"
,"FollowForFollowBack"
,"fashionable"
,"l"
,"PicOfTheDay"
,"fashiongram"

]

hashtags_list_Foodie = [
"instafood"
,"FoodBlogger"
,"lunch"
,"PicOfTheDay"
,"instadaily"
,"FoodPhotography"
,"PhotoOfTheDay"
,"food"
,"healthy"
,"foodie"
,"FoodLover"
,"bhfyp"
,"instagood"
,"tasty"
,"delicious"
,"foodstagram"
,"homemade"
,"cooking"
,"FoodPorn"
,"love"
,"foodgasm"
,"foodies"
,"HealthyFood"
,"dinner"
,"yummy"
,"restaurant"
]

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        username_input= self.driver.find_element_by_xpath("//input[@name='username']")
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_xpath("//input[@name='password']")
        password_input.send_keys(password)
        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()
        sleep(10)
    
class HomePage():
    def __init__(self, driver):
        self.driver =driver
    def goTo_login_page(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.implicitly_wait(5)
        return LoginPage(self.driver)

username = '' #add Your username   
password = '' #add your Password
search_text = "#cats" # Type in the thing you would want to be searched

browser = webdriver.Firefox(executable_path="geckodriver.exe") #Add the path to the gekodriver you can also add realative path instead of the actual 
home = HomePage(browser)
home = home.goTo_login_page()
dogs = home.login(username, password)
data = {}

# for i in hashtags_list:
#     try:
#         browser.get("https://www.instagram.com/explore/tags/{tags}/".format(tags = i))
#         x = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div').text
#         # browser.text
#         data[i] = x.split('\n')[1].split()[0]
#         sleep(5)
#     except:
#         continue

# for i in hashtags_list_Likes:
#     try:
#         browser.get("https://www.instagram.com/explore/tags/{tags}/".format(tags = i))
#         x = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div').text
#         # browser.text
#         data[i] = x.split('\n')[1].split()[0]
#         sleep(5)
#     except:
#         continue
# for i in hashtags_list_Pets:
#     try:
#         browser.get("https://www.instagram.com/explore/tags/{tags}/".format(tags = i))
#         x = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div').text
#         # browser.text
#         data[i] = x.split('\n')[1].split()[0]
#         sleep(5)
#     except:
#         continue
for i in hashtags_list_Foodie:
    try:
        browser.get("https://www.instagram.com/explore/tags/{tags}/".format(tags = i))
        x = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div').text
        # browser.text
        data[i] = x.split('\n')[1].split()[0]
        sleep(5)
    except:
        continue
# dogs.save_post()

print(data)
# print(data)
browser.quit()


import pandas as pd
import numpy as np
col = list(data.keys())
ind = list(data.values())
d = {'hash' :[], 'number' : [], 'category':'foodie'}
for i, v in enumerate(col):
    d['hash'].append(v)
    d['number'].append(ind[i])
df = pd.DataFrame(data= d)
df.to_csv("foodie.csv")
