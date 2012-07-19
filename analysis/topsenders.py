import topsent
from optparse import OptionParser
import random, smtplib, sys, time, urllib
import sqlite3, email, math, imaplib
from dateutil.parser import parse
from datetime import timedelta
from spam import get_spam_contacts
import json
import psycopg2
import re


def get_top_senders(num, startdate, enddate, user, conn):
    c = conn.cursor()
    execCode = ""
    try:
        num = num+1

        # get account id
        c.execute("select accounts.id from accounts, auth_user as au where au.username = %s and au.id = accounts.user_id", (user,))
        aid = c.fetchone()[0]
        
        spam_contacts = get_spam_contacts(aid, conn)

        WHERE = []
        if len(spam_contacts):
            WHERE.append("contacts.id not in (%s)" % ','.join(map(str, spam_contacts)))
        WHERE.append("date >= %s and date < %s")
        WHERE.append("account = %s")
        WHERE.append("emails.fr = contacts.id")
        WHERE.append("contacts.email != %s")
        WHERE = ' and '.join(WHERE)



        sql = """select email, count(*) as c
        from emails, contacts
        where %s
        group by contacts.email
        order by c desc
        limit %s
        """ % (WHERE, num)

        c.execute(sql, (startdate, enddate, aid, user))
        res = c.fetchall()
        print res

    except Exception, e:
        print 'theres an error. we are in the catch block.'
        print execCode        
        print >> sys.stderr, e
        print e

        res = None

    total = 0
    emails = []
    numbers = []
    for item in res:
        total += int(item[1])
        emails.append(item[0])
        numbers.append(item[1])

    #get rid of the current user in the lists
    if user in emails:
        index = emails.index(user)
        emails.remove(user)
        numbers.remove(numbers[index])

    obj = dict()
    obj["labels"] = emails 
    obj["y"] = numbers
    

    return obj



if __name__ == "__main__":
    inputarg = 10
    if len(sys.argv) == 4:
        inputarg = sys.argv[1]
        start = sys.argv[2]
        end = sys.argv[3]
    else:
        sys.stderr.write("Not valid argmuents")
        exit(1)

    conn = sqlite3.connect('../mail.db', detect_types=sqlite3.PARSE_DECLTYPES)
    get_top_senders(10, start, end, conn)

#obj = dict()

#myemails, mynumbers = get_top_senders(int(inputarg))

#obj["x"] = myemails
#obj["y"] = mynumbers

#print json.dumps(obj)

