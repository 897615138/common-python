import os
import time
import zipfile

source = ['.\\tmp\\my_log.txt',
          '.\\tmp\\pic1.jpg',
          '.\\tmp\\pic2.jpg',
          '.\\tmp\\temp.txt',
          '.\\tmp\\song.wma'
          ]  # files you want to archive
target_dir = 'backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)  # make directory
    print('Successfully created directory', today)

for i in range(0, len(source)):
    with zipfile.ZipFile(target, 'a') as my_zip:
        my_zip.write(source[i])

print('Successful backup to', target)

input('Press Enter to continue!')
