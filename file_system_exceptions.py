# read from file
filename = 'pi.txt'

# # with info outside the block
# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip() * 3)

# with infor within the block
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip() * 3)
