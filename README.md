<div align="center">

<p align="center">
<img src="demo.gif" alt="Application Demo" width="800"/>
</p>

# Image Steganography GUI Application

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![OpenCV](https://img.shields.io/badge/opencv-4.x-orange.svg)](https://opencv.org/)
<!-- [![Dependencies](https://img.shields.io/badge/dependencies-auto_managed-brightgreen.svg)]() -->
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey.svg)]()
[![Code Size](https://img.shields.io/github/languages/code-size/aka-0x4C3DD/aicte25-ibmSB-b4.svg)]()
[![Last Commit](https://img.shields.io/github/last-commit/aka-0x4C3DD/aicte25-ibmSB-b4.svg)]()
[![Issues](https://img.shields.io/github/issues/aka-0x4C3DD/aicte25-ibmSB-b4.svg)]()

<p align="center">
A user-friendly Python application for hiding secret messages within images using steganography techniques with optional password protection.
</p>

</div>

## ⭐ Features

- Graphical User Interface (GUI) built with Tkinter
- Hide text messages in PNG/JPG/JPEG images
- Password protection for encrypted messages
- Automatic dependency management
- LSB (Least Significant Bit) steganography implementation
- Support for encoding and decoding hidden messages

## 🚀 Prerequisites

The application automatically checks and installs required dependencies:
- Python 3.x
- OpenCV (`opencv-python`)
- NumPy
- Tkinter (comes with Python)

## 💻 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/aicte25-ibmSB-b4.git
cd aicte25-ibmSB-b4
```

2. Run the application:
```bash
python bin/steganography.py
```

## 🎯 Usage

1. **Encoding a message:**
   - Click "Browse" to select an input image
   - Select an output location for the encoded image
   - Enter your secret message in the text box
   - (Optional) Enter a password for encryption
   - Click "Encode" to hide the message

2. **Decoding a message:**
   - Click "Browse" to select an encoded image
   - Enter the password if the message was encrypted
   - Click "Decode" to reveal the hidden message

<!-- ## 🎥 Demonstration

<p align="center">
<img src="demo.gif" alt="Steganography Demo" width="800"/>
</p>

The above demonstration shows:
- Selecting an input image
- Entering a secret message
- Password protection
- Encoding process
- Decoding the hidden message

-->

## 🔧 Technical Implementation

- **Steganography Method:** Uses LSB (Least Significant Bit) technique for message embedding
- **Encryption:** XOR-based encryption for password-protected messages
- **Message Delimiter:** Uses "=====" to identify message boundaries
- **Image Format:** Supports PNG output for lossless image encoding
- **Dependencies:** Auto-installation of required Python packages

## ⚠️ Limitations

- Output images should be saved in PNG format to prevent data loss
- Image must have sufficient pixels to store the message
- Original image quality is preserved with minimal visual changes

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Suman Garai**
- Project developed as part of AICTE 2025 IBM Skillbuild Program

## 🙏 Acknowledgments

- AICTE for the project opportunity
- IBM Skillbuild Program
- OpenCV and NumPy communities
