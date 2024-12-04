# Create a program that will accept a word and output the word one letter at a time in reverse.
word = input('please enter a word')
drow=''
for i in range(len(word)):
    drow=drow+word[len(word)-1-i]
    print(drow)
 
# temporary variable string thing so that you can store some letters, then link it to the loop's variable
# print it