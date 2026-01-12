
W = 500
H = 72

newDrawing()
newPage(W, H)
imagePath = 'words-.png'
imagePath = 'design-models-1498x234.png'
exportPath = f'design-models-{W}x{H}.png'
iw, ih = imageSize(imagePath)
print(iw, ih)
scale(W/iw*1.22)
image(imagePath, (-98, -26))
saveImage(exportPath)

newDrawing()
newPage(W, H)
imagePath = 'design-models-2208-754.png'
exportPath = f'design-models-{W}x{H}.png'
iw, ih = imageSize(imagePath)
print(iw, ih)
scale(W/iw*1.15)
image(imagePath, (-120, 0))
saveImage(exportPath)

