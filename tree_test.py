def tree(heights):
    greater = 0
    less = 0
    greaterf = 0
    lessf = 0
    for n in range(len(heights)):
        if [n+1] > n:
            greater + 1
            if less > lessf:
                lessf = less
            less = 0
        if [n+1] < n:
            less + 1
            if greater > greaterf:
                greaterf = greater
            greater = 0
        return greaterf and lessf
print(tree([1,3,4,2]))