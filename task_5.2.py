list1 = [1,2,3,4,5,6,7,8,9,10]
print('Original list :',list1)

a = list1[0:5]
print('Extracted first five elements :',a)

list1.reverse()
b = list1[5:]
print('Reversed extracted elements :',b)
