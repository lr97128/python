#关键字参数要放在后面，关键字收集参数放在最后面


def stu(name, age, *args, hobby="lily", **kwargs):
    '''
    文档
    :param name:
    :param age:
    :param args:
    :param hobby:
    :param kwargs:
    :return:
    '''

    if name is not None:
        print("name:" + name + " ", end=" ")
    if age is not None:
        print("age:" + age + " ", end=" ")
    print("hobby:" + hobby + " ", end=" ")
    if args is not None:
        for item in args:
            print("args:" + item + " ", end=" ")
    if kwargs is not None:
        for k,v in kwargs.items():
            print("kwargs: " + k + " ---- " + v)
    print("")


if __name__ == "__main__":
    stu("1", "2", "3")
    stu(name="1",age="2")
    stu("1", "2", "3", "lucy", num="4 girlfriends")
#    help(json)
    x = 100
    y = 200
    print(eval("x+y"))
    exec("print(x+y)")
    list1 = []
    print(list1)
    c = "I love wangxiaojing"
    for i in c:
        print(i)
    a = [i for i in range(1,21)]
    print(a)
    b = [j for j in a if j % 2 == 0]
    print(b)

    str1 = "45"
    print(str1)
    i1 = int(str1)
    print(i1)