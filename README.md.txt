CONVERT_HEIC_to_JPG
- A simple, user-friendly Python application with a GUI to convert `.heic` image files (common on iPhones) into `.jpg` format. Powered by Tkinter and Pillow, this tool helps you to handle Apple’s odd image formats.

background: HEIC (High-Efficiency Image Container) is Apple's default image format on iPhones. It's efficient, but not exactly friendly—most browsers and apps don't like it natively.

Requirements 
Pillow module 
	Type the below two commands in your terminal: 
	"pip install pillow" 
	"pip install pillow-heif"

Two methods: 
    - using terminal: 
        Add the image in HEIC format with name as 'input' in this folder.
        Run converter_terminal.py script
        output image will be generated in this folder
    
    - using GUI: 
        Just run the converter_GUI.py script and pick any HEIC image from any location and then press 'Convert HEIC to jpg'
