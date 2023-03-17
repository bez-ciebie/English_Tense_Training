import winsound
import requests

# This is a sample Python script.
import numpy as np
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

name_ch = ["他"]
name_en = ["he "]
tense_ch = ["做"  ,"做了","正在做",   "当时正在做","已经做了","当时已经做了","当时没做完现在还在做"]
tense_en = ["does","did","is doing","was doing","has done","had done","has been doing"]
# print(len(tense_ch))  8

def playRandomTense():
    i = np.random.randint(0,7)
    filename = str(i)+".wav"
    # print(filename)
    winsound.PlaySound(filename, winsound.SND_FILENAME)
    return i

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while(1):
        ii = playRandomTense()

        print(name_en)
        print(tense_en)
        print("press q for exit! ")
        print()
        answer = input("请输入英文：")
        print("你输入的内容是: ", answer)
        print("正确答案是：", name_en[0]+tense_en[ii])
        if answer == (name_en[0]+tense_en[ii]):
            print("success")
        elif answer == "q":
            print("exit")
            break
        else:
            print("false")

        print("###########################################################")