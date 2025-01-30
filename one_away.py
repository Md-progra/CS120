def one_away(str1,str2):
        count = 0 
        for i in range(len(str1)) and range(len(str2)):
                        if str1[i] != str2[i]:
                                count += 1 
                                
                        if count == 1 and len(str1) == len(str2):
                                return True
        return False
                        
                
                        

print(one_away("water","water"))