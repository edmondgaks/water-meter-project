import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'water-meter-reading.jpg';

image = cv2.imread('water-meter-reading.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to preprocess the image
_, thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Use OCR to extract text from the image
text = pytesseract.image_to_string(thresh)

print("Extracted Text:")
print(text)