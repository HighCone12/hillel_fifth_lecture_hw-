lst = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
for i in lst:
    while lst.count(i) > 1:
        lst.remove(i)
        lst.remove('eg')
print(lst)