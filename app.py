#calculate the longest word 


def longest_word(sentence):
    word = sentence.split()
    longest = word[0] 
    for words in word:
        if len(words) > len(longest):
            longest = words 
    return longest





sentence = input("Enter a sentence: ")
print(longest_word(sentence))