file_name = "input.txt"
f = open(file_name, "r")

txt_inputs = f.readlines()

ans = 0
num_inputs = list(map(lambda x: int(x), txt_inputs))

prev = num_inputs[0]

for num in num_inputs[1:]:
    if num > prev: 
        ans += 1
    prev = num

print(ans)
print(len(txt_inputs))
