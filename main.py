from os import listdir
from excel import Excel

print(f'\n\nLayerZero Sybil Checker\n')


L0_sybils_raw = []
L0_sybils = {}
for file_name in listdir('sybil_list'):
    with open(f'sybil_list/{file_name}') as f: L0_sybils_raw += f.read().splitlines()
L0_sybils = {sybil.split(',')[-1].lower(): sybil.split(',')[0] for sybil in L0_sybils_raw if sybil}

with open('addresses.txt') as f: addresses = f.read().splitlines()
excel = Excel(total_len=len(addresses), name="sybil")

total_sybil = 0
for index, address in enumerate(addresses):
    sybil = address.lower() in L0_sybils
    if sybil:
        print(f'[-] [{index+1}/{len(addresses)}] {address}: SYBIL !!!')
        total_sybil += 1
        status = "Sybil"
        data = [address, "Sybil", L0_sybils[address.lower()]]
    else:
        print(f'[+] [{index+1}/{len(addresses)}] {address}: not sybil')
        data = [address, "Not sybil"]

    excel.edit_table(data=data)
excel.edit_table(data=[f"Total sybils: {total_sybil}/{len(addresses)}"])

input(f'\nTotal sybils: {total_sybil}/{len(addresses)}\nResults saved in results/{excel.file_name}\n\n> Exit')
