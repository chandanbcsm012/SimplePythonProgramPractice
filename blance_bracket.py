# def blance_bracket_count(s):
#     open_b = 0
#     close_b = 0
#     for i in s:
#         if i == '(':
#             open_b +=1
#         else:
#             close_b +=1
#     return close_b - open_b


# s = ')())()())'
# count = blance_bracket_count(s)
# print(count)

# def is_balanced_bracket(s):
#     map = {'(': ')', '{': '}', '[': ']'}
#     stack = []
#     for i in s:
#         if i in map:
#             stack.append(i)
#         else:
#             if stack:
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0

# print(is_balanced_bracket("()()"))        # True
# print(is_balanced_bracket("(())"))        # True
# print(is_balanced_bracket("(()))"))       # False
# print(is_balanced_bracket(")("))          # False