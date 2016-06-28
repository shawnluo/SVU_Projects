import os


def InsPic():
    path = os.getcwd()

    fileList = os.listdir(path)

    i = 1
    for file in fileList:
        ext = os.path.splitext(file)[1]
        if ext.strip() == '.jpg':
            # os.rename(file, str(i) + r'.jpg')
            i = i + 1

    f = open(r'Index.html', 'w+')

    f.write('<?xml version = "1.0" encoding = "UTF-8"?>\n')

    for i in range(1, i):
        fileName = str(i) + r'.jpg'
        image = r'<img src="' + fileName + r'">'
        f.write(image)

    f.close()

InsPic()