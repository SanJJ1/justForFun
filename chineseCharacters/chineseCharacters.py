# Problem statement:
# take a string input, and output the sum of all the numbers in the string.
# Example:
# input:    "asdfj123jklj42lkj17oiowe9"
# output:    191, becase 123 + 42 + 17 + 9 = 191

# exec(bytes('浩潰瑲爠൥瀊楲瑮猨浵洨灡椨瑮爬⹥楦摮污⡬❲摜✫椬灮瑵⤨⤩⤩','u16')[2:])

# print(bytes('浩潰瑲爠൥瀊楲瑮猨浵洨灡椨瑮爬⹥楦摮污⡬❲摜✫椬灮瑵⤨⤩⤩','u16'))

# print(bytes('浩潰瑲爠൥瀊楲瑮猨浵洨灡椨瑮爬⹥楦摮污⡬❲摜✫椬灮瑵⤨⤩⤩','u16')[2:])

# print("import re\r\nprint(sum(map(int,re.findall(r'\\d+',input()))))")

import re

x = map(int, re.findall(r'\d+', input()))
print(sum(x))
