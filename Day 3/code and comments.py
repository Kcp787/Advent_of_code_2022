#create a dataframe of the strings, then find the length of the string
#split the text in 2 (first half, second half) 

#create a list of the two columns

fir_list = df1["First Half"].values.tolist()
sec_list = df1["Second Half"].values.tolist()
print(fir_list)

#then want to loop through every item in the list and compare to see if the letter exists in the second list
#append the duplicate letter and item numbers to separate lists (as there may be more than 1 of the same letter in the two strings - this is calculated in Excel)

l = []
t = []


for i in range (0,300):
    a = fir_list[i]
    b = sec_list[i]
    for letter in a:
        if letter in b:
                # print(letter)
                l.append(letter)
                t.append(i)
                
