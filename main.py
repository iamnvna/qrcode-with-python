import qrcode

data = input("Enter the data for the QR Code below: \n")

img = qrcode.make(data)

img.save("C:/Users/cobbi/Desktop/Learn/qrcode-with-python/QRfile.png")

## Commentary
"""
Line 1:
    The required library for creating a QR Code in python is you guessed 
    it, qrcode. There are other libraries that can help too. If the library
    is not already installed in your working environment, use "pip install
    qrcode" to install it through the terminal.
    
Line 3: 
    The data variable is declared to collect input that would make the 
    content of the QR Code. 
    
Line 5:
    The img variable is declared to hold the encoded data as an image file.
    
Line 7:
    The save function is called to save the encoded image into a designated
    folder which is appended with the desired file name, QRfind.png in this
    case. 
"""
