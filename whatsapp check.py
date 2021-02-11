import pyttsx3
import mysql.connector
from mysql.connector import Error


def Talk(speech):
    engine = pyttsx3.init()
    voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice',voice)
    engine.setProperty('rate', 145)
    engine.say(speech)
    engine.runAndWait()

def start():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='jyothisclassdata',
                                             user='root',
                                             password='')
        if connection.is_connected():
            sql_select_Query = "select * from data WHERE CLASS='XII' ORDER BY STUDENT_NAME ASC"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            for row in records:
                print()
                #print("Appending ", row[2], )
                #print("Admission Number = ", row[1])
                #print("VCODE = ", row[3])
                print()
                Talk("Name : "+row[4]+".")
                Talk("Number : "+str(row[12]))
                   # createmessage(number, classD, row[2], row[1], row[3])
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

start()