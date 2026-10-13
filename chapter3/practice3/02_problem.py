# write a python program to fill in a letter template given below with name and date.

letter = '''Dear <| Name |>,
You are selected!
<|Date|> '''

print(letter.replace("<| Name |>","Taizol").replace("<|Date|>"," 24 september 2050"))


l = input()
le =input()
print(f"You are  Name : {l}",f"you are selected Date is : {le}")