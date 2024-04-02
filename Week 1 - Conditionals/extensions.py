awnser = input("File name: ").lower().strip().split(".")

if(awnser[-1] in ["jpg", "jpeg", "gif", "png"]):
    if (awnser[-1] in ["jpg", "jpeg"]):
        print(f"image/jpeg")
    else:
        print(f"image/{awnser[-1]}")

elif(awnser[-1] in ["pdf", "zip", "bin"]):
    if (awnser[-1] in ["bin"]):
        print(f"application/octet-stream")
    else:
        print(f"application/{awnser[-1]}")

elif(awnser[-1] in ["txt"]):
    print(f"text/plain")
else:
    print(f"application/octet-stream")
