import cv2
import numpy as np
import os
import random
import shutil

# Add noise to simulate scan quality
def add_noise(img):
    noise_factor=random.uniform(0.1, 0.3)
    noise = np.random.normal(0, noise_factor * 255, img.shape)
    noisy_image = np.clip(img + noise, 0, 255).astype(np.uint8)
    return noisy_image

def pixelate_image(img, block_size):
    """
    Creates a pixelation effect without reducing resolution.

    Parameters:
        img (numpy.ndarray): Input image.
        block_size (int): Size of the pixelation block (e.g., 8).
    
    Returns:
        numpy.ndarray: Pixelated image.
    """
    h, w, c = img.shape
    # Ensure image dimensions are divisible by block size
    temp_img = img.copy()
    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            # Define the block
            block = temp_img[y:y + block_size, x:x + block_size]
            # Compute the average color of the block
            avg_color = block.mean(axis=(0, 1), dtype=int)
            # Assign the average color to all pixels in the block
            temp_img[y:y + block_size, x:x + block_size] = avg_color
    return temp_img

# Function to apply subtle perspective transformation using OpenCV
def apply_subtle_perspective_transform(image):
    rows, cols = image.shape[:2]

    # Define subtle random perspective transform points
    pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])
    pts2 = np.float32([[random.randint(10, 40), random.randint(10, 40)],  # Top-left
                       [cols - random.randint(10, 40), random.randint(10, 40)],  # Top-right
                       [random.randint(10, 40), rows - random.randint(10, 40)],  # Bottom-left
                       [cols - random.randint(10, 40), rows - random.randint(10, 40)]])  # Bottom-right

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    transformed_image = cv2.warpPerspective(image, matrix, (cols, rows))
    return transformed_image

# Augment function using OpenCV
def augment_receipt_image(image_path,i):
    descale_factor = random.uniform(0.35, 0.5)
    x=int(3600*descale_factor)
    y = int(480 * descale_factor)
    # Read image using OpenCV
    image = cv2.imread(image_path)

    # Resize image
    image = cv2.resize(image, (x, y))

    #Randomly rotate the image
    angle = random.uniform(-5, 5)  # Rotation angle between -5 and 5 degrees
    M = cv2.getRotationMatrix2D((x // 2, y // 2), angle, 1)
    image = cv2.warpAffine(image, M, (x, y))

    # Apply color jitter (brightness/contrast adjustment)
    alpha = random.uniform(0.3, 2.0)  # Contrast control
    beta = random.uniform(-30, 50)    # Brightness control
    image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # Add noise
    image = add_noise(image)
    #if(random.randint(0,1)==1):
      #  image=pixelate_image(image,2)
       # print("pixelated ",i)

    # Apply subtle perspective transformation
    image = apply_subtle_perspective_transform(image)

    # Save the augmented image
    
    new_filename = f"data/ron_{17999+i}.tif"
    cv2.imwrite(new_filename, image)  # Save image with OpenCV

    print(f"Augmented image saved as: {new_filename}")


for i in range(8999):
    image_path = f"data/ron_{i}.tif"
    augment_receipt_image(image_path,i)
    shutil.copy(f"data/ron_{i}.gt.txt", f"data/ron_{17999+i}.gt.txt")
    #shutil.copy(f"data/ron_{i}.box", f"data/ron_{9000+i}.box")