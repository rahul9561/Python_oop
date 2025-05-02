# # regex
# import re
# Basic Syntax:
# Literal characters: Match exactly as they are.

# Example: r"abc" matches the string "abc".

# . (Dot): Matches any single character except newline (\n).

# Example: r"a.b" matches "acb", "axb", but not "ab".

# ^ (Caret): Matches the beginning of the string.

# Example: r"^abc" matches "abc" only if it's at the start.

# $ (Dollar): Matches the end of the string.

# Example: r"abc$" matches "abc" only if it's at the end.

# * (Asterisk): Matches 0 or more repetitions of the preceding character or group.

# Example: r"ab*c" matches "ac", "abc", "abbc", etc.

# + (Plus): Matches 1 or more repetitions of the preceding character or group.

# Example: r"ab+c" matches "abc", "abbc", but not "ac".

# ? (Question mark): Matches 0 or 1 repetition of the preceding character or group.

# Example: r"ab?c" matches "abc" and "ac".

# {n,m}: Matches between n and m repetitions of the preceding character or group.

# Example: r"ab{2,4}c" matches "abbc", "abbc", "abbbc", but not "abc".

# [] (Square brackets): Matches any one character from a set.

# Example: r"[aeiou]" matches any vowel.

# | (Pipe): Logical OR. Matches either the expression before or the expression after the pipe.

# Example: r"abc|def" matches "abc" or "def".

# () (Parentheses): Groups expressions together.

# Example: r"(abc)+" matches one or more repetitions of "abc".

