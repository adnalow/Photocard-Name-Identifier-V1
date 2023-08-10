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
To utilize your own template and enable the program to identify it, kindly adhere to these steps:

1. Create a new folder within the "templates" directory, naming it after the idol.
2. Place all the photocard templates inside that folder, ensuring each photocard is renamed according to their respective names.
3. Replace the existing "query.jpg" in the "pc query" folder with the picture of the photocard you want to identify. 
    Remember to rename the     picture back to "query.jpg."
4. Execute the program, and you're all set! It will now identify the photocard based on your customized template.

*Important note!*:loudspeaker: 
    
To fine-tune the accuracy of the program, follow these steps:

1. Open the "main.py" file.
2. Look for the threshold level variable in the code.
3. This threshold is currently optimized for the existing template, but you can easily modify it to suit your own template.
4. Run the program with your customized template and observe the accuracy provided by the program.
5. Based on the program's accuracy output, adjust the threshold level accordingly. 
    Increase the threshold if you want to be more lenient in matching, or decrease it for stricter matching.
6. Keep experimenting with different threshold levels until you achieve the desired accuracy for your template.

By adjusting the threshold level, you can optimize the program to accurately recognize photocard templates based on your specific requirements.
Having a clear image for your template can also boost the recongnition accuracy to maxinum level.
---





