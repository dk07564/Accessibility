from bs4 import BeautifulSoup
from LoadListTest import *
import matplotlib.pyplot as plt
import numpy

viewList=["VideoView", "ImageView", "WebView", "CalendarView", "AdView", "MapView"]
textList=["AutoCompleteTextView", "CheckedTextView", "MultiAutoCompleteTextView"]

widgetList=[]
passList=[]
yPlt=[]
xmlList=[]
accList=[]
# for i in range(len(nameList)):
#     xPlt.append(i)

# print("\n", "<< 어플 이름: ", xmlName, " >>")



#xml파일 찾기
while len(nameList)>0:
    name = nameList.pop(0)
    xmlDir = name + "/res/layout"
    fileList = []
    fileList = os.listdir(xmlDir)
    fileList = [i for i in fileList if i.startswith("activity")]

    print("\n", "<< 어플 이름: ", name, " >>")

    while len(fileList) > 0:
        fileName = fileList.pop(0)

        if(fileName=="activity_main.xml"):
            xmlList.insert(0, "main")
            accList.insert(0, fileName)
        else:
            xmlList.append("")
            accList.append(fileName)

        file = xmlDir + '/' + fileName

        cnt = 0
        passCnt = 0

        #xml파일 크롤링
        try:
            print("\n" + "< 파일 명:", fileName, ">")
            with open(file) as fp:
                bs = BeautifulSoup(fp, "xml")

            list = bs.find_all()
            strList = ", ".join([str(i) for i in list])
            # list = strList.split("\n")
            # print(list)
            # strList = ", ".join(list)
            # print(strList)
            #
            list = strList.split(", ")
            # print(list)
            # print(list)

            #위젯별 분석
            for i in range(len(list)):
                # print(i, list)
                popList = list.pop(0)

                rate = False

                # print(popList, "\n")
                # cnt += 1

                #평가 대상이 아닌 위젯 제거
                if (popList.find("android:id") == -1 or (popList.find("width") or popList.find("height")) == -1 or popList.find("Layout") >= 0):
                    #cnt -= 1
                    popList = ""

                #평가 대상 위젯 평가
                else:
                    cnt += 1

                    #View
                    if (popList.find("View") >= 0 and popList.find("TextView") == -1):
                        # for i in range(len(viewList)):

                            if (popList.find("VideoView")>=0 or popList.find("ImageView")>=0 or popList.find("WebView")>=0
                                    or popList.find("CalendarView")>=0 or popList.find("AdView")>=0 or popList.find("MapView")>=0):
                                # print("Not in ViewList", popList, "\n", viewList[i])
                                if (popList.find("contentDescription") == -1):
                                    finder = popList.split(" ")

                                    for f in range(len(finder)):
                                        IDfinder = finder.pop(0)
                                        ID = "".join(IDfinder)

                                        if (ID.find("</") >= 0):
                                            cnt -= 1

                                        elif (ID.find("<") >= 0):
                                            print("종류:", ID.replace("<", ""))

                                        elif (ID.find("android:id") >= 0):
                                            print("contentDescription이 없는 위젯:", ID)
                                            print("\n")

                                            popList = ""

                                            break

                                else:
                                    finder = popList.split(" ")

                                    for f in range(len(finder)):
                                        IDfinder = finder.pop(0)
                                        ID = "".join(IDfinder)

                                        if (ID.find("android:id") >= 0):
                                            print("통과된 위젯:", ID)
                                            passCnt += 1
                                            print("\n")

                                            popList = ""
                                            break


                                # else:
                                #     cnt -= 1
                                #     popList = ""
                                #
                                #     break

                            else:
                                cnt -= 1
                                popList=""
                                break

                    # TextView
                    elif (popList.find("TextView") >= 0):
                        for i in range(len(textList)):

                            if (rate == True):
                                break

                            if (popList.find(textList[i]) >= 0):
                                if (popList.find("hint") == -1):
                                    finder = popList.split(" ")

                                    for f in range(len(finder)):
                                        IDfinder = finder.pop(0)
                                        ID = "".join(IDfinder)

                                        if (ID.find("android:id") >= 0):
                                            print("hint가 없는 " + textList[i] + ": ", ID)
                                            print("\n")

                                            break

                                else:
                                    finder = popList.split(" ")

                                    for f in range(len(finder)):
                                        IDfinder = finder.pop(0)
                                        ID = "".join(IDfinder)

                                        if (ID.find("android:id") >= 0):
                                            print("통과된 " + textList[i] + ": ", ID)
                                            passCnt += 1
                                            print("\n")

                                            break

                            else:
                                if (popList.find('sp"') == -1):
                                    finder = popList.split(" ")

                                    for f in range(len(finder)):
                                        IDfinder = finder.pop(0)
                                        ID = "".join(IDfinder)

                                        if (ID.find("android:id") >= 0):
                                            print("단위가 sp가 아닌 TextView" + ": ", ID)
                                            print("\n")

                                            rate = True
                                            break

                                else:
                                    finder = popList.split(" ")

                                    for f in range(len(finder)):
                                        IDfinder = finder.pop(0)
                                        ID = "".join(IDfinder)

                                        if (ID.find("android:id") >= 0):
                                            print("통과된 " + "TextView" + ": ", ID)
                                            passCnt += 1
                                            print("\n")

                                            rate = True
                                            break


                    # EditText 평가
                    elif (popList.find("EditText") >= 0):
                        if (popList.find("hint") == -1 and popList.find("labelFor") == -1):
                            finder = popList.split(" ")

                            for f in range(len(finder)):
                                IDfinder = finder.pop(0)
                                ID = "".join(IDfinder)

                                if (ID.find("android:id") >= 0):
                                    print("통과되지 않은 EditText:", ID)
                                    print("\n")

                                    break

                        else:
                            finder = popList.split(" ")

                            for f in range(len(finder)):
                                IDfinder = finder.pop(0)
                                ID = "".join(IDfinder)

                                if (ID.find("android:id") >= 0):
                                    print("통과된 EditText:", ID)
                                    passCnt += 1
                                    print("\n")

                                    break

                        # CheckBox 평가
                    elif (popList.find("CheckBox") >= 0):
                        if (popList.find("hint") == -1):
                            finder = popList.split(" ")

                            for f in range(len(finder)):
                                IDfinder = finder.pop(0)
                                ID = "".join(IDfinder)

                                if (ID.find("android:id") >= 0):
                                    print("hint가 없는 CheckBox:", ID)
                                    print("\n")

                                    break

                        else:
                            finder = popList.split(" ")

                            for f in range(len(finder)):
                                IDfinder = finder.pop(0)
                                ID = "".join(IDfinder)

                                if (ID.find("android:id") >= 0):
                                    print("통과된 CheckBox:", ID)
                                    passCnt += 1
                                    print("\n")

                                    break


                    else:
                        if (popList.find("contentDescription") == -1):
                            finder = popList.split(" ")

                            for f in range(len(finder)):
                                IDfinder = finder.pop(0)
                                ID = "".join(IDfinder)

                                if (ID.find("</") >= 0):
                                    pass
                                    cnt -= 1

                                if (ID.find("<") >= 0):
                                    print("종류:", ID.replace("<", ""))

                                if (ID.find("android:id") >= 0):
                                    print("contentDescription이 없는 위젯:", ID)
                                    print("\n")

                                    break

                        else:
                            finder = popList.split(" ")

                            for f in range(len(finder)):
                                IDfinder = finder.pop(0)
                                ID = "".join(IDfinder)

                                if (ID.find("android:id") >= 0):
                                    print("통과된 위젯:", ID)
                                    passCnt += 1
                                    print("\n")

                                    break

                        # print(popList)

                    for i in range(len(viewList)):
                        if (popList.find(viewList[i]) >= 0):
                            if (popList.find("contentDescription") == -1):
                                finder = popList.split(" ")

                                for f in range(len(finder)):
                                    IDfinder = finder.pop(0)
                                    ID = "".join(IDfinder)
                                    if (ID.find("android:id") >= 0):
                                        print("contentDescription이 없는 " + viewList[i] + ": ", ID)

                                        break

                            else:
                                finder = popList.split(" ")

                                for f in range(len(finder)):
                                    IDfinder = finder.pop(0)
                                    ID = "".join(IDfinder)

                                    if (ID.find("android:id") >= 0):
                                        print("통과된 " + viewList[i] + ": ", ID)
                                        passCnt += 1
                                        print("\n")

                                        break

                #
                #             # pass
                #             # cnt -= 1
                #
                #
                #
                #             elif (popList.find("labelFor") == -1):
                #                 finder = popList.split(" ")
                #
                #                 for f in range(len(finder)):
                #                     IDfinder = finder.pop(0)
                #                     ID = "".join(IDfinder)
                #
                #                     if (ID.find("android:id") >= 0):
                #                         print("label이 없는 " + "TextView" + ": ", ID)
                #                         print("\n")
                #

                #
                # elif
                #
                # else:
                #     if
                #
                # print("평가한 위젯 수:", cnt)
                # print("통과된 위젯 수:", passCnt)
                # print("\n")



        except FileNotFoundError:
            print("파일을 찾을 수 없음")

        print("평가한 위젯 수:", cnt)
        print("통과된 위젯 수:", passCnt)
        print("\n")

        widgetList.append(cnt)
        passList.append(passCnt)