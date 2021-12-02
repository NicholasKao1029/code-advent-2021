file_name = "input.txt"
f = open(file_name, "r")

txt_inputs = f.readlines()

num_inputs = list(map(lambda x: int(x), txt_inputs))


def sliding_3(lst):
    length = len(lst)
    ans = []
    for i in range(length-2):
        sum = 0
        for j in range(3):
            sum += lst[i+j]
        ans.append(sum)
    return ans


sliding_3_window = sliding_3(num_inputs)

def count_increasing(lst):
    ans = 0
    prev = lst[0]
    for num in lst[1:]:
        if num > prev: 
            ans += 1
        prev = num
    return ans

print('pt.1')
print(count_increasing(num_inputs))
print()
print('pt.2')
print(count_increasing(sliding_3_window))
