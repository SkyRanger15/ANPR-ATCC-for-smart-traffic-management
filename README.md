# ANPR and ATCC for Smart Traffic Management

## Project Overview
The objective of this project is to implement a smart traffic control system using Automatic Number Plate Recognition (ANPR) and Automatic Traffic Classification and Control (ATCC). Leveraging Deep Learning, Computer Vision and Object Detection, this system enables automated traffic surveillance and management in urban environments.

### Key Features
- Recognition of vehicle number plates (ANPR) -
- Traffic classification and control automation (ATCC) -
- Data interpolation for precise tracking -
- Visualization tools

### Results
- you can file the result video at this location : [output video](https://drive.google.com/file/d/1VcIJV9AeiGbdGsQ7CrSDSOdqNZiCpz17/view?usp=sharing)

##  Workflow
1. Execute `main.py` to perform initial vehicle detection and generate CSV file in `output/` directory
2. Run `add_missing_data.py` to perform data interpolation and generate enhanced CSV file in `output/` directory
3. Run `visualize.py` to create visualization video using interpolated data, saved in `output_videos/` directory

## Setup and Installation
1. Clone the repository:
```bash
git clone https://github.com/SkyRanger15/ANPR-ATCC-for-smart-traffic-management.git
cd anpr-atcc-traffic-management
```

2. Create and activate virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Project


1. Replace the path to your input video and your desired output directory.

2. Run the main detection:
```bash
python main.py
```

3. Perform data interpolation:
```bash
python add_missing_data.py
```

4. Generate visualization:
```bash
python visualize.py
```

## License
ANPR and ATCC for Smart Traffic Management is released under the [MIT License](LICENSE), allowing you to freely use, modify, and distribute the project.
