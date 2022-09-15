import tarfile
import glob
from PIL import Image

TAR_PATH = r'Skins.tar'     # Location of Skins tar

# Unpack Tar file
with tarfile.open(TAR_PATH) as f:
    f.extractall()

# Iterate over skins in folder, crop, and save.
for i,filename in enumerate(glob.glob('Skins/*.png')):
    _, imagename = filename.split('\\')
    im = Image.open(filename)
    im32 = im.crop((0,0,64,32))
    im32.save('skins32/'+imagename)
    if i%1000==0:
        print(f"{i} skins cropped.")
else:
    print("All skins cropped.")