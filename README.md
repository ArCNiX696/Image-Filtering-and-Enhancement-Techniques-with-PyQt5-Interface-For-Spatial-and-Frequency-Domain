Image Filtering and Enhancement Techniques with PyQt5 Interface: From Spatial to Frequency Domain 📸

Welcome to the Image Filtering and Enhancement Techniques repository! This project explores various image processing filters, implemented from scratch, to enhance image quality by reducing noise and highlighting edges. The techniques include average and median filters, Sobel operator, Gaussian filter, and Fourier-based filters applied in both spatial and frequency domains, all integrated into a user-friendly PyQt5 interface.

📚 Project Overview
This repository delves into the intricacies of image enhancement through various filtering techniques aimed at noise reduction and edge enhancement. The implemented filters include:

>User Interface
![image](https://github.com/ArCNiX696/Image-Filtering-and-Enhancement-Techniques-with-PyQt5-Interface-For-Spatial-and-Frequency-Domain/assets/134034570/922982b2-a06f-4f69-9a4f-73eb630f0fd8)

Average Filter: Smooths the image by averaging pixel values within a neighborhood.
Median Filter: Reduces noise by replacing pixel values with the median of neighboring values.
Sobel Operator: Enhances edges by emphasizing intensity transitions.
Gaussian Filter: Applies a Gaussian blur to reduce noise while preserving details.
Low-Pass and High-Pass Filters: Utilized in the frequency domain to selectively amplify or attenuate spatial frequencies.
All these filters are accessible through a user-friendly graphical interface created with PyQt5, making it easy to apply and compare different techniques.

🚀 Getting Started
To get started with this project, follow these steps:

Clone the Repository:

git clone https://github.com/ArCNiX696/Image-Filtering-and-Enhancement-Techniques-with-PyQt5-Interface-For-Spatial-and-Frequency-Domain.git

Install Dependencies:
Ensure you have the necessary libraries installed to run the project. Use the following command to install the required Python packages:

Run the Application:
Execute the main script to launch the PyQt5 interface and start applying the various filters:
main.py

🛠️ Required Software and Versions
Python: 3.11.5
NumPy: (for array and matrix operations)
Matplotlib: (for plotting and visualization)
SciPy: (for scientific computing and image processing)
PyQt5: (for the graphical user interface)

📊 Performance Evaluation
Each filter has been tested on various images to evaluate its effectiveness in noise reduction and edge enhancement. Key observations include:

Average Filter: Effective in noise reduction but causes blurring.
Median Filter: Superior noise reduction while preserving details.
Sobel Operator: Excellent edge enhancement with different mask sizes.
Gaussian Filter: Versatile in smoothing, with sigma value controlling the extent of blur.
Fourier-Based Filters: Low-pass and high-pass filters effectively manage noise and edges in the frequency domain.

📁 Project Structure
main.py: Main script to run the various filters through the PyQt5 interface.
GaussianFil.py: Implementation of the Gaussian filter in the spatial domain.
GaussianFourier.py: Implementation of the Gaussian filter in the frequency domain.
Smooth_Filter.py: Implementation of smoothing filters.
Sharp.py: Implementation of sharpening filters.
Report.pdf: Detailed report on the filtering techniques and their testing results.

📈 Results and Discussion
The results from applying these filters demonstrate significant improvements in image quality. Each filter serves a specific purpose, from noise reduction to edge enhancement, showcasing their unique strengths and applications. The PyQt5 interface allows for an intuitive comparison and application of these techniques.

Happy learning and exploring! 😊📊💡
