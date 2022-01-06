class Solution:
    """
        hory笨笨的做法
    """
    def simplifyPath_hory(self, path: str) -> str:
        stack = []
        dot_count = 0
        new_path = path + '/'
        for s in new_path:
            if s == '.':
                dot_count += 1

            if s == '/' and 1 <= dot_count <= 2 and stack[-1] == '.':
                drop_t = 0
                drop_thing = ''
                while stack[-1] != '/' or (stack[-1] == '/' and drop_thing == '.'
                        and drop_t < 1 and dot_count == 2 and len(stack) > 1):
                    if dot_count == 2 and not drop_thing and stack[-3] != '/' :
                        stack.append(s)
                        break
                    if stack[-2] != '/' and dot_count == 1:
                        stack.append(s)
                        break
                    drop_thing = stack.pop()
                    if drop_thing == '/':
                        drop_t += 1
                dot_count = 0
                continue

            if len(stack) > 0 and s == '/' and stack[-1] == '/':
                continue

            stack.append(s)
            if s == '/':
                dot_count = 0
            
        
        if len(stack) == 1:
            return '/'
        elif stack[-1] == '/':
            return ''.join(stack[:len(stack)-1])

    """
        答案做法
    """
    def simplifyPath(self, path: str) -> str:
        names = path.split("/")
        stack = list()
        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)
        return "/" + "/".join(stack)


sol = Solution()
path = "/./"
new_path = sol.simplifyPath(path)
print(new_path)




            