class RemoveDuplicate:
    def __init__(self, lst):
        self.lst = lst
        
    def remove_duplicate(self):
        seen = set()
        return [x for x in self.lst if not (x in seen or seen.add(x))]
    

r = RemoveDuplicate([1, 2, 2, 4, 3, 7, 7, 7, 6, 4])
print(r.remove_duplicate())