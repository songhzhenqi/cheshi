import random
while 1:
    x = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
    # 每一位上进行0-9的随机数选择
    if any([x[0] == x[1], x[0] == x[2], x[0] == x[3], x[1] == x[2], x[1] == x[3], x[2] == x[3]]):
        # 把4位数字进行比较如果有重复则跳过并继续循环
        pass
    else:
        break
print("数组查询请输入1，数值重置请输入2，数组修改请输入3")
while 1:
    y = input("请输入4位不重复的阿拉伯数字：")
    if y == "":
        # 输入数字位数不够不进入循环
        print("输入为空！！")
        pass
    elif 3 < int(y) <= 999:
        print("输入阿拉伯数字位数不够！")
        pass
    elif len(y) > 4:
        print("输入阿拉伯数字位数过长！")
        pass
    else:
        y = int(y)
        if int(y) == 1:
            # 查询数组功能
            print("您所查询的数组是", x)
        elif int(y) == 2:
            # 重置数组功能
            while 1:
                x = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
                # 每一位上进行0-9的随机数选择
                if any([x[0] == x[1], x[0] == x[2], x[0] == x[3], x[1] == x[2], x[1] == x[3], x[2] == x[3]]):
                    # 把4位数字进行比较如果有重复则跳过并继续循环
                    pass
                else:
                    print("已重置")
                    break
        elif int(y) == 3:
            # 修改数组功能
            while 1:
                n = input("请输入要修改第几个数字，输入0可退出修改页面：")
                if n == "" or int(n) > 4:
                    # 直接回车就跳过
                    print("输入位数错误或者输入为空！！请输入正确的数字位置")
                    pass
                elif int(n) == 0:
                    print("已退出修改！！")
                    break
                else:
                    if int(n) == 1 or 2 or 3 or 4:
                        x[int(n) - 1] = int(input("请输入修改的数字："))
                    if any([x[0] == x[1], x[0] == x[2], x[0] == x[3], x[1] == x[2], x[1] == x[3], x[2] == x[3]]):
                        # 把4位数字进行比较如果有重复则跳过并继续循环
                        print("提示：数字有重复请重新修改！！！如果有疑问退出后请，按1查询具体重复。")
                        pass
                    elif x[int(n)-1] > 9:
                        print("提示：数字不在0-9区间内，请重新修改！！！")
                        pass
                    else:
                        print("修改成功！")
                        break
        else:
            z = [int(y / 1000), int((y / 100) % 10), int((y / 10) % 10), int(y % 10)]
            # 把每一位数提取出来用数列进行保存
            (i, j) = (0, 0)
            for b in range(0, 4):
                if x[b] == z[b]:
                    # 相似的记作A+1
                    i += 1
                else:
                    if any([x[b] == z[0], x[b] == z[1], x[b] == z[2], x[b] == z[3]]):
                        # 如果与其他任何一位相似B+1
                        j += 1
            if i == 4:
                print("%dA%dB恭喜你猜中了!" % (i, j))
                break
            else:
                print("%dA%dB猜错了，请再接再厉" % (i, j))






