                        # ONE OF CYPHER FUNCTION #
#--------------------------------------------------------------------------------------------------#
# CREATING A ENCRYPT FUNCTION :-

def encryption(word,key):
    words_list = list(word)
    key_list = list(key)
    encrypted = ''
    k = 0
    l = 0
    while k < len(words_list):
        j = 0
        i = 0
        while True:
            if dict[j][0] == words_list[k]:
                new_j = j
                while l < len(words_list):
                    while True:
                        if dict[0][i] == key_list[l]:
                            new_i = i
                            encrypted = encrypted + dict[new_j][new_i]
                            l = l + 1
                            break
                        else:
                            i = i + 1
                    break        
                k = k + 1                
                break            
            else:
                j = j + 1

    return encrypted

#-------------------------------------------------------------------------------------------------#
#  CREATING A DECRYPT FUNCTION :-

def decryption(encrypted_words,key,word):
    encrypted_word_list = list(encrypted_word)
    word_list = list(word)
    d_key = ''
    j = 0
    k = 0
    while j < 26:
        if (len(d_key) == len(word_list)):
            break
        else:

            if dict[j][0] == encrypted_word_list[k]:
                i = 0
                while i < 26:
                    if dict[j][i] == word_list[k]:
                        d_key = d_key + dict[0][i]
                        if (len(d_key) == len(word_list)):
                            break
                        else:
                            k = k + 1
                            break 
                        
                    else:
                        i = i + 1
                j = 0        
            else:   
                j = j + 1
          
        
       
    decrypted_word = encryption(d_key,encrypted_word)
    return decrypted_word
    

#-------------------------------------------------------------------------------------------------#
# CREATING MATRIX LETTERS :-
dict = []
i = 0

j = 65
while i < 26:
    dict.append([])
    k = 0
    j = 65 + i
    while k < 26:
        
        if j == 91:
            r = 0
           
            while r < i:
                p = 65 + r
                dict[i].append(chr(p))
                r+=1

        elif j < 91:
            dict[i].append(chr(j))     
        j+=1
        k+=1
    i+=1



for i in range(len(dict)):
    print("\t")
    for j in range(len(dict[i])):
        print(dict[i][j], end=" ")

print("\n")

#-----------------------------------------------------------------------------------------------#
# INPUTS FROM USER:-

word = input("Input Your word: ")
key = input("Enter A key : ")
new_key = list(key)

length = len(key)
newkey = ''

original_word_list = list(word)
i = 0


while i < len(original_word_list):
    if len(newkey) < len(original_word_list):
        newkey = newkey + new_key[i]
        i = i + 1
        if i == 3:
            i = 0
    else:
        break 
print("Your new key is : " + newkey)
encrypted_word = encryption(word,newkey)
decrypted_word = decryption(encrypted_word,newkey,word)
print("Your Encrypted word: " + encrypted_word)
print("Your Decrypted word: " + decrypted_word)
  








  

