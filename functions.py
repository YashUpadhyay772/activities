[10:05 pm, 10/04/2023] Raman Pal: '''
Problem 1:
Suppose you are buying something online on amazon.com 
On the website, you get
a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on the item because it's black Friday sales.
Write a function that takes as input the amount of the asset that you are buying and a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result.
'''

def discounted_price(amount, prime_member):
    prime_discount = 0.15
    black_friday_discount = 0.08
    if prime_member:
        amount *= (1 - prime_discount)
    amount *= (1 - black_friday_discount)
    return amount
print(discounted_price(4500,True))
[10:05 pm, 10/04/2023] Raman Pal: '''
Problem 2:
Chit Chat Application - Function:
(a) In few chit-chat programs, there is a limitation on the number of letters that you can send to your family and friends.
Write a function that takes as input the,
message and checks whether the number of letters is less than 200 or above. If the length of the information is less than 200, the chat should be returned.
If the length of the chat is greater than 200, data consisting of only the first 200 characters should be returned.
(b) How one can check if the restriction is on a number of words rather than letters?
Write a function that allows a message with only 30 words.
'''

def msg_length(msg):
    if len(msg) <= 200:
        return msg
    else:
        return msg[:200]

message = "Hello, how are you? …
