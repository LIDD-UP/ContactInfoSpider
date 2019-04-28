from PIL import Image

print_file = open('./print_file.txt','w',encoding='utf8')

image1 = Image.open('./captcha1.png')
image2 = Image.open('./captcha2.png')

# 对比像素
image1_pix_obj = image1.load()
image2_pix_obj = image2.load()

print(image1.size)
print(image2.size)
print(image1.mode)
print(image2.mode)

big_pixel_gap_list = []

for x in range(image1.size[0]):
    for y in range(image1.size[1]):
        image1_rgb_value = image1_pix_obj[x,y]
        image2_rgb_value = image2_pix_obj[x,y]
        print(image1_rgb_value,file=print_file)
        print(image2_rgb_value,file=print_file)
        print('--------------',file=print_file)
        # print(image1_rgb_value - image2_rgb_value)
        # if image1_rgb_value != image2_rgb_value: # 通过全部的像素的比对不同获得出的结果很不好
        if abs(image1_pix_obj[x,y][0] - image2_pix_obj[x,y][0]) >20:
                # and abs(image1_pix_obj[x,y][1] - image2_pix_obj[x,y][1]) >15 and abs(image1_pix_obj[x,y][2] - image2_pix_obj[x,y][2]) >15: # 通过第一个像素的对比效果要好一点， # 而且阈值的把控要设置好

            print('像素不同',file=print_file)
            image_location_and_pixel = (x,y,image1_pix_obj[x,y])
            big_pixel_gap_list.append(image_location_and_pixel)

print(big_pixel_gap_list,file=print_file)
print(len(big_pixel_gap_list),file=print_file)



# new_image_obj
new_image_obj = Image.new('RGBA',(image1.size[0],image1.size[1]))
new_image_obj_pixel_data = new_image_obj.load()
for i in range(new_image_obj.size[0]):
    for j in range(new_image_obj.size[1]):
        new_image_obj_pixel_data[i,j] = (255,255,255,255)
#
#
#
x_list = []
for image_info in big_pixel_gap_list:
    x,y,pixel_data = image_info

    new_image_obj_pixel_data[x,y] = pixel_data
    x_list.append(x)

print(min([x for x in x_list if x >60]))
print_file.close()
new_image_obj.save('./different2.png')
