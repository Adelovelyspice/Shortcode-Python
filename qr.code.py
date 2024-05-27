import qrcode

# Function to generate a QR code
def generate_qr(data, filename):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # control the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)

# Example usage
if __name__ == "__main__":
    # Data to be encoded in the QR code
    data = "https://www.example.com"
    
    # Filename to save the QR code image
    filename = "example_qr.png"
    
    # Generate and save the QR code
    generate_qr(data, filename)
    print(f"QR code generated and saved as {filename}")
