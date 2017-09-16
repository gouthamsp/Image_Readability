
import numpy as np
import cv2
import os
import glob
from shutil import copyfile



class CONVERTIMAGE(object):

    def __init__(self, ImagesDict):
        """
            Convert Images to an Enhanced version or maintain the scaling.
            Detects corners of page and use only the part that has content in them.

            Args:
                ImagesDict: Dictionary of Images With Image Location.
                    {
                        data:
                        {
                            ImageName : ImageLocation
                        }
                    }
        """

        self.ImagesList = list()
        self.Directory = list()
        self.ImagesDict = ImagesDict
        self.copyIntoOneDir()


    def copyIntoOneDir(self):
        """
            Copy all the images into one Directory
            That is, CurPath...\Cambire
            and Rename all the copied files it to 'Original_imagename.jpg'
            
            Args:
                No Args needed
        """

        Location = os.path.dirname(os.path.realpath(__file__)) + "\\Cambire"
        ImagesWithDir = list()

        try:
            shutil.rmtree(Location)
        except OSError, e:
            print ("Error: %s - %s." % (e.filename,e.strerror))

        try:
            os.mkdir(Location)
        except OSError:
            pass

        for Image, Dir in self.ImagesDict:
            self.ImagesList.append(Image)
            self.Directory.append(Dir)
            
            ImagesWithDir.append(Dir + "\\" + Image)

        for i in ImagesWithDir:
            copyfile(i, Location)

        os.chdir(Location)

        for image in glob.glob("*.jpg"):
            NewImageName = "Original_" + image
            os.rename(image, NewImageName)


    def ConvertImageToGrayscale(self):
        """
            Converts Image into a Grayscale Image for Enhanced Image Reading
            Args:
                No Args needed
        """
        for ImageName in self.ImagesList:
            GrayImage = cv2.imread(ImageName, cv2.IMREAD_GRAYSCALE)
            ImageName = "Grayscale_" + ImageName
            
            os.chdir(".\Cambire")            
            
            cv2.imwrite(ImageName, GrayImage)
            
            cv2.imshow(ImageName, GrayImage)
            cv2.waitKey(0)
            cv2.closeAllWindows()
            
            os.chdir("..")


    def DefaultEnhance(self):
        """
            Enhance Image using Image Thresholding and Multiple Image Thresholding
            Args:
                No Args needed
        """
        for ImageName in self.ImagesList:
            Convertion = cv2.imread(ImageName, cv2.IMREAD_COLOR)
            
            cv2.imshow("Original Image", Convertion)
            
            os.chdir(".\Cambire")
            
            GrayImage = cv2.cvtColor(Convertion, cv2.COLOR_BGR2GRAY)
            Enhanced = cv2.adaptiveThreshold(GrayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)
            
            # ConvertionImage = "Convertion_" + ImageName
            # GrayscaleImage = "Gray_" + ImageName
            EnhancedImage = "Enhanced_" + ImageName
            TempImagename = "Original_" + ImageName
            
            # cv2.imwrite(ConvertionImage, Convertion)
            # cv2.imwrite(GrayscaleImage, GrayImage)
            cv2.imwrite(TempImagename, Convertion)
            cv2.imwrite(EnhancedImage, Enhanced)
            
            os.chdir("..")


    def DetectCorners(self):
        """
            Detect Page Corners
            Args:
                No Args needed
        """
        os.chdir(self.Directory)
        os.chdir("Cambire")

        for Image in glob.glob("Oringinal_*.jpg"):
            ImageOriginal = cv2.imread(Image, cv2.IMREAD_COLOR)
            GrayscaleImage = cv2.cvtColor(ImageOriginal, cv2.COLOR_BGR2GRAY)

            GrayscaleImage = np.float32(GrayscaleImage)
            cv2.imshow("Enhanced", ImageOriginal)

            corners = cv2.cornerHarris(GrayscaleImage, 2, 3, 1)
            GrayscaleImage = cv2.dilate(GrayscaleImage, None)
            
            ImageOriginal[GrayscaleImage > 0.4 * GrayscaleImage.max()] = [0,0,255]
                
            Imagename = "Cornered_" + Image
            cv2.imwrite(Imagename, ImageOriginal)
            cv2.imshow(Imagename, ImageOriginal)

            cv2.waitKey(0)
            cv2.distroyAllWindows()
            os.chdir("..")


    def DetectCorners(self):
        """
            Detect Page Corners
            Args:
                No Args needed
        """
        os.chdir(self.Directory)
        os.chdir("Cambire")

        for Image in glob.glob("Enhanced_*.jpg"):
            ImageOriginal = cv2.imread(Image, cv2.IMREAD_COLOR)
            GrayscaleImage = cv2.cvtColor(ImageOriginal, cv2.COLOR_BGR2GRAY)

            GrayscaleImage = np.float32(GrayscaleImage)
            cv2.imshow("Enhanced", ImageOriginal)

            corners = cv2.cornerHarris(GrayscaleImage, 2, 3, 1)
            GrayscaleImage = cv2.dilate(GrayscaleImage, None)
            
            ImageOriginal[GrayscaleImage > 0.4 * GrayscaleImage.max()] = [0,0,255]
                
            Imagename = "Cornered_" + Image
            cv2.imwrite(Imagename, ImageOriginal)
            cv2.imshow(Imagename, ImageOriginal)

            cv2.waitKey(0)
            cv2.distroyAllWindows()
            os.chdir("..")


    def PageDetection(self):
        """
            Page corner detection using canny edge detection and probabilistic hough line transform.

            Args:
                No Args needed
        """

        for Img in glob.glob("Original_*.jpg"):
            Page = cv2.imread(Img)
            PageGrayscale = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)

            Edges = cv2.Canny(PageGrayscale, 50, 200, 3)

            """
            plt.subplot(121),plt.imshow(PageGrayscale, cmap = 'gray')
            plt.title('Original Image'), plt.xticks([]), plt.yticks([])
            plt.subplot(122),plt.imshow(edges, cmap = 'gray')
            plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
            plt.show()
            """

            Edgename = "Canny_" + Img
            cv2.imwrite(Edgename, Edges)
            cv2.imshow("Canny", Edges)

            minLineLength = 300
            minLineGap = 5

            Lines = cv2.HoughLinesP(Edges, 1, np.pi/180, 100, minLineLength, minLineGap)
            for x1, y1, x2, y2 in Lines:
                cv2.line(Page, (x1,y1), (x2,y2), (0,0,255), 3)

            Edgename = "Edged_" + Img
            cv2.imwrite(Edgename, Page)
            cv2.imshow("Edged", Page)


def main():
    ImagesDict = {['testimage.jpg':'C:\Users\Goutham\Pictures\9gag']}
    c = CONVERTIMAGE(ImagesDict)
    c.DefaultEnhance()
    c.DetectCorners()


if "__name__" is main():
    main()
