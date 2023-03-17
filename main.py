# This is a sample Python script.
import numpy as np
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

name_ch = ["他"]
name_en = ["he "]
tense_ch = ["做"  ,"做了","正在做",   "当时正在做","已经做了","当时已经做了","当时没做完现在还在做","将做"]
tense_en = ["does","did","is doing","was doing","has done","had done","has been doing","will do"]
# print(len(tense_ch))  8

def printRandomTense():
    # Use a breakpoint in the code line below to debug your script.
    i = np.random.randint(0,8)
    # print(i)
    print(name_en[0]+tense_en[i])  # Press Ctrl+F8 to toggle the breakpoint.
    return i

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while(1):
        ii = printRandomTense()
        print(name_ch)
        print(tense_ch)
        print()
        str = input("请输入：");
        print("你输入的内容是: ", str)
        print("正确答案是：", name_ch[0]+tense_ch[ii])
        if str == (name_ch[0]+tense_ch[ii]):
            print("success")
        else:
            print("false")

        print("#########################")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
