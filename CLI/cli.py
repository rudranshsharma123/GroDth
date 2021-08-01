import os
import random
from time import sleep
from unicodedata import category

import inquirer
import requests
from inquirer.themes import GreenPassion
from termcolor import colored, cprint
from cliutils import (clear_everything, get_categories, get_tags,
                          type_writer_anim)

categories = ['all', 'likes', 'pets', 'travel', 'fashion', 'foodie'] 

clear_everything()
sleep(4)


type_writer_anim("Hello and welcome to GroDth\n Your helper in Growing and cultivating your Online Presence \n")

sleep(1.5)

while True:
    questions = [ 
        inquirer.List(
            'ans',
            message = 'Menu',
            choices = ['About GroDth', 'Search HashTags', 'Categorical HashTags', 'Best Pracitises' ,'Fair Use', 'Quit'],
        )
    ]
    ans = inquirer.prompt(questions, theme = GreenPassion()) 

    if ans['ans'] == "Search HashTags":
        question = [inquirer.Text(
            'hashtag',
            message = "Enter the name of the hashtags you would like to search"
        )]

        search_ans = inquirer.prompt(question, theme = GreenPassion())
        search_key = search_ans['hashtag']
        type_writer_anim("Searching for your hashtags \n")
        get_tags(search_key)
    elif ans['ans'] == 'Quit':
        print('\n')
        type_writer_anim("Quitting!! \n")
        exit(0)
    elif ans['ans']== "Categorical HashTags":
        categorical_hashes = [ 
        inquirer.List(
            'ans',
            message = 'Available Categories are as follows',
            choices = categories,
        )
    ]
        choices = inquirer.prompt(categorical_hashes, theme = GreenPassion()) 
        type_writer_anim([x + '\n' for x in get_categories(choices['ans'])])
    elif ans['ans'] == 'About GroDth':
        text = """Hello and welcome to GroDth. \n Gro-Dth is Growth + Depth that is exactly what this platform should help you in doing. \n You are here because you are or want to be an content creator. \n This platform will help you in reaching your follower goal. \n You will find a comprehensive HashTags analytics. \n You will find best practises and things to help your all round GroDth \n There is also a fair use section. Which goes through your video and comapares it with the source material to ensure fair use \n"""
        type_writer_anim(text)
    elif ans['ans'] == "Best Pracitises":
        text = """There are a few practises you should follow to for your growth. \n First, Follow Brand Hashtags, The ones you are going to post about \n Secondly, Categorica Hashtags is very important. \n Thirdly, follow event hashtags, like in the month of July do use #Pride. \n Do follow, campaign hashtags as welll. \n While you will find, a lot of the most popular hashtags here do not blindly follow them! \n"""
        type_writer_anim(text)
    elif ans['ans'] == 'Fair Use':
        question = [inquirer.Text(
            'vid1',
            message = "Enter the name of the video file 1"
        ), 
        inquirer.Text(
            'vid2',
            message = "Enter the name of the video file 2"
        )
        ]

        search_ans = inquirer.prompt(question, theme = GreenPassion())
        one = search_ans['vid1']
        two = search_ans['vid2']

        type_writer_anim("Comparing the two videos for you \n")
        
        
        from fair_use import ImageChecker

        check = ImageChecker(one = one, two = two)
        check.checkTwoVid()
        

