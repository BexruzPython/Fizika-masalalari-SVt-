S = int(input("Masofani kiriting: "))
V = int(input("Tezlikni kiriting: "))
t = int(input("Vaqtni kiriting: "))
if S == 0:
    print(f"masofani topdik:", V * t)
if V == 0:
    print(f"tezlikni topdik:", S * t)
if t == 0:
    print(f"vaqtni topdik:", S / V)
