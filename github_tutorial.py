# 1 [create a program that searches for an item in a list of numbers. 
#     The item to be searched for should be gotten from the user as an input.]

# chals_list = [2,5,6,8,20]
# Get input from user and convert to integer
# data = int(input("Enter a number: "))
# Search for the number in the list
# for data in chals_list:
#     if data == number:
#         print("found")
#         break
# else:
#     print("not found")

# for number in chals_list:
#     if data == number:
#         print("found")
#         break
#     else:
#         print("not found")
#         break

# if data in chals_list:
#     print("found")
# else:
#     print("not found")

# wrap the previous search code in a pure function
def search_engine(search_list,item_to_search):
    if item_to_search in search_list:
        print("found")
    else:
        print("not found")

dataset = [2,4,6,5,8,10,34]
userdata = int(input("Enter a number: "))
search_engine(dataset, userdata)






# is_found = False

# # for data in chals_list:
# #     print(f"data found")
# #     break

# for data in chals_list:
#     if data == number:
#         is_found = True 
#         print("found")
#         break

# if is_found == True:
#     print("found")

# else:
#     print("not found")

