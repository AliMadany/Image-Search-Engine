# Image Search Engine

## Overview
The Image Search Engine is a Python-based project that provides two distinct methods for searching images:
1. **Search by Color**: Finds images with a similar color distribution using color histograms and cosine similarity.
2. **Search by Image**: Identifies visually similar images using deep learning features extracted from a pre-trained ResNet50 model.

The project also includes a GUI application built with `customtkinter` to enable users to load images and visualize search results interactively.

---

## Features
- **Color-based Search**:
  - Uses OpenCV to compute color histograms for images.
  - Employs cosine similarity to rank images based on color similarity.
- **Content-based Search**:
  - Utilizes a pre-trained ResNet50 model from TensorFlow for feature extraction.
  - Leverages cosine similarity to find visually similar images.
- **GUI Interface**:
  - Provides an intuitive interface for loading images and displaying search results.
  - Displays similar images with thumbnails in a scrollable results pane.

---

## Installation
### Prerequisites
Ensure the following tools and libraries are installed:
- Python 3.7+
- TensorFlow
- OpenCV
- Numpy
- SciPy
- Matplotlib
- Scikit-learn
- CustomTkinter
- Pillow

### Setup
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the dataset (e.g., COCO dataset) and place it in the `data_dir` specified in the code.

---

## How It Works

### Search by Color
1. Extracts color histograms (RGB channels) for all dataset images.
2. Computes cosine similarity between the query image histogram and dataset histograms.
3. Returns top-k most similar images.

### Search by Image
1. Preprocesses the query image and dataset images to match ResNet50's input size.
2. Extracts deep features using ResNet50’s pooling layer.
3. Calculates cosine similarity between the query image features and dataset features.
4. Returns images exceeding the similarity threshold.

---

## Usage

### Running the GUI
1. Navigate to the project directory.
2. Run the GUI application:
   ```bash
   python gui_app.py
   ```
3. Use the "Load Image" button to upload an image.
4. Click "Search by Image" or "Search by Color" to retrieve results.

### Command-Line Usage
Both search methods can be executed via Python scripts:
- **Search by Color**:
  ```python
  from Color import main1
  
  results = main1("<input_image_path>")
  print(results)
  ```
- **Search by Image**:
  ```python
  from implementResults import main
  
  results = main("<input_image_path>")
  print(results)
  ```

---

## APIs and Tools Used
- **TensorFlow**: ResNet50 pre-trained model for feature extraction.
- **OpenCV**: Image processing and color histogram computation.
- **SciPy**: Cosine similarity calculations.
- **CustomTkinter**: GUI development.
- **Pillow**: Image loading and thumbnail creation.

---

## File Structure
```
├── Color.py                 # Color-based search implementation
├── implementResults.py      # Content-based search implementation
├── gui_app.py               # GUI application
├── dataset_features.npy     # Pre-computed features for dataset (optional)
├── dataset_filepaths.npy    # Dataset image paths (optional)
├── requirements.txt         # Required Python libraries
└── README.md                # Project documentation
```

---

## Future Enhancements
- Add support for more image similarity metrics.
- Implement real-time image search using live camera input.
- Integrate additional pre-trained models for diverse feature extraction.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- **COCO Dataset**: For providing a diverse set of test images.
- TensorFlow and OpenCV communities for their powerful tools and extensive documentation.

---

## Contributions
Feel free to fork this repository, create pull requests, or open issues for suggestions or bug reports.

