import cv2

def cartoonify_image(img_cv2):
    """
    Takes an OpenCV BGR image (numpy array) and returns cartoonified version.
    """
    # Convert to grayscale
    gray = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur
    gray_blur = cv2.medianBlur(gray, 5)
    
    # Detect edges
    edges = cv2.adaptiveThreshold(
        gray_blur,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        blockSize=9,
        C=9
    )
    
    # Smooth color image
    color = cv2.bilateralFilter(img_cv2, d=9, sigmaColor=250, sigmaSpace=250)
    
    # Combine color and edges
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    return cartoon
