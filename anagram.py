def func(msg1, msg2):
    #checks if the sorted list of both the strings are same
    if(sorted(msg1)==sorted(msg2)):
        print("The given strings are anagrams")
    else:
        print("The given strings are not anagrams")

msg1 = "silent"
msg2 = "listen"
print("Message 1 is: "+msg1+" and Message 2 is: "+msg2)
func(msg1, msg2)

msg1 = "bad"
msg2 = "dad"
print("Message 1 is: "+msg1+" and Message 2 is: "+msg2)
func(msg1, msg2)

msga = input("Enter msg1 \n")
msgb = input("Enter msg2 \n")
func(msga, msgb)
print("Thank YOU!")