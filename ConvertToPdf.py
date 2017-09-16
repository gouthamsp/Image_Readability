import fpdf
import os
import glob
from PIL import Image



class CTP(object):
    
    def __init__(self, Directory):
        """
            Convert Images into a pdf
            Args:
                Directory: Directory of the images stored after final processing steps
        """
        self.Directory = Directory


    def convert2pdf(self):
        
        os.chdir(self.Directory)
        pdf = FPDF()
        Filename = "Cambire_Final_PDF.pdf"

        for Img in glob.glob("Final_*.jpg"):
            pdf.add_page()
            pdf.image(Img)

        pdf.output(Filename)

        print "File Saved as Cambire_Final_PDF.pdf"
            
        