from PIL import Image
import tkinter as tk


def image_melange(monimage):
    L, H = monimage.size
    img_horizontale = Image.new("RGB", (L, H))
    img_verticale = Image.new("RGB", (L, H))

    for x in range(0, L, 1):
        for y in range(0, H, 1):
            pixel = monimage.getpixel((x, y))
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

    return img_horizontale


def image_ranger(myimage):
    # Attention cette variable n'est pas la même que celles déclarée au tout debut
    # il faut lui donner un autre nom pour eviter la confusion

    img_horizontale = Image.new("RGB", (L, H))
    img_verticale = Image.new("RGB", (L, H))

    for y in range(0, H, 1):
        for x in range(0, L, 1):
            pixel = myimage.getpixel((x, y))
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


def affichage():
    can1.itemconfig(photo,image=img_horizontale)



monimage = Image.open("lori.png")
L, H = monimage.size
fen1 = tk.Tk()
can1 = tk.Canvas(fen1, width=L, height=H, bg='white')
can1.pack()
photo = tk.PhotoImage(file='lori.png')
can1.create_image(L / 2, H / 2, image=photo)
bouton1 = tk.Button(fen1, text='mélanger image', command=lambda: image_melange(monimage))
bouton1.pack()

bouton2 = tk.Button(fen1, text='ranger image', command=lambda: image_ranger(myimage))
bouton2.pack()

fen1.mainloop()
