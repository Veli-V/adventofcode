import sys
sys.setrecursionlimit(5500)

path = "input.txt"
#path = "test2.txt"

with open(path, 'r') as f:
    data = list(map(int, f.read().split(" ")))

print("alussa:               " + str(data))


def countMeta( nums ):
    result = 0
    childs = nums.pop(0)
    metas = nums.pop(0)
    print("childs: " + str(childs) + " metas: " + str(metas))
    if childs == 0:
        print("lapsia on nolla")
        for i in range(0,metas):
            pop = nums.pop(0)
            print(str(i) + " popataan lapsetta " + str(pop))
            result += pop
        return result
    else:
        for i in range(0,childs):
            print("lapsia on viakka kuinka " + str(i) + "/" + str(childs))
            print("lähetetään eteenpäin: " + str(nums))
            result += countMeta(nums)
            print("Arvo palasi, summa nyt: " + str(result))
    print("popataan listasta: " + str(nums))
    for i in range(0,metas):
        pop = nums.pop(0)
        print(str(i) + " popataan lopussa " + str(pop))
        result += pop
    return result

answer = countMeta(data)
print()
print("Vastaus: " + str(answer))
