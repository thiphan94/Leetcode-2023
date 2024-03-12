class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        res = []
        for i in path_list:
            if i == "..":
                if res:
                    res.pop()
            elif i and i != ".":
                res.append(i)
        return "/" + "/".join(res)
