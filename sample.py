import cv2
import os

# Read image
img = cv2.imread("mypic.jpg")

if img is None:
    print("Error: Image not found")
    exit()

# Get message and password (password is not used in this code, but you can implement encryption later)
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Dictionary to map characters to their ASCII values
d = {chr(i): i for i in range(255)}  # Mapping from character to ASCII
c = {i: chr(i) for i in range(255)}  # Mapping from ASCII to character

# Check if the image has enough space to hide the message
height, width, _ = img.shape
max_chars = height * width

if len(msg) > max_chars:
    print("Error: Message is too long to encode in the image")
    exit()

# Variables to track pixel positions
n, m, z = 0, 0, 0

# Encoding the message
for i in range(len(msg)):
    # Get ASCII value of the character
    ascii_value = d[msg[i]]
    
    # Modify the least significant bit of the pixel values
    pixel = img[n, m]
    pixel[z] = (pixel[z] & 0xFE) | (ascii_value & 0x01)  # Replace LSB of the pixel channel
    n += 1
    m += 1
    z = (z + 1) % 3  # Cycle through R, G, B channels

    if m == width:  # Move to the next row after reaching the width of the image
        m = 0
        n += 1

    if n == height:  # If we've reached the bottom of the image, stop encoding
        break

# Save the image with the hidden message
cv2.imwrite("encryptedImage.jpg", img)

# Open the image (on Windows)
os.system("start encryptedImage.jpg")
