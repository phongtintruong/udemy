dick = ['cuo', 'HuyBinh', 'KhanhHau', 'Nghia10', 'Lam']
dick.append('MinhThot')
bonus_dick = ['Thang']
dick += bonus_dick
dick_and_length = [['cuo', 2], ['HuyBinh', 5]]
dick += dick_and_length
print(dick.append(19))
print(dick)
empty_list = []
print(empty_list)
print(dick[8])
bonus_dick = [input(), input(), input()]
if bonus_dick[-1] == 'Trung':
    print("last element is wrong")