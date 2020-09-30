# Exercise 11
# Tanish sarmah
my_str="""Tutorials keyboard_arrow_downStudent keyboard_arrow_downCourses
Interview Preparationexpand_more
Practice @Geeksforgeeksexpand_more
Algorithmsexpand_more
Data Structuresexpand_more
Programming Languagesexpand_more
Web Technologiesexpand_more
Tutorial Libraryexpand_more
Computer Science Subjectsexpand_more
GATE 2021expand_more
UGC NET / ISROexpand_more
QUIZ Sectionexpand_more
Puzzles
Geeksforgeeks Initiativesexpand_more
Contact Us
Address:
GeeksforGeeks
5th & 6th Floor, Royal Kapsons, A- 118,
Sector- 136, Noida, Uttar Pradesh (201305)

For feedback and queries: feedback@geeksforgeeks.org

For course related queries: geeks.classes@geeksforgeeks.org
For payment related issues: geeks.classes@geeksforgeeks.org
For any issue in a purchased course : complaints@geeksforgeeks.org
To contribute, please see the contribute page
GeeksforGeeks Official App
auto
Most Popular Articles
Must Do Coding Questions for Companies like Amazon, Microsoft, Adobe, ...
Must Do Coding Questions Company-wise
CamelCase Pattern Matching
Get Your Dream Job With Amazon SDE Test Series
Flipkart On-campus Placement Process 2020 Graduate
Most Visited Articles
Count minimum swap to make string palindrome
TCS CodeVita 2020 - Important Dates, Eligibility, How to Apply?
SAP Labs India FTE Interview Experience | On-Campus (Virtual) 2020
DE Shaw Internship Interview Experience (On-Campus) 2021
SAP Labs India FTE Interview Experience | On-Campus (Virtual) 2020
GeeksforGeeks
room
5th Floor, A-118,
Sector-136, Noida, Uttar Pradesh - 201305
email
feedback@geeksforgeeks.org
Company
About Us
Careers
Privacy Policy
Contact Us
Learn
Algorithms
Data Structures
Languages
CS Subjects
Video Tutorials
Practice
Courses
Company-wise
Topic-wise
How to begin?
Contribute
Write an Article
Write Interview Experience
Internships
tanish234.code@gmail.com
Videos
@geeksforgeeks , Some rights reserved
"""
import re
var=re.findall(r"\s([a-zA-Z0-9]+.\w+@.+)",my_str)
# print(var)
f=open("Emails.txt","w")
for index,item in enumerate(var):
    f.write(f"{index+1}.{item}")
    f.write("\n")
