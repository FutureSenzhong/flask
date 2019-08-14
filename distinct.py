
def distinct_ab(file_name_a, file_name_b):
    str1 = []
    str2 = []
    str_dump = []
    with open("{}".format(file_name_a), 'r') as fa, \
        open("{}".format(file_name_b), 'r') as fb, \
        open("不同的文件.txt", 'w+') as fc,\
        open("相同的文件.txt", 'w+') as fd:

        # 将A.txt的内容逐行读到str1中
        for line in fa.readlines():
            str1.append(line.replace("\n", ''))
        # 将B.txt中的内容逐行读到str2中
        for line in fb.readlines():
            str2.append(line.replace("\n", ''))

        # 将两个文件中重复的行，添加到str_dump中
        for i in str1:
            if i in str2:
                str_dump.append(i)

        # 将两个文件的行合并，并去重
        str_all = set(str1 + str2)

        # 将重复的行，在去重的合并行中，remove掉，剩下的就是不重复的行了
        for i in str_dump:
            fd.write(i + '\n')
            if i in str_all:
                str_all.remove(i)
        # 写行文件中
        for i in list(str_all):
            fc.write(i + '\n')

    print('提取{}文件和{}文件的不同文件成功'.format(file_name_a, file_name_b))


if __name__ == '__main__':
    print('******************程序开始********************')
    print('本程序可以比较两个文件，并将不同的内容提取单独保存')
    print('                                       ')
    while True:
        try:
            print('请确保需要对比提取的两个文件与程序在同一目录')
            a = str(input('请输入第一个文件名称和后缀并回车：'))
            b = str(input('请输入第二个文件名称和后缀并回车：'))
            distinct_ab(a, b)
            print('                                       ')
            print('***************程序结束*****************')
            break
        except :
            print('文件不存在,输入有误，请重新输入！！！')
            q = int(input('输入0退出程序，输入1继续:'))
            if q == 0:
                print('                                       ')
                print('******************程序结束********************')
                break
            else:
                continue
