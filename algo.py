# Excercise 1

words = ['this' , 'is', 'a', 'sentence', '.']

def backwards(new_num, x, y):
    new_num[x], new_num[y] = new_num[y], new_num[x]

def wardback(blist):
    left = 0
    right = len(blist) -1
    while left < right:
        blist[left], blist[right] = blist[right], blist[left]
        left += 1
        right -= 1
    return blist
print(words)
wardback(words)

# Notes were very helpful for this one, I wrapping my head around the synatx for these algorithms.

# Excercise 2

def word_count(a_text):
    count_word = {}
    strings = a_text.split()
    
    for word in strings:
        if word in count_word:
            count_word[word] += 1
            
        else:
            count_word[word] = 1
            
    return count_word

a_text ='In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
counted = word_count(a_text)
print(counted)



# This one was pretty straight forward, at first it was only printing {'In':1} but it was because I did'nt indent the return properly.


# Excercise 3

# a_list = [1,5,67,89,4,53,2,6]

def search_list(a_list4, search):
    for num in a_list4:
        if num == search:
            return True
    return False
   

a_list4 = [1,5,67,89,4,53,2,6]
search_num = 99

my_num = search_list(a_list4, search_num)
if my_num:
    print(search_num)
    
else:
    print("not here.")
        
#  time complexity - O(8)       