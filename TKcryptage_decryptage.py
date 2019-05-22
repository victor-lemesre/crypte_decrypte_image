from PIL import Image
import tkinter as Tk

monImage = Image.open("lori.png")
L, H = monImage.size


def image_melange():
    ImgHorizontale = Image.new("RGB", (L, H))
    ImgVerticale = Image.new("RGB", (L, H))

    for x in range(0, L, 1):
        for y in range(0, H, 1):
            pixel = monImage.getpixel((x, y))
            if y % 2 == 0:
                ImgVerticale.putpixel((L - 1 - x, y), (pixel[0], pixel[1], pixel[2]))
            else:
                ImgVerticale.putpixel((x, y), (pixel[0], pixel[1], pixel[2]))

    for y in range(0, H, 1):
        for x in range(0, L, 1):
            pixel = ImgVerticale.getpixel((x, y))
            if x % 2 == 0:
                ImgHorizontale.putpixel((x, H - 1 - y), (pixel[0], pixel[1], pixel[2]))
            else:
                ImgHorizontale.putpixel((x, y), (pixel[0], pixel[1], pixel[2]))

    ImgHorizontale.save("ImageM.png")
    ImgHorizontale.show()


def image_ranger():
    monImage = Image.open("ImageMelange.png")
    ImgHorizontale = Image.new("RGB", (L, H))
    ImgVerticale = Image.new("RGB", (L, H))

    for y in range(0, H, 1):
        for x in range(0, L, 1):
            pixel = monImage.getpixel((x, y))
            if x % 2 == 0:
                ImgHorizontale.putpixel((x, H - 1 - y), (pixel[0], pixel[1], pixel[2]))
            else:
                ImgHorizontale.putpixel((x, y), (pixel[0], pixel[1], pixel[2]))

    for x in range(0, L, 1):
        for y in range(0, H, 1):
            pixel = ImgHorizontale.getpixel((x, y))
            if y % 2 == 0:
                ImgVerticale.putpixel((L - 1 - x, y), (pixel[0], pixel[1], pixel[2]))
            else:
                ImgVerticale.putpixel((x, y), (pixel[0], pixel[1], pixel[2]))

    ImgVerticale.save("ImageM.png")
    ImgVerticale.show()


fen1 = Tk.Tk()
can1 = Tk.Canvas(fen1, width=L, height=H, bg='white')
can1.pack()
photo = Tk.PhotoImage(file='lori.png')
img = can1.create_image(L / 2, H / 2, image=photo)
bouton1 = Tk.Button(fen1, text='mélanger image', command=image_melange)
bouton1.pack()

bouton2 = Tk.Button(fen1, text='ranger image', command=image_ranger)
bouton2.pack()

fen1.mainloop()
