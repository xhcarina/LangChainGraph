def openLock(deadends, target) -> int:
        if target == '0000':
            return 0

        thres = []
        counts = []
        inter = []
        for j in range(4):
            for i in range(len(deadends)):
                inter.append(deadends[i][j])
                thres.append(deadends[i][j])
            counts.append(inter)
            inter = []
        

        print(counts)
        # order
        for i, num in enumerate(target):
            #print(counts[i])
            if num > min(set(counts[i])) and num < max(set(counts[i])):
                return -1

        counter = 0
        set(thres)
        # 4, 5
        for num in target:
            if int(num) <= 4 and num <= min(thres):
                counter += int(num)
            if int(num) >= 5:
                counter += 10 - int(num)
        return counter


deadends=["0201","0101","0102","1212","2002"]
target="0202"


openLock(deadends, target)


            