def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size


    # Use the modulo operator to check whether there's any remainder
    partial_block = filesize % block_size




    # Depending on whether there's a remainder or not, return the right number.
    if partial_block > 0:

        if filesize>block_size:
            return block_size+(block_size*full_blocks)
        else:
            return block_size
    else:
        #print("i am not executed")
        return block_size * full_blocks


print(calculate_storage(110))  # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192


def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))

print(((10 >= 5*2) and (10 <= 5*2)))

print("big" > "small")