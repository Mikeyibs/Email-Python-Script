#!/usr/bin/env python 
import numpy
import smtplib

count = 8
username = "----------------"
password = "----------------" #Requires an app password setup for a gmail account

partcipants = { #Fake Data
    'name': {
        1 : 'John',
        2 : 'Leo',
        3 : 'Mikey',
        4 : 'Jack',
        5 : 'Kyle',
        6 : 'Naab',
        7 : 'Juliette',
        8 : 'Karly'
    },

    'email': {
        1 : 'john@gmail.com',
        2 : 'leo@gmail.com',
        3 : 'mikey@gmail.edu',
        4 : 'jack@gmail.com',
        5 : 'kyle@gmail.com',
        6 : 'naab@gmail.net',
        7 : 'juliette@gmail.com',
        8 : 'karly@gmail.com',
    },

    'shirt_size': {
        1 : 'large',
        2 : 'large',
        3 : 'large',
        4 : 'large',
        5 : 'large',
        6 : 'large',
        7 : 'large',
        8 : 'large',
    }
}

def generateMathes():
    s = [i for i in range(1, count+1)]
    a = numpy.random.choice(s, count, replace=False)
    
    return a

def sendEmails(a):
    try:
        smpt = smtplib.SMTP('smtp.gmail.com', 587)
        smpt.starttls()
        smpt.login(username, password)
        
        for i in range(len(a)-1) : 
            send_username = partcipants['email'].get(a[i])
            message = 'You Are Getting a Shirt for --> ' + partcipants['name'].get(a[i+1]) + '\n Shirt Size --> ' + partcipants['shirt_size'].get(a[i+1])
            smpt.sendmail(username, send_username, message)
        
        smpt.quit()
        print("Email Sent Successfully!\n")
    except Exception as ex:
        print(ex)



def main():
    a = generateMathes()
    sendEmails(a)

main()