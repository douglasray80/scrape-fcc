#!/usr/bin/python
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument('--ignore-certificate-errors')
chromeOptions.add_argument('--incognito')
chromeOptions.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get('https://learn.freeCodeCamp.org')

superblocks = driver.find_elements_by_class_name('superblock')

for superblock in superblocks:
    superblock.click()
    time.sleep(2)

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')
curriculum = soup.find(class_='map-ui')

with open("output.html", "w+") as file:
    file.write(str(curriculum.contents[0]))

# search_box.send_keys('ChromeDriver')
# search_box.submit()

# Get course module headers (ie Responsive Web Design Certification)
# modules = soup.find_all(class_='map-title')
# super_blocks = soup.find_all(class_='superblock')
# courses = curriculum.find_all(class_='superblock')
# with open("output/markup.html", "a+") as myfile:
#     for course in courses:

#         modules = course.find_all(class_='block')
#         for module in modules:
#             if 'open' not in module['class']:
#                 module['class'].append(u'open')
#             # print(module.attrs)

#         myfile.write(str(course))

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