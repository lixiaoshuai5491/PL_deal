import skimage.io as io


def img_unbg(img):
    w = img.shape[0]
    h = img.shape[1]
    ub_img = img.copy()
    print("calculate...")
    for i in range(w):
        for j in range(h):
            if img[i, j, 0] == 0 & img[i, j, 1] == 0 & img[i, j, 2] == 0:
                ub_img[i, j, 3] = 0
    return ub_img


if __name__ == '__main__':
    root_dir = 'C:/Users/Administrator/Desktop/666/'
    img_path = root_dir + '*.bmp'
    # coll = io.ImageCollection(str, load_func=transparent_back)
    coll = io.ImageCollection(img_path)
    for i in range(len(coll)):
        print("All:%d,  processing:%d" % (len(coll), i+1))
        # img = transparent_back(coll[i])
        img = img_unbg(coll[i])
        io.imsave(root_dir + str(i) + '.png', img)
        print("Image %d have saved!" % i)
        io.imshow(coll[0])
        io.show()
    print("All image have saved.")


