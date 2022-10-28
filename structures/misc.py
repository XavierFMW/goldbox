import trees


class RangeDict:

    def __init__(self, round_up_keys=True):
        self.dictionary = {None: None}
        self.keys = trees.BinarySearchTree()
        self.round_up = round_up_keys

    def add(self, key, value):
        self.dictionary[key] = value
        self.keys.push(key)

    def remove(self, key):
        self.dictionary.pop(key)
        self.keys.pull(key)

    def get(self, key):
        if key in self.keys:
            true_key = key
        else:
            true_key = self.keys.nearest_value(key, self.round_up)

        return self.dictionary[true_key]

    def __str__(self):
        output = "RangeDict{"
        for key, value in self.dictionary.items():
            if key is not None:
                output += f"{key}: {value}, "
        output += "}"

        return output
