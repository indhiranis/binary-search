def binary_search(list,key):
  low=0
  high=len(list)-1
  Found=False
  while low<=high and not Found:
    mid=(low+high)//2
    if key==list[mid]:
      Found=True
    elif key<list[mid]:
      high=mid-1
    else:
      low=mid+1
  if Found==True:
    print('key is found')
  else:
    print('key is not found')
  
list=[23,1,4,2,3]
list.sort()
print(list)
key=int(input('enter the key:'))
binary_search(list,key)
