#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome('chromedriver')

baseUrl = 'https://learn.freecodecamp.org/'
driver.get(baseUrl)
expandLists = driver.find_elements_by_class_name("superblock")
for x in range(len(expandLists)):
    if expandLists[x].is_displayed():
        driver.execute_script("arguments[0].click();", expandLists[x])
        time.sleep(1)
page_source = driver.page_source

# url = urllib2.urlopen(page)
soup = BeautifulSoup(page_source, 'html.parser')

curriculum = soup.find(class_='map-ui')

# Get course module headers (ie Responsive Web Design Certification)
# modules = soup.find_all(class_='map-title')
super_blocks = soup.find_all(class_='superblock')
courses = curriculum.find_all(class_='superblock')
with open("output/markup.html", "a+") as myfile:
    for course in courses:

        modules = course.find_all(class_='block')
        for module in modules:
            if 'open' not in module['class']:
                module['class'].append(u'open')
            # print(module.attrs)

        myfile.write(str(course))

        # challenges = module.find_all(class_='map-challenge-title')
        # for challenge in challenges:
        # print(challenge.a.string)

# urlList = []

# get titles from
# course (superblock)
# module (block)
# challenge

# get all the course titles, module titles, and challenge titles
# parse all the titles into urls
# append to urlList
# for super_block in super_blocks:
#     if super_block.div:
#         # course title
#         course_heading = super_block.div.h4.string

#         if 'Certification' not in course_heading:
#             section_title = course_heading.split(' (')[0]
#         else:
#             section_title = course_heading.split(' Certification')[0]

#         # course title, parsed
#         section_title = section_title.lower().replace(' ', '-')
#         # print(section_title)

#         blocks = super_block.find_all(class_='block')

#         for block in blocks:
#             if block.div:
#                 # module title, parsed
#                 module_title = block.div.h5.string

#             module_title = module_title.lower().replace(' ', '-')

#             challenges = block.find_all(class_='map-challenge-title')

#             for challenge in challenges:
#                 challenge_title = challenge.a.string.lower().replace(' ', '-')
#                 url = '%s/%s/%s' % (section_title,
#                                     module_title, challenge_title)
#                 urlList.append(url)

# for item in urlList:
#     print(item)

# for module in modules:
#     # is there a course header?
#     if module.h4:
#         heading = module.h4.string
#         if 'Certification' not in heading:
#             section_title = heading.split(' (')[0]
#         else:
#             section_title = heading.split(' Certification')[0]

#         # print(section_title.lower().replace(' ', '-'))

#         sub_modules = module.find_all(class_='map-title')

# if module.h5:
#     sub_heading = module.h5.string
#     print(sub_heading)