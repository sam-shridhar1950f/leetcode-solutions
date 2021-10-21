# From GT's Intro To Computing Class
def name_refixer(strings):
    fixed_list = []
    for i in range(len(strings)):
        if "," not in strings[i]:
            str1 = ""
            first_ind = 0
            for j in range(len(strings[i])):
                if " " not in strings[i][j:len(strings[i])]:
                    if first_ind == 0:
                        first_ind = j
                    str1 += strings[i][j] # appending last name
            str1 += ", "
            str1 += strings[i][0:first_ind]
            fixed_list.append(str1.strip())
            
                
        if "," in strings[i]:
            fixed_list.append(strings[i])
    return fixed_list    
