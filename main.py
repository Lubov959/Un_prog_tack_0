def sum_of_two(nums: list, target: int) -> list:
    # Проверки
    if not isinstance(target, int):
        raise TypeError("Параметр target должен быть целым числом")

    if not isinstance(nums, list) or not nums:
        raise TypeError("Параметр nums должен быть не пустым листом")


    #Доп переменные
    res = []
    locked_index = set() #кортеж для уже попавших в ответ индексов

    #Перебор всех индексов и значений из nums
    for i, num in enumerate(nums):
        if i in locked_index:
            continue

        # Начинаем поиск со следующего элемента после i
        for j, value in enumerate(nums[i + 1:], start=i + 1):
            if j in locked_index:
                continue

            if (num + value) == target:
                res.append([i, j])
                #Блокируем эти индексы
                locked_index.add(i)
                locked_index.add(j)
                break  # Нашли пару для числа i, переходим к следующему i
    return res


def main():
    my_nums = [1,2,3,9,10]
    targ = 10
    print(f'Для массива {my_nums} сумма {targ} достигается суммой элементов с индексами:')
    print(sum_of_two(my_nums, targ))

if __name__ == '__main__':
    main()


