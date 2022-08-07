methods_list = dir(str)
for i in methods_list:
    while i != '__':
        methods_list = i
        print(methods_list)
        break