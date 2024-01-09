import os
from pathlib import Path

# def is_majority(items: list[bool]) -> bool:
#     # your code here
#     comp_list =[]
#     for i in items:
#         if i == True:
#             comp_list.append(i)
#     if len(comp_list) > len(list) // 2:
#         return True
#     elif len(comp_list) <= len(list) // 2:s
#         return False


# result = os.system('cmd /k "driverquery"').read()
# result = result.split('\n')[2]
# print(result)

'''file = open('drivers.txt', "r+", encoding="utf-8")
# req_drivers = os.system('driverquery /v')
# file.write(req_drivers)
# for line in file:
#     if "Filesystem" in line:
#         print(line)
file.write('text, here it is')
print(file)
file.close()'''


file_path = Path(r'E:\Документы\new_f.txt')
os.chdir(r'E:\Документы\1.Налоговая\Декларации')
os.chdir('..'*2)
if file_path.exists():
    with open('new_f.txt', 'r') as f:
        for i, line in enumerate(f):
            if i == 3:
                break
        print(line)
else:
    print('File is not found')