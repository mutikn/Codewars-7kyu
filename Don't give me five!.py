def dont_give_me_five(start, end):
    list_of_numbers = [i for i in range(start, end+1)]
    list_of_new_numbers = list(filter(lambda x : "5" not in str(x) , list_of_numbers))
    return len(list_of_new_numbers)
print(dont_give_me_five(4, 17))
# https://www.codewars.com/kata/5813d19765d81c592200001a/train/python

