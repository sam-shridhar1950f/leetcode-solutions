# From GT's Intro To Computing Class
def name_fixer(strings):
    fixed_list = []
    for i in range(len(strings)):
        if "," not in strings[i]:
            fixed_list.append(strings[i])
            
                
        if "," in strings[i]:
            count = 0
            last_name = ""
            comma_ind = 0
            while True:
                if strings[i][count] == ",":
                    comma_ind = count + 2
                    break
                
                last_name += strings[i][count]
                count += 1
            rest_of_name = strings[i][comma_ind:len(strings[i])]
            fixed_list.append(rest_of_name + " " + last_name)
                
                
                
    return fixed_list  
