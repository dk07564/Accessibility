import os

apktool="/apktool.jar"
path_dir = input("경로 입력:")
dirList=[]
dirList=os.listdir(path_dir)
dirList=[i for i in dirList if i.endswith(".apk")]
nameList=[]

try:
    while len(dirList)>0:
        xmlFile = dirList.pop()
        xmlName=xmlFile.replace(".apk", "")
        nameList.append(xmlName)

        if(os.path.exists(xmlName)):
            pass
        else:
            os.system("java -jar " + apktool + " d " + path_dir + "/" + xmlFile)

        # name=nameList.pop(0)
        # xmlDir = name + "/res/layout"
        # fileList = []
        # fileList = os.listdir(xmlDir)
        # fileList = [i for i in fileList if i.startswith("activity")]

    # print(nameList)

except FileNotFoundError:
    print("파일을 찾을 수 없음")