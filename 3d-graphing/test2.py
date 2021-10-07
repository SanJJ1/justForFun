import sys
x = 0

def rev(s):
    rev.c += 1
    l = len(s)//2
    if len(s) == 2:
        return s[1] + s[0]
    if len(s) == 1:
        return s
    return rev(s[l:]) + rev(s[:l])
# rev.c = 0
# print(rev(input()))
# print(rev.c)
x = "fpkyoxvdqejuoytwbdzrwsltxelptcmlzfavlwpawcyipsulafdkxqaizizlekqdummggirxteorkiifoakwzssqmmgntddrmmuhbgselibtthwcfklxlktvmfoceqtfbbhoyatmjfqlurajtyrdvmdiifwhaojdbekxzagnprxzwiazmpsxddokbclctliamxknhhdmdpfaiwkdykycxhacbwurfqtfsygrecxuacibysdvrgnqyvvzntimocitwrlobrttzdnkocdttzqoiaqxjwuxhgrpwselwmdkmoanexkweqxjbcijtsfaxpmircpkxanoaacvqyvhtyevqialrsihxubinqueebvpmaelmvdgbehowjxfridlyfutajezyhhiurwwsxoypgyahrsgrcyyibtavouzeaypivftyxrrhlcnfussecybqkbeemlsezkfdjnqihstbsgdntsacxwhqryjymowzycjfwuuvdjawtkfdxlryeksdqtlfhvcomkbyyzfnnndtqkmkaozolzjywmuegjmucykdvwdpzncdmbbcvjqcjfmrsgxzpoitzibvctecdajmtefvrqmcvrhbadeozobvavooisjdfymikeburvpxhhfxlptddhybacsmzwwzgslffabuyauvwvwukkcpswcponyssrqrvbpqyomwzuwnesjcuobvduolootmpobccqldxwgixcxcmeduvslzlkoethkslarqkxpzozjxtkaiqiwdbysrsnpppajyzfsjojvqfbjgvznwvypfobaozbtfwtvrsrlfjdjlywyrvmgmmuewwklblcwqavbfgoseidzqziuqqlpgtqlkfjolxzbkasfvcynwblgecadtxcldeghwhrgdtxvdwqzqylxxdhoanpwxqfzgzdcsmkjfcvdlrlyxehejwodyvbxpjdqgcgusquknoyjvbtkkwsyqhubhqxndclhnnvkvzfzvgkdjlaevozftgxpbrcplsfjnbbwqcjo"
for i in range(3, 1024):
    rev.c = 0
    rev(x[:i])
    print(i, rev.c)
