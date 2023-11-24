import requests
from bs4 import BeautifulSoup

import re
def Find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]

class discudemy:
    completed = ["Mastering Pointers in C : A Course on Efficient Programming","Programming Network Applications in Java","Bootstrap 5 Course: Build Responsive Websites like a Pro","Bootstrap 4 Basics","Flutter SQLite Database with full project","Azure Pipelines/AppService/StaticWebApp/ASPNET Core/Angular","Linux for Cloud Engineers: A Complete Project Based Learning","SQL Bootcamp: Learn Enough SQL To Be A Professional [2023]","Microsoft SQL Server for Beginners | Crash Course","Python And Flask Framework Complete Course For Beginners","Cloud Computing and Amazon Web Services (AWS) Fundamentals","Java Data Structures and Algorithms Masterclass","WordPress Theme Development from Scratch 2.0","Databases with Python: MySQL, SQLite & MongoDB with Python","Complete SQL & Relational Database Management System","Excel - Microsoft Excel Course Beginner to Expert 2023","SQL- The Complete Introduction to SQL programming","Python And Flask Demonstrations Practice Course","Python And Django Framework And HTML 5 Complete Course 2022","Advanced Microsoft Word With Job Success","Essential Canva Course for Graphics Design Learn in 2 Hour","Data Science: Python for Data Analysis Full Bootcamp","Python Performance Optimization","ChatGPT - Power Your English Language Learning with AI","Building a Dynamic Notebook App with Firebase, and Next.JS","The Ultimate MySQL Crash Course 2023","JavaScript - Basics to Advanced step by step","Make Simple Games with Python","Complete Pandas for Absolute Beginners 2023","React JS Interview Questions & Answers for Beginners [2023]","PHP for Beginners 2023: The Complete PHP MySQL PDO Course","PHP with MySQL 2023: Build 5 PHP and MySQL Projects","HTML5 & CSS3 Complete Course: Build Websites like a Pro","AutoCAD 2023 MasterClass: Produce Amazing Site Plans Quickly","Enhance Lightroom Editing with the Luminar Neo Plugin","AZ-900 Azure Fundamentals practice tests","PHP for Beginners: PHP Crash Course 2023","Master Python using ChatGPT","Asteroids with Python PyGame","Prompt Engineering Professional Certification","Linux Security","CSS Crash Course For Beginners","Python: Object Oriented Programming","Python Data Science with NumPy: Over 100 Exercises","Public Speaking: You Can be a Great Speaker within 24 Hours","Real time Automation+Manual Interview Questions with Answers","Python para no matemáticos: De 0 hasta reconocimiento facial","Cryptocurrency Course: Learn to Make Money Online WORLDWIDE!","Functional Programming + Lambdas, Method References, Streams","Java Multithreading - Concurrency, Parallelism & Performance","GoF Design Patterns - Complete Course with Java Examples","Improving software development productivity","Color Grading and Video Editing with Davinci Resolve 18","Complete Video Creation, YouTube Marketing & ChatGPT Course","Excel Accounting Problem","AZ-900: Microsoft Azure Fundamentals 4 Practice Tests 2023","Ethical Hacking: Introduction to Exploits","ChatGPT SEO Guide: Improve Your SEO Strategy Using ChatGPT","Python Demonstrations For Practice Course","Android MARSHMALLOW - Develop Hands-on Android Apps","XAMARIN: Create Native Cross Platform Apps with C# Codes","3D Architecture with Maya and 3Ds Max","Public Speaking for Beginners","Public Speaking for College Students: Become a Great Speaker","ChatGPT: Make Money with ChatGPT as a New Freelancer","Presentation Skills Training: Great One on One Presentations","Cryptocurrency Guide: Beginner to Advanced","The Complete Meta | Facebook Lead Generation Guide + ChatGPT","Selling on eBay Complete Course - Start an eBay Business","Drupal For Absolute Beginners (2023)","Computer Vision Fundamentals","Learn Crystal Programming","Build a User Web App from Scratch with Vanilla PHP 8+","Android App's Development Masterclass - Build 2 Apps - Java","Reverse Engineering & Malware Analysis in 21 Hours | REMAC+","ChatGPT Coding Express: Fast-Track Coding with ChatGPT","Android Very Basic App Development Course with Java in Hindi","iOS, Swift & SwiftUI - Complete iOS App Development","Quantitative Finance with Python","Portrait Photography for Absolute Beginners","Learn Python Programming: by Building a Facebook ChatBot App","Python Programming: Learn Python by Build a XTwitter Chatbot","The Complete Video Editing Masterclass with Vegas Pro","Unlock your Passive Income with Photography on Unsplash","The complete introduction to cryptocurrencies trading","Project Management Crash Course in 60 Minutes","Python for Deep Learning: Build Neural Networks in Python","Data Manipulation in Python: Master Python, Numpy & Pandas","WordPress Crash Course: Build any Website in Minutes!","JavaScript for Beginners - The Complete introduction to JS","Instagram Marketing 2021: Growth and Promotion on Instagram","C++ Code Like you are in MATRIX : Mastering C++ in 12 Hours","TailwindCSS from A to Z: Master TailwindCSS Quickly","Java Network Programming - Mastering TCP/IP : CJNP+ 2023 JVA","Time Management Mastery: 10X Your Time, Join the New Rich","Beginning Bash Scripting","Master Android by Building 3 Applications in Kotlin Language","Android Course Build 3 Applications from Scratch with Java","Master Android Application Build 3 Applications from Scratch","Build a Backend REST API with Node JS from Scratch","SEO Strategy 2023. SEO training to TOP rank your website!","Digital Marketing Strategist. Unlock your career growth","Google Analytics 4 (GA4): Become a Web Analytics Specialist!","Ubuntu Linux for beginners","CSS Complete Course For Beginners","Figma Design Course 2023. Your Website from Start to Finish","Internet of Things (IoT) : Fundamental Course (101 level)","Git, GitHub & Markdown Crash Course: Learn Git, GitHub & MD","Prompt & AI Engineering Safety Professional Certification","Ethical Hacking: Network Exploitation Basics","Web Analytics with Similarweb: from Basic to PRO!","The Complete Introduction to C++ Programming","Object Oriented Programming in C++ & Interview Preparation","Create your first 3 fully apps with .NET MAUI","Coding Basics: Gentle Intro to Computer Programming","File & Folder Management Using PowerShell","Practical Password cracking - Office files | Ethical Hacking","Olympic Games Analytics Project in Apache Spark for beginner","CSS And Javascript Crash Course","Professional Diploma in Social Media Marketing & Management","Fastest Laravel app building trick","Complete Photography : 21 Courses in 1 [Beginner to Expert]","Deep Learning MasterClass","Git for Beginners","OOP Design Patterns in Python","Spark Machine Learning Project (House Sale Price Prediction)","Dividend Stocks Investing: Generate Monthly Passive Income","T-Shirt Design Masterclass In Photoshop | Sell Your T-Shirt","How to make Video Intro and Outro: A Beginner's Guide","The Ultimate SEO, Social Media, & Digital Marketing Course","Best Master GRE Prep& GMAT Prep Math through Animated Videos","Tally Prime Erp +GST : Certificate Course","The BEST Bitcoin Trading Course for ALL Levels! (2023)","PHP with MySQL 2023: Build Hotel Booking Management System","Master Course : Fundamentals of Machine Learning (101 level)","Master Course in Artificial Intelligence & Deep Learning 3.0","HTML 5,Python,Flask Framework All In One Complete Course","JavaScript And PHP And Python Programming Complete Course","Java And PHP Complete Course","SEO Training: Complete SEO Course & ChatGPT SEO Copywriting","Introduction to Quantum Computing","Convert a one page HTML5 Template to a WordPress Theme","Java Training Complete Course 2022","Lua's Core Syntax (Programming Language)","Create a Movie Streaming Website and OTT App Like Netflix","The Complete DART Programming Guide for Beginners","Autodesk Combustion Training Hands-on","AWS Certified SysOps Administrator – Associate","HR Leadership - Talent Acquisition | Recruitment & Selection","KUBERNETES - Beginners Hands-on Course","HTML and CSS for Beginners 2023","The Complete Digital Marketing Course for Local Businesses","Create a GUI with Python","How to write Best Resume (CV) & Application Covering Letter","NextJS - Build a Full-Stack Authentication with NextAuth","Complete Photography Masterclass: 4 Courses IN 1","CSS, Bootstrap And JavaScript And Python Stack Course","The Complete, Step-By-Step course to Ace your Job Interview","Python For Beginners Course In-Depth","Fast WPF in C# Windows Presentation Foundation for Beginners","The Complete Resume and CV Writing Course: Get the Ideal Job","Talent Acquisition Excellence by Skilled Interview Taking","Java Certification ( Java Oops feature )","Complete PYTHON Programming for Beginners - 2023","Java And C++ Complete Course for Beginners 2022","Online CAT 2023 Exam Preparation Coaching Course for MBA","JavaScript And PHP Programming Complete Course","Communication Skills: Be a Star Presenter on a Panels"]
    @staticmethod
    def getLinks(url:str):
        return BeautifulSoup(requests.get(url).content,'html.parser').find_all('a')

    @staticmethod
    def firstPagediskUdemy(url:str):
        allLinks = discudemy.getLinks(url)
        if "Take Course" in str(allLinks[12]):
            return discudemy.secondPagediskUdemy(allLinks[12].get('href'))
        else:
            return False

    @staticmethod
    def secondPagediskUdemy(url:str):
        allLinks = discudemy.getLinks(url)
        return allLinks[11].get('href')

    @staticmethod
    def checkAvailable(message:str):
        message =message.split('\n')[3][3:]
        print(message)
        if message in discudemy.completed:
            return False
        else:
            return True

    @staticmethod
    def make(message):
        try:
            if discudemy.checkAvailable(message):
                link = discudemy.firstPagediskUdemy(Find(message)[0])
                if link:
                    discudemy.completed.append(link)
                return link
            else:
                return False
        except:
            return False

from telethon.sync import TelegramClient, events

from asyncio import run

api_id = '26989318'
api_hash = '062a6050a2c00efbd633b53c434a4f5b'
session_name = 'my-laptop-script'
phone_number = '+918220853158'
async def channel_info():
    client =  TelegramClient(session_name,api_id,api_hash)

    @client.on(events.NewMessage())
    async def handler(event):
        message = event.message
        sender = await message.get_sender()
        forwardId = 1002102875081
        text = message.text
        media = message.media
        if sender.id==1494678304:
            text = discudemy.make(text)
            if not text:
                print(text)
                return False
            # if media:
            #     await client.send_message(forwardId,message=text,file=media)
            #     print("Media attached. Forwarded with modified caption.")
            # else:
            await client.send_message(forwardId, message=message)
            print(f"Received text message: '{text}' and forwarded as it is.")

    async def list_channels():
        await client.start()
        dialogs = await client.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                print(f"Channel Name: {dialog.title}, Sender ID: {dialog.id}")
    # await list_channels()

    await client.start(phone=phone_number)
    await client.run_until_disconnected()

run(channel_info())
