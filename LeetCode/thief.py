def best_path_cost(l: list) -> list:
    print("call")
    if len(l) == 1:
        return [l[0], l]
    elif len(l) == 2:
        return [max(l), [max(l)]]
    else:
        max_money1, house_list1 = best_path_cost(l[2:])
        max_money2, house_list2 = best_path_cost(l[3:])
        return max([max_money1+l[0], [l[0]]+house_list1], [max_money2+l[1], [[l[1]]+house_list2]])


houses = [8, 7, 6, 5, 1, 1]
print(best_path_cost(houses))

# iterative approach
