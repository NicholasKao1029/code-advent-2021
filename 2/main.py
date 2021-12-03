file_name = "input.txt"
f = open(file_name, "r")
txt_inputs = f.readlines()
# num_inputs = list(map(lambda x: int(x), txt_inputs))


depth_movement = set(['down', 'up'])
horiz_movement = 'forward'



def calculate_depth_horiz(input):
    depth = 0
    horiz = 0
    for x in input:
        text_split = x.split(' ')
        direction = text_split[0]
        amount = int(text_split[1])
        
        if direction in depth_movement:
            if direction == 'down':
                depth += amount
            else:
                depth -= amount
        else:
            assert(direction == horiz_movement)
            horiz += amount
    return depth, horiz

depth, horiz = calculate_depth_horiz(txt_inputs)

print('pt.1')
print(depth, horiz, depth * horiz)




def calculate_depth_horiz_aim(input):
    depth = 0
    horiz = 0
    aim = 0
    for x in input:
        text_split = x.split(' ')
        direction = text_split[0]
        X = int(text_split[1])
        
        if direction in depth_movement:
            if direction == 'down':
                aim += X
            else:
                # 'up'
                aim -= X
        else:
            assert(direction == horiz_movement)
            horiz += X
            depth += (aim * X)
    return depth, horiz, aim


depth, horiz, aim= calculate_depth_horiz_aim(txt_inputs)

print()
print('pt.2')
print(depth, horiz, depth * horiz)
