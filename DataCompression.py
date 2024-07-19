data_in = input("Enter an uncompressed string:")
data_out = ""
l = len(data_in)
count = 1
for i in range(1, l):
    if data_in[i - 1] == data_in[i]:
        count += 1
    else:
        if count > 1:
            data_out = data_out + data_in[i - 1] + str(count)
        else:
            data_out = data_out + data_in[i - 1]
        count = 1
data_out = data_out + data_in[i - 1] + str(count)
print("Compressed string:", data_out)
