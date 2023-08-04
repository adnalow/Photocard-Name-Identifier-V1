import cv2
import os
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def get_image_embedding(image_path, model):
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    embedding = model.predict(img_array)
    return embedding.flatten()

def find_matching_images(query_image_path, user_folder, threshold=0.7):
    # Load the query image and compile a list of filenames for the compiled images in the user folder
    query_embedding = get_image_embedding(query_image_path, model)
    compiled_images_dir = os.path.join("C:\\Users\\reini\\Documents\\Developer Projects\\Python\\Photocard-Name-Identifier-V1\\girl group templates", user_folder)
    compiled_filenames = os.listdir(compiled_images_dir)

    # List to store matching filenames
    matching_filenames = []

    # Loop over compiled images and find matches
    for filename in compiled_filenames:
        compiled_image_path = os.path.join(compiled_images_dir, filename)
        compiled_embedding = get_image_embedding(compiled_image_path, model)

        # Calculate the cosine similarity between the query embedding and the compiled embedding
        similarity = np.dot(query_embedding, compiled_embedding) / (np.linalg.norm(query_embedding) * np.linalg.norm(compiled_embedding))

        if similarity > threshold:
            matching_filenames.append(filename)

    return matching_filenames

# Load MobileNetV2 pre-trained model
model = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224, 224, 3))

# Example usage
user_input_folder = input("Enter the folder name: ")
query_image_path = "C:\\Users\\reini\\Documents\\Developer Projects\\Python\\Photocard-Name-Identifier-V1\\pc query\\query.jpg"
matching_files = find_matching_images(query_image_path, user_input_folder)

if len(matching_files) > 0:
    print("Matching filenames found:")
    for filename in matching_files:
        print(filename)
else:
    print("No matching filenames found.")
