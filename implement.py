import os
import numpy as np
import PIL
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_image(image_path, target_size=(224, 224)):
    # Load and preprocess the input image
    img = load_img(image_path, target_size=target_size)
    img_array = img_to_array(img)
    img_array = preprocess_input(img_array)
    return img_array

def extract_features(model, images):
    # Extract features from the input images using the specified model
    features = model.predict(images)
    return features.reshape(features.shape[0], -1)

def find_similar_images(input_image_features, dataset_features, dataset_filepaths, similarity_threshold=0.5, max_display=10):
    # Calculate cosine similarity between input image features and dataset features
    similarities = cosine_similarity(input_image_features, dataset_features)

    # Filter dataset images based on cosine similarity scores and similarity threshold
    high_similarity_indices = np.where(similarities > similarity_threshold)[1]
    
    # Count the number of images in the dataset that have a similarity score over the threshold
    num_images_over_threshold = len(high_similarity_indices)
    print(f"Number of images in the dataset with similarity score > {similarity_threshold}: {num_images_over_threshold}")

    # Limit the number of images to display based on the maximum display count
    num_similar_images = min(num_images_over_threshold, max_display)
    if num_similar_images == 0:
        print("No similar images found above the similarity threshold.")
        return

    # Calculate number of rows and columns for subplot layout
    rows = (num_similar_images + 1) // 2  # Number of rows (each row contains 2 images)
    cols = 2  # Fixed number of columns

    # Create a figure with appropriate size
    plt.figure(figsize=(16, 5 * rows))

    # Display images with high similarity scores above the threshold
    for i in range(num_similar_images):
        idx = high_similarity_indices[i]
        img_path = dataset_filepaths[idx]
        similarity_score = similarities[0][idx]

        # Load and display the image
        img = PIL.Image.open(img_path)
        plt.subplot(rows, cols, i + 1)
        plt.imshow(img)
        plt.title(f'Similarity: {similarity_score:.2f}')
        plt.axis('off')

    # Display the input image if there's space left in the grid
    if num_similar_images % 2 != 0:
        plt.subplot(rows, cols, num_similar_images + 1)
        input_img = PIL.Image.open(input_image_path)
        plt.imshow(input_img)
        plt.title('Input Image')
        plt.axis('off')

    plt.tight_layout()  # Adjust spacing between subplots
    plt.show()

# Define paths and parameters
data_dir = r'C:\Users\AliMa\Desktop\ObjectDetection\Bachelor\val2017'
input_image_path = r'C:\Users\AliMa\Desktop\ObjectDetection\Bachelor\input8.jpg'
img_height, img_width = 224, 224  # ResNet50 input size
similarity_threshold = 0.5  # Minimum similarity score threshold (50%)
max_display = 20  # Maximum number of similar images to display

# Load pre-trained ResNet50 model for feature extraction
base_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Check if saved features exist
if os.path.exists('dataset_features.npy') and os.path.exists('dataset_filepaths.npy'):
    # Load saved features and filepaths from disk
    dataset_features = np.load('dataset_features.npy')
    dataset_filepaths = np.load('dataset_filepaths.npy')
else:
    # Manually load and preprocess dataset images
    dataset_filepaths = [os.path.join(data_dir, filename) for filename in os.listdir(data_dir) if filename.endswith(('.jpeg', '.jpg', '.png'))]
    dataset_images = [preprocess_image(filepath, target_size=(img_height, img_width)) for filepath in dataset_filepaths]
    dataset_images = np.array(dataset_images)

    # Extract features for the dataset images
    dataset_features = extract_features(base_model, dataset_images)

    # Save extracted features and corresponding filepaths
    np.save('dataset_features.npy', dataset_features)
    np.save('dataset_filepaths.npy', np.array(dataset_filepaths))

# Load and preprocess the input image
input_image = preprocess_image(input_image_path, target_size=(img_height, img_width))
input_image = np.expand_dims(input_image, axis=0)  # Add batch dimension

# Extract features for the input image
input_image_features = extract_features(base_model, input_image)

# Find and display similar images with high similarity scores above the threshold
find_similar_images(input_image_features, dataset_features, dataset_filepaths, similarity_threshold, max_display)