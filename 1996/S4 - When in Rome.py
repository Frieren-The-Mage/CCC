roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
        "D": 500, "M": 1000}

rev = {1: "I", 5: 'V', 10: 'X', 50: 'L', 100: 'C',
        500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC',
       400: 'CD', 900: 'CM'}

def rom_to_num(n):
    ans = 0

    n = n.replace("IV", "IIII")
    n = n.replace("IX", "VIIII")
    n = n.replace("XL", "XXXX")
    n = n.replace("XC", "LXXXX")
    n = n.replace("CD", "CCCC")
    n = n.replace("CM", "DCCCC")

    for letter in n:
        ans += roman[letter]
    return ans

def num_to_rom(n):
    ans = ''

    while n:
        for i in sorted(rev.keys(), reverse=True):
            if i <= n:
                n -= i
                ans += rev[i]
                break
    return ans

t = int(input())
for i in range(t):
    s = input()

    s = s.replace('+', ' ').replace('=', ' ').split()

    n = rom_to_num(s[0]) + rom_to_num(s[1])

    if n > 1000:
        print(f'{s[0]}+{s[1]}=CONCORDIA CUM VERITATE')
        continue

    else:
        # print(n)
        rom = num_to_rom(n)
        print(s[0] + '+' + s[1] + '=' + rom)
