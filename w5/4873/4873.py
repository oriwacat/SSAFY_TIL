def check_match(expression):
  stack = []
  matching_dict = {
    ')': '(',
    '}': '{',
    ']': '['
  }

  for char in expression:
    if char in matching_dict.values():
      stack.append(char)
    elif char in matching_dict.keys():
      if not stack:
        return 