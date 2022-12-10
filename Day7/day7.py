# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1
print(len(it_companies))
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies.update(['update1','update2'])
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)
#4
"""We can remove an item from a set using remove() method. If the item is not 
found remove() method will raise errors,so it is good to check if the item exist 
in the given set. However, discard() method doesn't raise any errors."""
#ex2
#1
joined=A.union(B)
print(A)
print(B)
print(joined)
#2
print(A.intersection(B))
#3
print(A.issubset(B))
#4
print(A.isdisjoint(B))
#5
print(joined,'\n',B.union(A))
#6
print(A.symmetric_difference(B))
#7
del A
del B

#ex3
#1
age_l=list(age)
print(len(age),len(age_l))
#2
"""
string is a single, or a group of words signed by '', or "".
list is a collection which is ordered and changeable(modifiable). Allows duplicate members.
tuple is a collection which is ordered and unchangeable or unmodifiable(immutable). 
Allows duplicate members.
set is a collection which is unordered, un-indexed and unmodifiable, but we can add new items
to the set. Duplicate members are not allowed.
"""
#3
sentence='I am a teacher and I love to inspire and teach people.'
sentence_splited=sentence.split(' ')
print(sentence)
print(sentence_splited, len(sentence_splited))