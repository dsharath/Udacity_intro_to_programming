def find_last(search_string,target_string):
     i=-1
     while search_string.find(target_string,i+1) >=0:
         i = search_string.find(target_string,i+1)
     return i


print find_last('aaaaa', 'a')+1