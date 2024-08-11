class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.bucket = [[] for _ in range(size)]

    def hashFunction(self, key):
        numericSum = sum(int(char) for char in key if char.isdigit())
        return numericSum % self.size

    def put(self, key, data):
        index = self.hashFunction(key)
        bucket = self.bucket[index]
        for i, (k, d) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, data)
                return
        bucket.append((key, data))

    def get(self, key):
        index = self.hashFunction(key)
        bucket = self.bucket[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self.hashFunction(key)
        bucket = self.bucket[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

    def print_map(self):
        print("Hash Map Contents:")
        for index, bucket in enumerate(self.bucket):
            print(f"Bucket {index}: {bucket}")

hash_map = HashMap(size=10)

hash_map.put("123-4567", "Charlotte")
hash_map.put("123-4568", "Thomas")
hash_map.put("123-4569", "Jens")
hash_map.put("123-4570", "Peter")
hash_map.put("123-4571", "Lisa")
hash_map.put("123-4672", "Adele")
hash_map.put("123-4573", "Michaela")
hash_map.put("123-6574", "Bob")

hash_map.print_map()
