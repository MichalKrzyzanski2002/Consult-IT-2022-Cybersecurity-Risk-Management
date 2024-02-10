import win32file
import ctypes

def loadWordList():
    file = open("ExamplePhishingWarningWordList.txt","r", encoding="utf-8")
    content = file.read()
    content_list = content.split("\n")
    #print(content_list)
    file.close()
    return content_list

def loadEmailBlacklist():
    file = open("EmailBlacklist.txt","r", encoding="utf-8")
    content = file.read()
    content_list = content.split("\n")
    file.close()
    return content_list

def loadEmailWhitelist():
    file = open("EmailWhitelist.txt","r", encoding="utf-8")
    content = file.read()
    content_list = content.split("\n")
    file.close()
    return content_list

if __name__ == '__main__':
    word_list = loadWordList()
    email_blacklist = loadEmailBlacklist()
    email_whitelist = loadEmailWhitelist()

    email = open("ExampleEmailToCheck.txt", "r", encoding="utf-8")
    content = email.read()

    MB_OK = 0x0
    ICON_EXLAIM=0x30



    for x in email_blacklist:
        if content.__contains__(x):
            print("Message hidden and IT department informed")
            #SENDING INFORMATION TO THE IT DEPARTMENT
            #HIDING THE EMAIL FROM THE EMPLOYEE
            exit()


    internalEmail = False
    for x in email_whitelist:
        if content.__contains__(x):
            internalEmail = True
    if internalEmail == False:
        ctypes.windll.user32.MessageBoxW(0, "This email address is not part of the EKLAMOT company. Be cautious of any files sent or requests made.", "WARNING", MB_OK|ICON_EXLAIM)

    wordsFound = []
    for x in word_list:                                                             #Informing workers about potential SPAM or phishing
        if content.__contains__(x) or content.__contains__(x.swapcase()) or content.__contains__(x.casefold()):
            wordsFound.append(x)

    if(len(wordsFound) >= 5):                                                        #Significant phishing or spam risk
        print("Message hidden and IT department informed")
        #SENDING EMAIL TO THE IT DEPARTMENT
        #Hiding EMAIL the from the user
    else:
        ctypes.windll.user32.MessageBoxW(0, "Possible phishing attempt, words identified: " + wordsFound.__str__() +". \nMake sure the address of the sender is EXACTLY correct, don't download attached files, don't click on any links, unless you are ABSOLUTLY SURE that the sender is trustworthy. \nContact the sender personally to confirm any requests.\n For more info, visit the phishing help centre on our website.", "WARNING", MB_OK|ICON_EXLAIM)
