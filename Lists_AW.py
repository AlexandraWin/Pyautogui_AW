import time
subjects = ['Comp Sci', 'History', 'Spanish', 'Science', 'Math', 'Dance']
for i in subjects:
     if i == "History":
        print ("My favortie subject is " + i + "!!!")
     else:
        print ("I like " + i + "!")\


friends = ['Hedgehogs', 'My Bed', 'Hunter', 'Noah Snapp', 'John', ]

for i in friends:
    print (i.title() + " is awesome!")

myname = ""
letters = [ 'm', 'r', '.', ' ', 'p', 'i', 'c', 'k', 'l', 'e', 's',]

for i in letters:
    myname = myname + i
    print (myname)
    time.sleep(0.5)

print (myname.title())
           

