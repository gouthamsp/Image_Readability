from PIL import Image
import os
import glob
from fpdf import FPDF


__version__ = 1.0


class PROCESSPDF(object):
    """
        Class to process the image and convert it to pdfs
        Args:
            ImagesDir: Directory where Images are stored
            ImagesNameList: List of Images that need to be converted
    """

    def __init__(self, ImagesDir, ImagesNamesList):
        self.ImagesNameList = list()
        os.chdir(ImagesDir) # Change the Directory to Image's Directory
        for ImageName in ImagesNamesList:
            print ImageName
            self.ImagesNameList.append(ImageName)
        print self.ImagesNameList


    def AskOriginalOrGrayscale(self):
        """
            Ask the user if the image should be read in Grayscale or never change the format
            Args:
                No Args needed
        """
        print "Choose Original or Grayscale Image: "
        print "1> Original      2> Grayscale"
        UserChoice = input("Choose (1/2): ")
        
        if UserChoice is 2:
            print "Converting to Grayscale"
            self.ConvertToGrayscale()
        elif UserChoice is 1:
            print "Using Original Image"
            self.UseOriginalImage()
        else:
            print "Invalid Choice"


    def ConvertToGrayscale(self):
        """
            Convert the image to a grayscale version
            Args:
                No args needed
        """
        for ImageName in self.ImagesNameList:
            print ImageName
            OriginalImage = Image.open(ImageName) # open colour image
            OriginalImage = OriginalImage.convert('1') # convert image to black and white
            self.ImageNameAfter = "Cambire_" + ImageName
            os.chdir("C:\Users\Goutham\Pictures\9gag\Cambire")
            OriginalImage.save(self.ImageNameAfter, "JPEG", quality=100)
            os.chdir("C:\Users\Goutham\Pictures\9gag")


    def UseOriginalImage(self):
        """
            Use the original image specified by the user
            Args:
                No args needed
        """
        for ImageName in self.ImagesNameList:
            print ImageName
            OriginalImage = Image.open(ImageName)
            self.ImageNameAfter = "Cambire_" + ImageName
            os.chdir("C:\Users\Goutham\Pictures\9gag\Cambire")           
            OriginalImage.save(self.ImageNameAfter, "JPEG")
            os.chdir("C:\Users\Goutham\Pictures\9gag")            


    def ConvertToPdf(self):
        """
            Convert images that are already converted into a pdf
            Args:
                No args needed
        """
        pdf = FPDF()
        FileName = "Cambire_PDF.pdf"
        os.chdir("C:\Users\Goutham\Pictures\9gag\Cambire")
        for ImageNameTemp in glob.glob("C:\Users\Goutham\Pictures\9gag\Cambire\Cambire_*.jpg"):
            ConversionImage = Image.open(ImageNameTemp)
            pdf.add_page()
            pdf.image(ImageNameTemp)
        pdf.output(FileName, "F")	
        os.chdir("C:\Users\Goutham\Pictures\9gag")
        print "Your File is saved as Cambire_PDF.pdf"



def main():
    temporarydir = "Cambire"
    ImagesList = ['aeYZvZB_460s.jpg', 'ajqLpBQ_460s.jpg']
    ImagesDir = "C:\Users\Goutham\Pictures\9gag"
    ConvertToPDF = PROCESSPDF(ImagesDir, ImagesList)
    try:
        os.mkdir(temporarydir)
    except OSError, IOError:
        pass
    ConvertToPDF.AskOriginalOrGrayscale()
    ConvertToPDF.ConvertToPdf()


if __name__ == '__main__':
    main()