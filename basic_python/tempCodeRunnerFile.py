import zipfile as zp

Zip = zp.ZipFile('Zipped rename.zip', 'w')

Zip.write("code.png")
