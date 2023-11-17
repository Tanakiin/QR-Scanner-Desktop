# QR Code Scanner Desktop

This Python script utilizes the Tkinter library to create a simple QR code scanner with a draggable rectangle interface. The code allows users to capture a screenshot of a selected area on the screen using a draggable rectangle. The captured image is then processed to decode any QR codes present within the selected region.

## Dependencies

- **Tkinter**: Used for creating the graphical user interface.
- **PIL (Pillow)**: Required for capturing screenshots.
- **pyzbar**: Utilized for decoding QR codes.
- **webbrowser**: Used to open the decoded URL in the default web browser.
- **keyboard**: Used for defining a hotkey to activate the QR code scanning.

## Usage

1. Run the script.
2. Press and hold the defined hotkey (`ctrl+alt+q` by default) to activate the draggable rectangle interface.
3. Drag the rectangle to select a region on the screen.
4. Release the mouse button to capture the screenshot of the selected area.
5. If a QR code is found in the screenshot, its data is extracted and opened in the default web browser.
6. If no QR code is found, a message is printed indicating the absence of QR codes.
7. The script continues to run, allowing for repeated scanning with the defined hotkey.

## Notes

- The draggable rectangle is created using Tkinter canvas.
- The script utilizes the `ImageGrab` module from PIL to capture screenshots.
- QR codes are decoded using the `decode` function from the `pyzbar` library.
- The decoded data, if a QR code is found, is opened in the default web browser.
- The script runs indefinitely, waiting for the hotkey to be pressed to initiate the scanning process.

**Note**: Ensure that all dependencies are installed before running the script.
