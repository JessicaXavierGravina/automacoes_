#Otimizador de Imagem
# pip install Pillow
import PIL

# Corta a Imagem
im = PIL.Image.open("imagem.jpg")
im = im.crop((34, 23, 100, 100))

# Redimensiona
im = PIL.Image.open("imagem.jpg")
im = im.resize((50, 50))

# Flipping
im = PIL.Image.open("imagem.jpg")
im = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)

# Gira
im = PIL.Image.open("imagem.jpg")
im = im.rotate(180)

# Comprime
im = PIL.Image.open("imagem.jpg")
im.save("imagem.jpg", optimize=True, quality=90)

# Desfoca
im = PIL.Image.open("imagem.jpg")
im = im.filter(PIL.ImageFilter.BLUR)

# Nitidez
im = PIL.Image.open("imagem.jpg")
im = im.filter(PIL.ImageFilter.SHARPEN)

# Define Brilho
im = PIL.Image.open("imagem.jpg")
im = PIL.ImageEnhance.Brightness(im)
im = im.enhance(1.5)

# Define Contraste
im = PIL.Image.open("imagem.jpg")
im = PIL.ImageEnhance.Contrast(im)
im = im.enhance(1.5)

# Adiciona Filtros
im = PIL.Image.open("imagem.jpg")
im = PIL.ImageOps.grayscale(im)
im = PIL.ImageOps.invert(im)
im = PIL.ImageOps.posterize(im, 4)

# Salva
im.save("imagem.jpg")
        
######################################################

# Otimizador de Video
# pip install moviepy
import moviepy.editor as pyedit

# Carrega o Video
video = pyedit.VideoFileClip("vid.mp4")

# Corta partes do video
vid1 = video.subclip(0, 10)
vid2 = video.subclip(20, 40)
final_vid = pyedit.concatenate_videoclips([vid1, vid2])

# Acelera video
final_vid = final_vid.speedx(2)

# Adiciona audio
aud = pyedit.AudioFileClip("bg.mp3")
final_vid = final_vid.set_audio(aud)

# Inverter
final_vid = final_vid.fx(pyedit.vfx.time_mirror)

# Mescla dois videos
vid1 = pyedit.VideoFileClip("vid1.mp4")
vid2 = pyedit.VideoFileClip("vid2.mp4")
final_vid = pyedit.concatenate_videoclips([vid1, vid2])

# Adiciona efeitos visuais
vid1 = final_vid.fx(pyedit.vfx.mirror_x)
vid2 = final_vid.fx(pyedit.vfx.invert_colors)
final_vid = pyedit.concatenate_videoclips([vid1, vid2])

# Adiciona imagens
img1 = pyedit.ImageClip("img1.jpg")
img2 = pyedit.ImageClip("img2.jpg")
final_vid = pyedit.concatenate_videoclips([img1, img2])

# Salva
final_vid.write_videofile("final.mp4")

