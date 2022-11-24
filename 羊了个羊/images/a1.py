from PIL import Image
for i in range(1,16): 
    img = Image.open('D:\\begga\\Documents\\代码\\app\\images\\images\\' + 'tile' + str(i) + '.png')

    img.thumbnail((60,66))
    img.save('tile' + str(i) + '.png')