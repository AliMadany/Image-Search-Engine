import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cosine

# Path to the dataset
data_dir = r"F:\Bachelor Thesis\Bachelor\val2017"

# Function to get color histogram vector
def get_vector(image, bins=32):
    red = cv2.calcHist([image], [2], None, [bins], [0, 256])
    green = cv2.calcHist([image], [1], None, [bins], [0, 256])
    blue = cv2.calcHist([image], [0], None, [bins], [0, 256])
    vector = np.concatenate([red, green, blue], axis=0)
    vector = vector.reshape(-1)
    return vector

# Function to load images from a directory
def load_images_from_directory(directory):
    images = []
    paths = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(directory, filename)
            image = cv2.imread(img_path)
            if image is not None:
                images.append(image)
                paths.append(img_path)
    return images, paths

# Convert list of vectors to a numpy array for easier manipulation
def convert_vectors_to_array(vectors):
    return np.array(vectors)

# Function to find similar images based on cosine similarity
def find_similar_images(query_vector, dataset_vectors, dataset_paths, top_k=10):
    distances = [cosine(query_vector, vector) for vector in dataset_vectors]
    # Get top k most similar images
    top_indices = np.argsort(distances)[:top_k]
    return [dataset_paths[idx] for idx in top_indices]

def main1(input_image_path):
    data_dir = r"F:\Bachelor Thesis\Bachelor\val2017"
    top_k = 200
    # Load dataset images and compute their vectors
    images, image_paths = load_images_from_directory(data_dir)
    image_vectors = [get_vector(image) for image in images]
    image_vectors = convert_vectors_to_array(image_vectors)

    # Load the query image
    query_image = cv2.imread(input_image_path)
    if query_image is not None:
        query_vector = get_vector(query_image)

        # Find similar images
        similar_image_paths = find_similar_images(query_vector, image_vectors, image_paths, top_k=top_k)

        return similar_image_paths
    else:
        print("Failed to load the query image.")
        return []



# Function to plot similar images with a maximum of 5 images per window
def plot_similar_images(similar_image_paths):
    num_images = len(similar_image_paths)
    num_windows = (num_images + 4) // 5  # Calculate the number of windows needed
    start_idx = 0

    for window_idx in range(num_windows):
        end_idx = min(start_idx + 5, num_images)  # Determine the end index for the current window
        fig, axes = plt.subplots(1, end_idx - start_idx, figsize=(15, 5))

        for i, image_idx in enumerate(range(start_idx, end_idx)):
            # Read the image using OpenCV
            image = cv2.imread(similar_image_paths[image_idx])
            # Convert from BGR to RGB color space for matplotlib
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            axes[i].imshow(image)
            axes[i].axis('off')

        plt.tight_layout()
        plt.show()

        start_idx = end_idx  # Update the start index for the next window

