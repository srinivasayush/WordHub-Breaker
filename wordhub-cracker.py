from itertools import permutations
from itertools import combinations
import enchant
import pyautogui as gui
import time
from selenium import webdriver

op = webdriver.ChromeOptions()

chrome = webdriver.Chrome('./chromedriver.exe', options=op)
english = enchant.Dict("en_US")
liperm = []
letters2 = []
licombfinal = []
final = []
randcount = 0
timer = int(input("Please enter the number of seconds you would like to wait for: "))
string = ""
chrome.get("https://wordhub.com/?fca=1&success=0#/")
while(timer >= 0):
    time.sleep(1)
    print("The code will start running in: "+str(timer)+" seconds")
    timer = timer-1
# Gets letters from https://wordhub.com/?fca=1&success=0#/


def letter_identifier():
    while(True):
        try:
            letters = []
            count = 0
            lowerlimit = 110
            spans = chrome.find_elements_by_tag_name('span')
            for span in spans:
                text = span.get_attribute('innerHTML')
                print("The line number is: "+str(count))
                print(text)
                if(len(text) == 1 and text.isalpha() and count > lowerlimit):
                    letters.append(text)
                count += 1
                if(len(letters) == 7):
                    break
            print(letters)
            if(len(letters) > 3):
                break
        except:
            pass
    return letters


def allPermutations(str):

    # Get all permutations of string str
    permList = permutations(str)

    # insert all permutations into a list
    for perm in list(permList):
        liperm.append(''.join(perm))


def allCombinations(string, integer):

    # Get all combinations of string
    combList = combinations(string, integer)

    # insert all combinations into a list
    for comb in list(combList):
        licombfinal.append(''.join(comb))


letters2 = letter_identifier()

# Putting the letters from the list into a string
for letter in letters2:
    string = letter+string[0:]

i = len(string)

while(i > 2):
    allCombinations(string, i)
    for j in licombfinal:
        allPermutations(j)
    i = i-1


for k in liperm:
    checked = english.check(k)
    if(checked == True):
        final.append(k)
        if((final.count(k) > 1)):
            final.pop(-1)

outputlist = final[::-1]


for word in outputlist:
    randcount = 0
    gui.typewrite(word)
    print(word)
    while(randcount < (len(word))):
        gui.press('backspace')
        randcount = randcount+1
