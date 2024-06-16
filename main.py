from excel import Excel

print(f'\n\nLayerZero Sybil Checker\n')

with open('L0_sybils.txt') as f: L0_sybils = f.read().splitlines()
with open('addresses.txt') as f: addresses = f.read().splitlines()
excel = Excel(total_len=len(addresses), name="sybil")

total_sybil = 0
for index, address in enumerate(addresses):
    sybil = address.lower() in L0_sybils
    if sybil:
        print(f'[-] [{index+1}/{len(addresses)}] {address}: SYBIL !!!')
        total_sybil += 1
        status = "Sybil"
    else:
        print(f'[+] [{index+1}/{len(addresses)}] {address}: not sybil')
        status = "Not sybil"

    excel.edit_table(data=[address, status])
excel.edit_table(data=[f"Total sybils: {total_sybil}/{len(addresses)}"])

input(f'\nTotal sybils: {total_sybil}/{len(addresses)}\nResults saved in results/{excel.file_name}\n\n> Exit')
