import zipfile as zp
with zp.ZipFile("Zipped rename.zip", "w") as Zip:
    Zip.write("code.png")   
    print("✅ File zipped successfully!")


with zp.ZipFile("Zipped rename.zip", "r") as Zip:
    Zip.extractall("extracted_files")  
    print("✅ File unzipped successfully!")
