# q1)-
if "abc" in "123abc456":
    print("found")

#.........................................
#q2)-
# Mutable: Can change (e.g., list).

# Immutable: Cannot change (e.g., str).

# Strings are immutable for performance and security.

#.........................................
#q3)-

table = str.maketrans("abc", "123")
print("abc".translate(table))

#.........................................
#q4)-
parts = ["a", "b", "c"]
result = ''.join(parts)
print(result)

#.........................................
#q5)-
# str(): User-friendly.
# repr(): Developer-friendly (shows escape characters).

#..........................................
#q6)-
name = "John"
print("Hello %s" % name)

#..........................................
#q7)-
# format(): Older.

# f-string: Newer, faster, cleaner.

#..........................................
#q8)-
s = "madam"
print(s == s[::-1])  

#..........................................
#q9)-
s = "hello, world!"
res = ""
for ch in s:
    if ch not in ",.!?":
        res += ch
print(res)  

#..........................................
#q10)-
s = "hello"
d = {}
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
print(d)

#..........................................
#q11)-

#..........................................
#q12)-
s = "7"
print(s.zfill(5))

#..........................................
#q13)-
# find(): First occurrence.

# rfind(): Last occurrence.

#..........................................
#q14)-
# execute raw input directly, users can inject malicious code.
# Always validate and sanitize input.

#..........................................
#q15)-lower(): Basic lowercase.

# casefold(): Aggressive lowercase (for international text).
s = "Groß"
print(s.lower())    
print(s.casefold()) 

