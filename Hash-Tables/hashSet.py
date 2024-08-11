class HashSet:
    def __init__(self,size=100):
        self.size = size
        self.bucket = [[] for _ in range(size)]

    def hashFunction(self,data):
        return sum(ord(char) for char in data) % self.size

    def add(self,data):
        index = self.hashFunction(data)
        bucket = self.bucket[index]
        if data not in bucket:
            bucket.append(data)

    def contains(self,data):
        index = self.hashFunction(data)
        bucket = self.bucket[index]
        return data in bucket

    def remove(self,data):
        index = self.hashFunction(data)
        bucket = self.bucket[index]
        if data in bucket:
            bucket.remove(data)

    def printSet(self):
        print("Hash set contents:")
        for index,bucket in enumerate(self.bucket):
            print(f"Bucket {index}:{bucket}")



hash_set = HashSet(size=10)

hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")

hash_set.printSet()

print("\n'Peter' is in the set:",hash_set.contains('Peter'))
print("Removing 'Peter'")
hash_set.remove('Peter')
print("'Peter' is in the set:",hash_set.contains('Peter'))
print("'Adele' has hash code:",hash_set.hashFunction('Adele'))