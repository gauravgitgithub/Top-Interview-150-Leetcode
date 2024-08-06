import sys


class Palindrome:
    def isPalindrome(self, str):
        if str == str[::-1]:
            print("Palindrome")
        else:
            print('Not a palindrome')
            
    def isPalindrome2(self, str):
        for i in range(0, int(len(str)/2)):
            if str[i] != str[len(str) - i - 1]:
                print("Not a palindrome")
                break
        print("Palindrome")
            

if len(sys.argv) != 2:
    print("Usage: python script.py <number>")
    sys.exit(1)            

try:
    str = sys.argv[1]
except ValueError:
    print("Enter a valid string")
    sys.exit(1)
    

p = Palindrome()
p.isPalindrome(str)
p.isPalindrome2(str)