# 🚗 ANPR and ATCC for Smart Traffic Management

## 🎯 Project Overview
This project implements an intelligent traffic management system utilizing Automatic Number Plate Recognition (ANPR) and Automatic Traffic Classification and Control (ATCC). By leveraging Deep Learning and Object Detection techniques, the system automates traffic monitoring and control in smart city environments.

### Key Features
- 📝 Automatic Number Plate Recognition (ANPR)
- 🚦 Automatic Traffic Classification and Control (ATCC)
- 📊 Data interpolation for accurate tracking
- 📈 Visualization capabilities

### Results
- you can file the result video at this location : "Provide the link of the output video."

## 🚀 Workflow
1. Execute `main.py` to perform initial vehicle detection and generate CSV file in `output/` directory
2. Run `add_missing_data.py` to perform data interpolation and generate enhanced CSV file in `output/` directory
3. Run `visualize.py` to create visualization video using interpolated data, saved in `output_videos/` directory

## 🛠️ Setup and Installation
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

## 🏃‍♂️ Running the Project


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

## 📄 License
ANPR and ATCC for Smart Traffic Management is released under the [MIT License](LICENSE), allowing you to freely use, modify, and distribute the project.
