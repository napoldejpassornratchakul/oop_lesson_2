def gen_comb_list(list_set):
    if len(list_set) == 1:
        main_list = []
        for i in list_set[0]:
            temp = []
            temp.append(i)
            main_list.append(temp)
        return main_list
    else:
        main_list = []
        for i in list_set[0]:
            remain_list = gen_comb_list(list_set[1:])
            for j in remain_list:
                main_list.append([i] + j)

        return main_list





print(gen_comb_list([[1, 2, 3]]))
print(gen_comb_list([[1, 2, 3], [4, 5]]))

