# open command is used to open specific file
# mode could be : r (Read), W (Write), a (Append), r+ (Read and Write both)

# file opened in read mode
emp_fp = open("employee.txt", "r")

# for i in emp_fp:
if emp_fp.readable():
    # readlines read read all lines and make one array
    # print(emp_fp.readlines()[0])
    # read all lines at time
    # print(emp_fp.read())
    # readline can read only one line at time it like one pointer line by line
    # print(emp_fp.readline())
    # or we can access through loop
    for i in emp_fp:
        print(i)

emp_fp.close()

# file opened with Write (append) mode
emp_fp = open("employee.txt", "a")
emp_fp.write("\nRohan - HR")
emp_fp.close()

# we can create .html file also
htmlFile = open("index.html","w")
htmlFile.write("<p><b>This is index file</b></p>")
htmlFile.close()

