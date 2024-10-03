# Tkinter Application in Python

This document provides a step-by-step guide to set up, run, and test the provided Python script. The script is a GUI application using Tkinter to display images of famous paintings. The instructions cover the creation of a virtual environment, installation of dependencies, and running the application to ensure it works as expected.

## Prerequisites

- Python 3.x installed on your machine.
- An active internet connection to install necessary packages.
- The script `main.py` containing the provided code.

## Steps for Testing

### 1. Set Up a Virtual Environment

A virtual environment helps in managing dependencies in isolation, ensuring no conflicts with other Python projects on your machine.

1. **Create a Virtual Environment:**

   Run the following command in your terminal or command prompt:

   ```bash
   python -m venv venv
   ```

   This command will create a virtual environment named `venv` in your current directory.

2. **Activate the Virtual Environment:**

   Depending on your operating system, activate the virtual environment with one of the following commands:

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

### 2. Create `requirements.txt`

The script requires the `Pillow` library to handle image processing. Create a `requirements.txt` file with the following content:

```
Pillow
```

Save this file in the same directory as your Python script (`main.py`).

### 3. Install Dependencies

Once the virtual environment is activated, install the required packages listed in `requirements.txt` by running:

```bash
pip install -r requirements.txt
```

This command will install `Pillow`, which is essential for handling image operations in the provided script.

### 4. Prepare the Images

Ensure that the necessary images are available in the specified paths:

- **Image Paths:**
  - `images/gioconda.jpg`
  - `images/the_scream.jpg`
  - `images/the_girl_with_the_pearl.jpg`

Place these images in a directory named `images` in the same folder as `main.py`. Make sure the filenames match exactly as specified, or adjust the paths in the script accordingly.

### 5. Run the Application

With the dependencies installed and images prepared, you can now run the script:

```bash
python main.py
```

### 6. Test Functionality

The application window should appear with three buttons corresponding to the names of famous painters:

- **Leonardo da Vinci**
- **Edvard Munch**
- **Johannes Vermeer**

Test the following functionalities:

1. **Painter Buttons:**

   - Click on each painter’s button to display the corresponding painting.
   - Ensure that the image is properly loaded and displayed in the window.
   - The image should be resized to fit a size of 300x400 pixels.

2. **Close Painting Button:**

   - After displaying a painting, click the "Cerrar pintura" button.
   - Verify that the image disappears.

3. **Close Application:**

   - Click the "Cerrar ventana" button to close the application.
   - Confirm the prompt asking whether you want to close the window.

4. **Error Handling:**
   - Try removing or renaming one of the images and click on the corresponding button.
   - Ensure that an error message appears, informing you that the image could not be opened.

### 7. Deactivate the Virtual Environment

After testing, deactivate the virtual environment:

```bash
deactivate
```

## Expected Outcomes

- Each button should correctly display the respective image.
- Images should be properly resized and displayed without distortion.
- Clicking "Cerrar pintura" should remove the image from the view.
- Clicking "Cerrar ventana" should prompt for confirmation and close the app if confirmed.
- If an image is missing, an error message should be displayed.

## Troubleshooting

- **Tkinter Not Found Error**: Tkinter is included with most Python installations. If you receive an error, ensure Python was installed with standard libraries or reinstall Python.
- **Images Not Found**: Ensure the images are in the correct path relative to `main.py`.
- **Virtual Environment Activation Issues**: Make sure you are using the correct command for your operating system.

## Summary

This documentation walks you through setting up a virtual environment, installing dependencies, running the GUI application, and testing each feature to ensure proper functionality. By following these steps, you should be able to verify that the Python script works as intended.
