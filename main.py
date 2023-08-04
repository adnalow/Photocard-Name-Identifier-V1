import cv2
import os

def find_matching_images(query_image_path, user_folder, threshold=0.5):
    # Load the query image and compile a list of filenames for the compiled images in the user folder
    query_image = cv2.imread(query_image_path)
    compiled_images_dir = os.path.join("C:\\Users\\reini\\Documents\\Developer Projects\\Python\\Photocard-Name-Identifier-V1\\girl group templates", user_folder)
    compiled_filenames = os.listdir(compiled_images_dir)

    # Initialize feature detector and matcher
    orb = cv2.ORB_create()
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Detect and compute features for the query image
    kp_query, des_query = orb.detectAndCompute(query_image, None)

    # List to store matching filenames
    matching_filenames = []

    # Loop over compiled images and find matches
    for filename in compiled_filenames:
        compiled_image_path = os.path.join(compiled_images_dir, filename)
        compiled_image = cv2.imread(compiled_image_path)

        # Detect and compute features for the compiled image
        kp_compiled, des_compiled = orb.detectAndCompute(compiled_image, None)

        # Match features
        matches = bf.match(des_query, des_compiled)

        # Apply the ratio test to find good matches
        good_matches = [m for m in matches if m.distance < threshold * m.distance]

        # If enough good matches are found, consider it a match and store the filename
        if len(good_matches) > 5:  # You can adjust this threshold based on your needs
            matching_filenames.append(filename)

    return matching_filenames

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
