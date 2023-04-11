'''
Problem 2:
Chit Chat Application - Function:
(a) In few chit-chat programs, there is a limitation on the number of letters that you can send to your family and friends.
Write a function that takes as input the,
message and checks whether the number of letters is less than 200 or above. If the length of the information is less than 200, the chat should be returned.
If the length of the chat is greater than 200, data consisting of only the first 200 characters should be returned.
(b) How one can check if the restriction is on a number of words rather than letters?
Write a function that allows a message with only 30 words.
'''

def restrict_length(msg, max_length):
    if len(msg) <= max_length:
        return msg
    else:
        return msg[:max_length]

def restrict_word_count(msg, max_words):
    words = msg.split()
    if len(words) <= max_words:
        return msg
    else:
        return ' '.join(words[:max_words]) + '...'

message = "Hello, how are you? I hope you're doing well. Just wanted to check in and see how things are going with you. Let's catch up soon!"
restricted_message = restrict_length(message, 200)
print(restricted_message)

restricted_word_count = restrict_word_count(message, 30)
print(restricted_word_count)