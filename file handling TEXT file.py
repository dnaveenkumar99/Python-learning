#write operations
# x=open('sam1.txt','w')
# x.write('core python')
# x.close()
#
# x=open('sam2.txt','w')
# x.writelines(['python\n','java\n','JS\n'])
# x.close()

#write operations on already existing file
# x=open('sam1.txt','w')
# x.write('hello')
# x.close()

#using with key word
# with open(r'C:\Users\dnave\OneDrive\Desktop\sam3.txt','w') as a:
#     a.write('file handling')

# import os
#
# path = r'C:\Users\dnave\OneDrive\Desktop\sam3.txt'
#
# with open(path, 'w') as a:
#     a.write('file handling')
#
# print("File created at:", os.path.abspath(path))
# print("File exists:", os.path.exists(path))

# #read operations
# with open('sam2.txt','r') as a:
#     res=a.read()
#     print(res)
#
# #readline operations
# with open('sam2.txt','r') as a:
#     res=a.readline()
#     res1=a.readline()
#     print(res)
#     print(res1)
# with open('sam1.txt','r+') as a:
#      res=a.read()
#      print(res)
#      a.write('pentagon space')

# with open('sam1.txt','r+') as a:
#      a.write('welcome')
#      res=a.read()
#      print(res)

#append method
# with open('sam6.txt','a') as a:
#      a.write('Pentagon')
# with open('sam6.txt','a') as a:
#      a.write('space')

#printing the lenth of words in a file
# with open(r'C:\Users\dnave\OneDrive\Desktop\sam3.txt','r') as a:
#      res=a.read()
#      word=res.split()
#      print(len(word))

#removing the duplicate values in a filee
# with open(r'C:\Users\dnave\OneDrive\Desktop\sam3.txt','r') as a:
#      res=a.read()
#      word=res.split()
#      print(set(word))

#to find the count of words in the dictionary
# with open(r'C:\Users\dnave\OneDrive\Desktop\sam3.txt','r') as a:
#      res=a.read()
#      word=res.split()
#      d={}
#      for i in word:
#           d[i]=word.count(i)
#      print(d)
