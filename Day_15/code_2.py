strings = open("input.txt").read().split(",")


def getHash(seq):
    val = 0
    for ch in seq:
        val += ord(ch)
        val *= 17
        val %= 256
    return val


part1 = 0
for seq in strings:
    part1 += getHash(seq)

boxes = [dict() for i in range(256)]


def put(label, focal_length):
    boxes[getHash(label)][label] = int(focal_length)


def remove(label):
    for box in boxes:
        box.pop(label, None)


for seq in strings:
    label = "".join([ch for ch in seq if ch.isalpha()])
    operation = "".join([ch for ch in seq if ch == "-" or ch == "="])
    focal_length = "".join([ch for ch in seq if ch.isdigit()])

    if operation == "-":
        remove(label)
    if operation == "=":
        put(label, focal_length)

part2 = 0
for i, box in enumerate(boxes):
    j = 1
    for label, focal_length in box.items():
        part2 += (i + 1) * (j) * focal_length
        j += 1

print(part2)
