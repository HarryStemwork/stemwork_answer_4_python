import zipfile, glob, os, shutil

src_path = r'./beforeCal/discount.txt'
dst_path = r'./afterCal/discount.txt'

shutil.move(src_path, dst_path)

discount_f = open(r'./afterCal/discount.txt', 'r') #how to open discount.txt
finish_f = open(r'./afterCal/finish.txt','a')
for num in discount_f.readlines():
    num = finish_f.write(f'round(int(num) * 0.9, 2)')

discount_f.close()
finish_f.close()

fileZip = zipfile.ZipFile('afterCal.zip','w')
for name in glob.glob('afterCal/*'):
    fileZip.write(name, os.path.basename(name))

fileZip.close()
