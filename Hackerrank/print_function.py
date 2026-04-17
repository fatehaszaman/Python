# The included code stub will read an integer,n, from STDIN.
# Without using any string methods, try to print the following:
# 123.. n
# Note that "..." represents the consecutive values in between.


# Time: O(n)
# Space: O(1)

if __name__ == '__main__':
    n = int(input())
    string= ""
    if 0<n<151:
        for i in range(1,n+1):
            string+= str(i)
        print(string)
