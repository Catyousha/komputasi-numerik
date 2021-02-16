nilai_asli = float(input('Masukkan nilai sebenarnya: '))
nilai_ukur = float(input('Masukkan nilai hasil pengukuran: '))
satuan = input('Masukkan satuan: ')

abs_error = abs(nilai_asli - nilai_ukur)
rel_error = (abs_error / abs(nilai_asli))

print("Diketahui: ")
print(f"x̄ = {nilai_asli} {satuan}")
print(f"x = {nilai_ukur} {satuan}")

print("Error absolut: ")
print("𝑒 = |x̄ - x|")
print(f"𝑒 = |{nilai_asli} - {nilai_ukur}|")
print(f"𝑒 = {abs_error} {satuan}")

print("Error relatif: ")
print("∈ = (𝑒 / |x̄|) * 100%")
print(f"∈ = ({abs_error} / |{nilai_asli}|) * 100%")
print(f"∈ = {rel_error}%")