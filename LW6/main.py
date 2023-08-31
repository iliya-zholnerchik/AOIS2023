class Node:
    def __init__(self, key_name, information, value, hash_address):
        self.information = information
        self.key_name = key_name
        self.value = value
        self.next = None
        self.hash_address = hash_address


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def get_numeric_value(self, key_name):
        a = ord('а')
        alphabet = ''.join([chr(i) for i in range(a, a + 32)])
        alphabet = list(alphabet)
        return alphabet.index(key_name[0].lower()) * 33 + alphabet.index(key_name[1].lower())

    def get_hash_address(self, value):
        result = value % self.capacity
        return result

    def show(self):
        for i in range(len(self.table)):
            if self.table[i] is not None:
                if self.table[i].next is None:
                    print(f'Hash-address: {self.table[i].hash_address} key_name: {self.table[i].key_name}')
                elif self.table[i].next is not None:
                    print(f'Hash-address: {self.table[i].hash_address} key_name: ', end='')
                    current = self.table[i]
                    while True:
                        if current.next is None:
                            print(f'{current.key_name}')
                            break
                        else:
                            print(f'{current.key_name} ', end='')
                            current = current.next

    def insert(self, key_name, information):
        value = self.get_numeric_value(key_name)
        hash_address = self.get_hash_address(value)
        index = self.search_hash(hash_address)
        if self.table[index] is None:
            self.table[index] = Node(key_name, information, value, hash_address)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key_name == key_name:
                    current.value = information
                    return
                current = current.next
            new_node = Node(key_name, information, value, hash_address)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key_name):
        for i in range(len(self.table)):
            if self.table[i] is not None:
                if self.table[i].key_name == key_name:
                    print(
                        f' key_name: {self.table[i].key_name}\n Hash-address: {self.table[i].hash_address}\n number: {self.table[i].value}\n collisium: {1 if self.table[i].next is not None else 0}\n info: {self.table[i].information}')
                    return
                elif self.table[i].next is not None:
                    current = self.table[i]
                    while True:
                        if current.key_name == key_name:
                            print(
                                f' key_name: {current.key_name}\n Hash-address: {current.hash_address}\n number: {current.value}\n collisium: 1\n info: {current.information}')
                            return
                        elif current.next is None:
                            break
                        else:
                            current = current.next

    def search_hash(self, hash_address):
        index = 0
        for i in range(len(self.table)):
            current = self.table[i]
            if current is None:
                index = i
            elif current.hash_address == hash_address:
                return i
        return index

    def remove(self, key_name):
        for i in range(len(self.table)):
            if self.table[i] is not None:
                if self.table[i].key_name == key_name:
                    if self.table[i].next is not None:
                        self.table[i] = self.table[i].next
                        return
                    else:
                        self.table[i] = None
                        return
                else:
                    if self.table[i].next is not None:
                        previous = None
                        current = self.table[i]
                        while current:
                            if current.key_name == key_name:
                                previous.next = current.next
                                self.size -= 1
                                return
                            elif current.next is None:
                                break
                            else:
                                previous = current
                                current = current.next

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False


if __name__ == '__main__':
    numbers = ''
    ht = HashTable(16)

    ht.insert("яблоко", 3)
    ht.insert("банан", 2)
    ht.insert("вишня", 5)
    ht.insert("вино", 6)
    ht.insert("абрикос", 4)

    ht.remove("абрикос")
    ht.show()
    while True:
        print("\nOptions:\n 1) Adding\n 2) Searching\n 3) Deleting\n 4) Table view\n 5) Exit")
        key = input("Choose option:")
        if key == "1":
            name = input("Enter key name: ")
            info = input("Enter info: ")
            if name[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print('Only words can be used')
            else:
                ht.insert(name, info)
        elif key == "2":
            info = input("Enter key_name for search: ")
            ht.search(info)
        elif key == "3":
            info = input("Enter key_name to delete: ")
            ht.remove(info)
        elif key == "4":
            ht.show()
        elif key == "5":
            break
