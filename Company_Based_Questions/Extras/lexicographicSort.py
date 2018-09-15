def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    l.sort()
    print(*l,sep='\n')
main()