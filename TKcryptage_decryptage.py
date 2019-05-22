from PIL import Image
import tkinter as tk

monImage = Image.open("lori.png")
L, H = monImage.size


def image_melange():
    img_horizontale = Image.new("RGB", (L, H))
    img_verticale = Image.new("RGB", (L, H))

    for x in range(0, L, 1):
        for y in range(0, H, 1):
            pixel = monImage.getpixel((x, y))
            if y % 2 == 0:
                img_verticale.putpixel((L - 1 - x, y), (pixel[0], pixel[1], pixel[2]))
            else:
                img_verticale.putpixel((x, y), (pixel[0], pixel[1], pixel[2]))

    for y in range(0, H, 1):
        for x in range(0, L, 1):
            pixel = img_verticale.getpixel((x, y))
            if x % 2 == 0:
                img_horizontale.putpixel((x, H - 1 - y), (pixel[0], pixel[1], pixel[2]))
            else:
                img_horizontale.putpixel((x, y), (pixel[0], pixel[1], pixel[2]))

    img_horizontale.save("ImageM.png")
    img_horizontale.show()


def image_ranger():
    # Attention cette variable n'est pas la même que celles déclarée au tout debut
    # il faut lui donner un autre nom pour eviter la confusion
    monImage = Image.open("ImageMelange.png")
    img_horizontale = Image.new("RGB", (L, H))
    img_verticale = Image.new("RGB", (L, H))

    for y in range(0, H, 1):
        for x in range(0, L, 1):
            pixel = monImage.getpixel((x, y))
            if x % 2 == 0:
                img_horizontale.putpixel((x, H - 1 - y), (pixel[0], pixel[1], pixel[2]))
            else:
                img_horizontale.putpixel((x, y), (pixel[0], pixel[1], pixel[2]))

    for x in range(0, L, 1):
        for y in range(0, H, 1):
            pixel = img_horizontale.getpixel((x, y))
            if y % 2 == 0:
                img_verticale.putpixel((L - 1 - x, y), (pixel[0], pixel[1], pixel[2]))
            else:
                img_verticale.putpixel((x, y), (pixel[0], pixel[1], pixel[2]))

    img_verticale.save("ImageM.png")
    img_verticale.show()


fen1 = tk.Tk()
can1 = tk.Canvas(fen1, width=L, height=H, bg='white')
can1.pack()
photo = tk.PhotoImage(file='lori.png')
img = can1.create_image(L / 2, H / 2, image=photo)
bouton1 = tk.Button(fen1, text='mélanger image', command=image_melange)
bouton1.pack()

bouton2 = tk.Button(fen1, text='ranger image', command=image_ranger)
bouton2.pack()

fen1.mainloop()
