array = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]


def hashFunction(data):
    return sum(ord(char) for char in data) % len(array)

def add(data):
    index = hashFunction(data)
    bucket = array[index]
    if data not in bucket:
        bucket.append(data)

def contains(data):
    index = hashFunction(data)
    bucket = array[index]
    return data in bucket

add('Stuart')

print(array)
print("Contains Stuart:",contains('Stuart'))