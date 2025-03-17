class FileSystem:

    def __init__(self):
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        if not path or path == "/" or path in self.paths:
            return False
        arr = path.split("/")
        print(arr)
        root = self.paths
        for i in range(1,len(arr)):
            p = arr[i]
            if p not in root:
                if i == len(arr)-1:
                    root[p] = {}
                else:
                    return False
            root = root[p]
            

        if "end" in root:
            return False
        root["end"] = value
        return True

    def get(self, path: str) -> int:
        arr = path.split("/")
        root = self.paths
        for i in range(1,len(arr)):
            p = arr[i]
            if p not in root:
                return -1
            root = root[p]

        return root.get("end",-1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)