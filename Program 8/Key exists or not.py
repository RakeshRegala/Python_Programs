my_dict = {'name': 'ral', 'b': 20, 'c': 30, 'd': 40}
#print(my_dict.values())
key=input("Enter a key: ")
if key in my_dict:
    print(f"The key {key} exists in dictionary")
else:
        print(f"The key {key} does not exist in dictionary")
