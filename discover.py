# importing code from another file
# import github_tutorial
# github_tutorial.search_engine([1,5],8)
from github_tutorial import search_engine
search_engine([2,3],10)
# pre_list
pre_list = [2,4,6,77,34,56]
# search_engine(pre_list, 77)
while True:
    command = input("Type in 'q' to stop the program or a number to search my list: ")
    if command == "q":
        print("quit")
        break
    # elif command == 'skip':
    #     continue
    else:
        if command.isdigit():
            search_engine(pre_list, int(command))
        else:
            print("come on....the program needs a number since you did not type in 'q' ")