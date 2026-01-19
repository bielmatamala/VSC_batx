# SmartGallery - Technical Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Installation & Setup](#installation--setup)
4. [Core Components](#core-components)
5. [Workflow](#workflow)
6. [Configuration](#configuration)
7. [Troubleshooting](#troubleshooting)
8. [Performance Considerations](#performance-considerations)
9. [Future Enhancements](#future-enhancements)

## Project Overview
SmartGallery is an intelligent image processing and organization system that automatically classifies, rates, and organizes digital photographs. It leverages machine learning for image classification and quality assessment, with robust file handling capabilities.

## System Architecture

### High-Level Components
1. **Main Application (app.py)**
   - Orchestrates the image processing pipeline
   - Manages workflow and error handling
   - Coordinates between different modules

2. **Image Processing Pipeline**
   - RAW to JPG conversion
   - Image classification
   - Quality analysis
   - Metadata handling

3. **Machine Learning Models**
   - MobileNetV2 for image classification
   - Custom trained models support
   - Quality assessment algorithms

## Installation & Setup

### Prerequisites
- Python 3.8+
- Required Python packages (from requirements.txt):
  ```
  tensorflow
  keras
  numpy
  Pillow
  opencv-python
  exifread
  pyexiv2
  ```

### Configuration
Edit `Utils/config.py` to set the following paths:
- `INPUT_FOLDER`: Source directory for raw images
- `OUTPUT_FOLDER`: Destination for processed images
- `TEMP_FOLDER`: Temporary directory for intermediate files

## Core Components

### 1. Image Classifier (`models/classifier.py`)
- Implements MobileNetV2 for image classification
- Supports custom trained models
- Handles image preprocessing and prediction
- Returns category and confidence score

### 2. Image Quality Analyzer (`models/image_quality.py`)
- Analyzes image sharpness
- Detects blur and noise levels
- Assesses exposure and contrast
- Returns quality metrics and suggestions

### 3. RAW Processor (`Utils/raw_handler.py`)
- Converts RAW images to JPG
- Manages temporary file storage
- Handles file system operations

### 4. Image Sorter (`Utils/sorter.py`)
- Organizes images into category-based directories
- Handles file naming conventions
- Manages output directory structure

### 5. Metadata Handler (`Utils/metadata_writer.py`)
- Writes EXIF and XMP metadata
- Handles sidecar file creation
- Preserves original metadata during processing

## Workflow

1. **Initialization**
   - Clean temporary and output directories
   - Initialize ML models and processors

2. **Image Processing**
   - Convert RAW files to JPG
   - Process each image through the classification pipeline
   - Analyze image quality
   - Apply metadata

3. **Organization**
   - Sort images into category-based directories
   - Create dated folders for output
   - Clean up temporary files

## Configuration

### Environment Variables
- `INPUT_FOLDER`: Source directory for images
- `OUTPUT_FOLDER`: Processed images destination
- `TEMP_FOLDER`: Temporary processing directory

### Model Configuration
- Default model path: `D:\visual situdio code general\SmartGallery\models\mobilenetv2_cifar10.h5`
- Custom models can be specified during initialization
- Supports both custom-trained and pre-trained models

## Troubleshooting

### Common Issues
1. **Missing Dependencies**
   - Ensure all required Python packages are installed
   - Check for version compatibility

2. **File Permission Errors**
   - Verify read/write permissions for all specified directories
   - Ensure sufficient disk space

3. **Model Loading Failures**
   - Verify model file exists at specified path
   - Check model compatibility with TensorFlow/Keras version

### Logging
- Detailed logs are stored in the `logs` directory
- Each session is timestamped for easy reference

## Performance Considerations

### Processing Time
- Image processing time varies by:
  - Image resolution
  - Hardware specifications
  - Model complexity

### Resource Usage
- High memory usage during batch processing
- GPU acceleration recommended for large datasets

## Future Enhancements

### Planned Features
1. **Distributed Processing**
   - Support for multi-node processing
   - Cloud deployment options

2. **Enhanced Classification**
   - Support for custom categories
   - Improved model accuracy

3. **User Interface**
   - Web-based interface
   - Real-time progress tracking

4. **Advanced Features**
   - Duplicate detection
   - Face recognition
   - Automatic tagging

## License
[Specify License]

## Contact
[Your Contact Information]
