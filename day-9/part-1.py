with open("input", "r") as f:
    disk_map = f.readline().rstrip()
print(disk_map)

disk_size = sum(map(int, disk_map))
print(disk_size)

# disk_blocks = ["."] * disk_size
# print(disk_blocks)

id = 0
head_position = 0
disk_blocks = []
disk_map = iter(disk_map)

for block_length in disk_map:
    disk_blocks.extend([str(id)] * int(block_length))
    id += 1
    if free_space := next(disk_map, False):
        disk_blocks.extend(["."] * int(free_space))

new_disk_blocks = []

for block in disk_blocks:
    if block == ".":
        last_block = disk_blocks.pop()
        while last_block == ".":
            last_block = disk_blocks.pop()
        new_disk_blocks.append(last_block)
    else:
        new_disk_blocks.append(block)

checksum = 0

for idx, block in enumerate(new_disk_blocks):
    checksum += idx * int(block)

# print("".join(new_disk_blocks))
print(checksum)
