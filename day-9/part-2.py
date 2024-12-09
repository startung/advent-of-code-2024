from dataclasses import dataclass, field
from tqdm import tqdm


@dataclass(order=True)
class file:
    id: str = field(compare=False)
    start_block: int = field(compare=True)
    length: int = field(compare=False)


with open("input", "r") as f:
    disk_map = f.readline().rstrip()
# print(disk_map)

disk_size = sum(map(int, disk_map))
print(disk_size)

head_position = 0
disk_map = iter(disk_map)
files = []

for file_id, block_length in enumerate(disk_map):
    block_length = int(block_length)
    files.append(file(str(file_id), head_position, block_length))
    head_position += block_length
    if free_space := next(disk_map, False):
        head_position += int(free_space)

# print(files)


def files_to_block(files: list[file]) -> None:
    new_disk_blocks = []
    for f in sorted(files):
        if len(new_disk_blocks) < f.start_block:
            new_disk_blocks.extend("." * (f.start_block - len(new_disk_blocks)))
        new_disk_blocks.extend([f.id] * f.length)
    return "".join(new_disk_blocks)


def find_gap(files: list[file], length: int) -> int:
    head_position = 0
    for f in sorted(files):
        if f.start_block - head_position >= length:
            return head_position
        head_position = f.start_block + f.length
    return -1  # could not find a gap


def checksum_old(blocks: str) -> int:
    sum = 0
    for idx, block in enumerate(blocks):
        if block != ".":
            sum += idx * int(block)
    return sum


def checksum(files: list[file]) -> int:
    sum = 0
    for f in files:
        for idx in range(f.length):
            sum += int(f.id) * (idx + f.start_block)
    return sum


for f in tqdm(files[::-1]):
    gap = find_gap(files, f.length)
    if gap != -1 and gap < f.start_block:
        f.start_block = gap
    # print(f"{f.id} could fit at position {find_gap(files, f.length)}")
print(sorted(files)[:10])
blocks = files_to_block(files)
# print(blocks)
print(checksum(files))
