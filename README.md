# Image_Readability
Improves Images' context for easier readability


Uses OpenCV to recognise the corners and enhance image for 200% readability.
Misses the corner detection when a page is not completly covered in the image.
Converts it into a Printable Document after the image is enhanced.


# Corner Detection Technology
  * Harris Corner detection
  * Canny Edge detection.
  * Hough Line Transformation
  * Probabilistic Hough Line Transform
    Reference : 
        https://goo.gl/h3TLz8 (Harris Corner Detection)
        https://goo.gl/8PXQbi (Hough Line Transform)
        https://goo.gl/4eRkCD (Canny Edge Detection)
  
# Image Readability Improvement
  * OpenCV Thresholding
  * Adaptive Thresholding
    Reference :
        https://goo.gl/oMtYKX
