#WAP which accepts one character and checks it is Vowel or Consonent.
#Input: a
#Output:Vowel
def main():
    print("Enter a character: ")
    char=input()
    if(len(char)!=1):
        print("Enter Valid Character")

    else:
     if(char=="a" or char=="e" or char=="i" or char=="o" or char=="u" or char=="A" or char=="E" or char=="I" or char=="O" or char=="U"):
        print("Vowel")
     else:
        print("Consonent")
    


if __name__=="__main__":
    main()
