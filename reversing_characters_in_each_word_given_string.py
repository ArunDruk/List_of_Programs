''' out = "sihT si ot eton" '''
mystr = "This is to note"
new_list = mystr.split(" ")
new_str = ""
def rev_str(s):
    s1=""
    for i in s:
        s1= i +s1
    return s1

for i in new_list:
    s2 = rev_str(i)
    new_str = new_str +" " + s2

print(new_str)