from PIL import Image
import os


for file in os.listdir('orig'):  # '.' 表示與此py檔同資料夾檔案  不同資料夾直接輸入資料夾名稱
	if file.endswith('.jpg'):     # 檢查檔案結尾
		image_file = Image.open(os.path.join('orig', file))   # os.path.join(filename, file) 合併路徑
		image_file = image_file.convert('L')
		image_file.save(os.path.join('result',file[:-4]  + '_grey.png'))
			