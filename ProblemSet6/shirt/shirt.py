import sys
from os.path import splitext
from PIL import Image, ImageOps 

def main():
    check_commend_line_arg()
    #open image-file 
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        print("Input does not exist")
    #open shirt-file
    shirtfile = Image.open("shirt.png")
    #get size of shirt-file
    size = shirtfile.size
    #Resize (muppet資料夾內的image) of fit shirt
    muppet = ImageOps.fit(imagefile, size)
    #paste shirt-file into muppet-image 
    muppet.paste(shirtfile, shirtfile)
    #create output image
    muppet.save(sys.argv[2])
    

def check_commend_line_arg():
    #check len of command line argument right 
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    #check command line arguments file format(input and output)
    if check_extension(file1[1]) == False:
        sys.exit("Invalid input")
    if check_extension(file2[1]) == False:
        sys.exit("Invalid output")
    #check input and output file format(檔案格式) is same
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")

#check command line arguments file format(input and output)(圖檔)
def check_extension(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
