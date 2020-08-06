import os

apktool="/apktool.jar"
file_dir = input()
dirList=[]

try:
    dirList=os.listdir(file_dir)
    dirList=[i for i in dirList if i.endswith(".apk")]
    xmlFile=dirList.pop()
    os.system("java -jar " + apktool + " d " + file_dir + "/" + xmlFile)
    xmlFile=xmlFile.replace(".apk", "")

    print(xmlFile)

    xmlDir = xmlFile + "/res/layout"
    xmlList = []
    xmlList = os.listdir(xmlDir)
    xmlList = [i for i in xmlList if i.startswith("activity")]
    print(xmlList)

except FileNotFoundError:
    print("파일을 찾을 수 없음")