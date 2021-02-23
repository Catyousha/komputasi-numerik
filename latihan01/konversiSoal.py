x               = input("Masukkan angka yang ingin diubah ke desimal: ")
basis           = int(input("Masukkan basis: "))
hexa_symbol     = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
subscript       = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
hasil           = hexa_symbol[x[0]] if (x[0] in hexa_symbol.keys()) else int(x[0])

# print(hexa_symbol.keys())
suku = len(x)-1
print(f'b{str(suku).translate(subscript)} = a{str(suku).translate(subscript)}')
print(f'b{str(suku).translate(subscript)} = {hasil}')
for i in x[1:]:
    i = hexa_symbol[i] if (i in hexa_symbol.keys()) else int(i)

    suku -= 1
    simbol_suku         = str(suku).translate(subscript)
    simbol_suku_sebelum = str(suku+1).translate(subscript)
    
    print(f'b{simbol_suku} = a{simbol_suku} + b{simbol_suku_sebelum} * β')
    print(f"b{simbol_suku} = {i} + {hasil} * {basis}")

    hasil = i + (hasil * basis)
    print(f"b{simbol_suku} = {hasil}")

# print(hasil);
