__author__ = 'root'
letters = "qw ertyuiopasdfghjklzxcvbnm"
vowels = 'aeiou'

for i in letters:
    if i in vowels:
        print("%s is a vowel") % (i)
    else:
        print(i)