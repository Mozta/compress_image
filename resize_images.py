import sys , os, glob
from PIL import Image
cont =0

# Configuracion
diri = '/home/mozta/Documentos/Enviar'
#directorio donde tendremos nuestras imagenes
qualityimg = 80 #calidad de salida de las imagenes
# termina configuracion
print "comprimiendo1..."
for img in glob.glob(diri+'.JPG'):
    try:
        namefile =os.path.basename(img)
        print namefile
        splitname =  os.path.splitext(namefile)
        namefile = splitname[0]
        extens = splitname[1]
        i = Image.open(img)
        i.save(diri+"compress_"+namefile+extens,quality=qualityimg)
    except ValueError:
        print ValueError
        cont=cont +1
if cont >0:
    print "Algunos archivos no se puedieron comprimir"
else:
    print "todos los ficheros fueron comprimidos con exito"
