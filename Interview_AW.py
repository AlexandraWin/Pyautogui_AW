#interview Function
def question (q):
    global answer
    answer = input (q)
    print (answer)

question ("What's you name  ")

question ("Who are the members of your family?  ")

question ("what is your favorite subject   ")
if answer == "History":
    print ("I like history as well, American History is my favorite")

question ("What do you like to do during the summer?   ")
if answer == "Summer Camp":
    question ("what is you favorite part of camp")
    print ("Thats sounds like so much fun")

question ("What is your favotie extra curricular activity")
print ("I love to dance and preform")

question ("what is your favorite sport")
if answer == "competitive Shopping":
    print ("Wow! thats sounds intense!")
    
