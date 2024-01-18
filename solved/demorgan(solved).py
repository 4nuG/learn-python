'''
Verifies both De Morgan theorems:
not(A and B) == (not A) or (not B)
not(A or B) == ((not A) and (not B))
They're not the same.
'''

# This is not (A and B)
A = True
B = True
print("not(", A, "and", B, ")", "==",
      "(not", A, ") or (not", B, "):",
      not(A and B) == (not A) or (not B))

A = True
B = False
print("not(", A, "and", B, ")", "==",
      "(not", A, ") or (not", B, "):",
      not(A and B) == (not A) or (not B))

A = False
B = True
print("not(", A, "and", B, ")", "==",
      "(not", A, ") or (not", B, "):",
      not(A and B) == (not A) or (not B))

A = False
B = False
print("not(", A, "and", B, ")", "==",
      "(not", A, ") or (not", B, "):",
      not(A and B) == (not A) or (not B))

# This is not (A or B) == ((not A) and (not B))
A = True
B = True
print("not(", A, "and", B, ")", "==",
      "(not", A, ") or (not", B, "):",
      not(A or B) == ((not A) and (not B)))

A = True
B = False
print("not(", A, "and", B, ")", "==",
      "(not", A, ") or (not", B, "):",
      not(A or B) == ((not A) and (not B)))

A = False
B = True
print("not(", A, "and", B, ")", "==",
      "(not", A, ") or (not", B, "):",
      not(A or B) == ((not A) and (not B)))

A = False
B = False
print("not(", A, "and", B, ")", "==",
      "(not", A, ") or (not", B, "):",
      not(A or B) == ((not A) and (not B)))
