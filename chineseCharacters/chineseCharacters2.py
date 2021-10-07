import sys

print(bytes('浩潰瑲爠൥瀊楲瑮猨浵洨灡椨瑮爬⹥楦摮污⡬❲摜✫椬灮瑵⤨⤩⤩','u16'))
print(b"\xff\xfeimport re\r\nprint(sum(map(int,re.findall(r'\\d+',input()))))".decode("u16"))

print(b"\xff\xfeimport re\r".decode("u16"))

print(sys.getsizeof(b"\xff\xfeimport re\r\nprint(sum(map(int,re.findall(r'\\d+',input()))))"))