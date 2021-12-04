import numpy as np
import sys

file_name = "input.txt"
f = open(file_name, "r")
txt_inputs = f.readlines()
# num_inputs = list(map(lambda x: int(x), txt_inputs))


n = len(txt_inputs)
d = len(txt_inputs[0]) - 1
binary_data = np.zeros((n,d))

for i in range(n):
    bin_string = txt_inputs[i]
    bin_string = bin_string.strip('\n')
    num_list = np.array([list(map(lambda b: int(b), list(bin_string)))])
    binary_data[i] = num_list

gamma_rate = ""

for i in range(d):
    column = binary_data[:,i]
    column = column.astype(int)
    gamma_rate += str(np.argmax(np.bincount(column)))

gamma_rate_int = int(gamma_rate, 2)
epsilon_rate = "".join('1' if b == '0' else '0' for b in gamma_rate)
epsilon_rate_int = int(epsilon_rate, 2)


print('pt.1')
print(gamma_rate_int, epsilon_rate_int, gamma_rate_int * epsilon_rate_int)

### Part 2



oxygen_rating = ""


def determine_rating(tie_breaker, determinant):
    rating = binary_data.copy()
    i = 0 
    while len(rating) > 1:
        column = rating[:,i]
        column = column.astype(int)
        bincount = np.bincount(column)
        temp = []
        if(bincount.size == 2):
            if (bincount[0] == bincount[1]):
                most_common = tie_breaker
            else:
                # most_common = np.argmax(bincount)
                most_common = determinant(bincount)

            for bin in rating:
                if bin[i] == most_common:
                    temp.append(bin)
        else:
            temp = rating
        rating = np.array(temp)
        i += 1
    return rating

oxygen_gen_rating = determine_rating(1, np.argmax)
c02_scrubber_rating = determine_rating(0, np.argmin)

def two_d_np_bin_to_binary(rating):
    return int(''.join([str(int(b)) for b in (rating[0])]),2)

oxygen_gen_rating = (two_d_np_bin_to_binary(oxygen_gen_rating))
c02_scrubber_rating = (two_d_np_bin_to_binary(c02_scrubber_rating))


print('pt.2')
print(oxygen_gen_rating, c02_scrubber_rating, oxygen_gen_rating * c02_scrubber_rating)
