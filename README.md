# Photocard-Name-Identifier-V1
:snake:A python based photocard name identifier 
---
# Program name: *Recognayz*
---
## :book: Library used:
* opencv-python
* tensorflow
---
## :question:*How it works*
The program utilizes two main folders. The first folder holds subfolders named after different idols, each containing photocard templates specific to that idol. The second folder contains images of photocard samples that the user wants to identify.

The program initiates by prompting the user to provide the name of the idol featured in their photocard. It will then use this input to search for a matching folder within the templates directory. If a match is found, the program proceeds to search for similar photos to the provided photocard and eventually reveals the name of the idol featured in the user's input image.

---
## :art:*Program Personalization*
If ever that you want to use your own template and allow the program to use it so that you can finally use this program, just follow these steps:

1. Make a new folder under templates named to the idol 
2. Inside that folder, put all the photocard templates. 
    Make sure to rename each photocard to their respective names.
3. Replace the query.jpg under the pc query folder with the picture of the photocard that you want to know the name.
    Don't forget to rename the picture back to query.jpg
4. Run the program 

*Important note!*:loudspeaker: 
    
If you want to adjust the accuracy of the the program, just adjust the threshold level in main.py. The existing threshold is tested on the existing template so just adjust adjust it based on the accuracy that will be given by the program by using your own template

---





