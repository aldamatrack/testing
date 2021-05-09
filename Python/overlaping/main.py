

with open("result.txt", "w") as result:
    with open("list1.txt", "r") as t1:
        with open("list2.txt", "r") as t2:
            set1 = set(t1.read().split())
            set2 = set(t2.read().split())

            intersection = set1.intersection(set2)
            a = []
            print (intersection)
            for i in intersection:
                result.write(i)
                result.write("\n")
