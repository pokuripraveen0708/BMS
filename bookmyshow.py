import urllib.request as urllib2
from bs4 import BeautifulSoup
import re
import smtplib
import time

# AGHM - asian gpr
# CPCL -
try:
    site= "https://in.bookmyshow.com/buytickets/war-hyderabad/movie-hyd-ET00107162-MT/" #Replace this your movieandcity url
    date="20191002" #replace the date with the date for which you'd like to book tickets! Format: YYYYMMDD
    site=site+date
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    venue ='AGHM' #this can be found by inspecting the element data-id for the venue where you would like to watch
    show='07:35 PM' #just replace it with your prefered show timing
    delay=300 #timegap in seconds between 2 script runs

    TO = 'pokuri.praveen0708@gmail.com,' #mail id for which you want to get alerted
    # Please add your username and password here, and make sure you
    # toggle allow less secure apps to on
    # https://myaccount.google.com/lesssecureapps?pli=1
    GMAIL_USER = 'pokuri.praveen0708@gmail.com'
    GMAIL_PASS = ''
    SUBJECT = 'WAR bookings started'
    TEXT = 'The tickets are now available for war movie at Asian GPR'

    def send_email(sub,t):
        print("Sending Email")
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(GMAIL_USER, GMAIL_PASS)
        header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
        header = header + '\n' + 'Subject:' + sub + '\n'
        print(header)
        msg = header + '\n' + t + ' \n\n'
        smtpserver.sendmail(GMAIL_USER, TO, msg)
        smtpserver.close()
        print("done")

    req = urllib2.Request(site,headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page,features="html.parser")
    soup2=soup.find_all('div', {'data-online': 'Y'})
    line = str(soup2)
    soup3= BeautifulSoup(line,features="html.parser")
    soup4=soup3.find_all('a', {'data-venue-code': venue})
    line1=str(soup4)
    #soup5=BeautifulSoup(line1,features="html.parser")
    #soup6=soup3.find_all('a', {'data-display-showtime': show})
    #line2=str(soup6)
    result=re.findall('data-availability="A"',line1)
    if len(result)>0:
        print("Available")
        send_email(SUBJECT,TEXT)
    else :
        print("Not available yet")
    #time.sleep(delay)
except Exception as e:
    send_email("error",e)