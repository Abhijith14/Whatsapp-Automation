import pyautogui
import time
import pyperclip
import pyttsx3
import mysql.connector
from mysql.connector import Error

def Talk(speech):
    engine = pyttsx3.init()
    voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice',voice)
    engine.say(speech)
    engine.runAndWait()


def autoW(msg, num):
   # num = ['919446411921', '919446411977', '917025439951', '918921863040', '918921650122', '919946883500', '918589024902']

    link1 = "https://api.whatsapp.com/send?phone="
    link2 = "&text=&source=&data=&app_absent="
    #print(pyautogui.position())

   # msg = "Dear children,\n 📗Click on the link given below. Use admission number and the verification code given below to view your details\n📕 Thoroughly check your details( Students Name, Father's Name, Mother's Name, Date of Birth and Subjects) to be given for CBSE Registration.\n📘 Upload the signatures of student, father and mother in the space provided. ( If any one/two person is not available , the other person can repeat their signature in the concerned place.\nFor eg: If father is not available, mother can put both the signature)\n📙Aadhar Number and Phone Number is compulsory for CBSE registration. So Please enter correct numbers\n📘If there is any change or correction, please specify it in the remarks column.\n📕Check and confirm the data entered before Submission.\nRemember this data will be uploaded to CBSE and making changes in future is difficult\nLink : \nName : \nAdmission Number : \nVerification Code : \nFor further queries, contact : 8589024902"

    pyperclip.copy(msg)


    for i in range(1):
       # for j in num:
            url = link1+str(num)+link2
            pyautogui.click(-2707, 130)
            pyautogui.hotkey("ctrl", "a")
            pyautogui.keyDown("delete")
            pyautogui.typewrite(url)
            pyautogui.keyDown("enter")
            time.sleep(1.5)
            pyautogui.click(-1710, 808)
            time.sleep(1)
            pyautogui.click(-1725, 988)
            time.sleep(15)
            pyautogui.hotkey("ctrl", "v")

            pyautogui.keyDown("enter")
            time.sleep(2)


d = 0
def createmessage(W, C, N, A, V):
    msg1 = "Dear children,\n📗Click on the link given below. Use admission number and the verification code given below to view your details\n📕 Thoroughly check your details( Students Name, Father's Name, Mother's Name, Date of Birth and Subjects) to be given for CBSE Registration.\n📘 Upload the signatures of student, father and mother in the space provided. ( If any one/two person is not available , the other person can repeat their signature in the concerned place.\nFor eg: If father is not available, mother can put both the signature)\n📙Aadhar Number and Phone Number is compulsory. So Please enter correct numbers\n📘If there is any change or correction, please specify it in the remarks column.\n📕Check and confirm the data entered before Submission.\nRemember this data will be uploaded to CBSE and making changes in future is difficult\nLink : http://jyothiscentralschool.com/live/StudentData/ \n"
    msg2 = "Name : "+N+"\nClass : "+C+"\nTo Login,\nAdmission Number : "+str(A)+"\nVerification Code : "+str(V)+"\nFor further queries, contact : 8589024902"
    msg = msg1 + msg2
    print(msg)
    print(W)
    #num = ['919446411921', '919446411977', '917025439951', '918921863040', '918921650122', '919946883500','918589024902']
    #global d

    autoW(msg, W)
    #Talk("Admission "+str(A) + ". Name : "+N)
   # d = d + 1
   # if d == 7:
  #      exit()



def startmiss():
    miss = [1234,1391,1290,3376,1266,1417,1227,3427]
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='jyothisclassdata',
                                             user='root',
                                             password='')
        if connection.is_connected():
            for val in miss:
                sql_select_Query = "select * from admin WHERE ADNO="+str(val)
                cursor = connection.cursor()
                cursor.execute(sql_select_Query)
                records = cursor.fetchall()
                for row in records:
                    print()
                    #print("Appending ", row[2], )
                    #print("Admission Number = ", row[1])
                    #print("VCODE = ", row[3])
                    mycursor = connection.cursor()
                    sqlcheck = "SELECT * FROM data where ADMISSION_NO="+str(row[1])
                    #print(sql)
                    mycursor.execute(sqlcheck)
                    myrecords = mycursor.fetchall()
                    for val in myrecords:
                        number = val[12]
                        classD = val[7]+" "+val[8]
                        createmessage(number, classD, row[2], row[1], row[3])
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




def startmain():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='jyothisclassdata',
                                             user='root',
                                             password='')
        if connection.is_connected():
            sql_select_Query = "select * from admin"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            for row in records:
                print()
                #print("Appending ", row[2], )
                #print("Admission Number = ", row[1])
                #print("VCODE = ", row[3])
                mycursor = connection.cursor()
                sqlcheck = "SELECT * FROM data where ADMISSION_NO="+str(row[1])
                #print(sql)
                mycursor.execute(sqlcheck)
                myrecords = mycursor.fetchall()
                for val in myrecords:
                    number = val[12]
                    classD = val[7]+" "+val[8]
                    createmessage(number, classD, row[2], row[1], row[3])
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


startmiss()