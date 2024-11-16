### **README.md**

# Classify3D

## **Features**
- Upload multiple images.
- Process images using OpenDroneMap (ODM) via Docker.
- View and download processed results:
  - All results as a ZIP archive.
- Automatically clean up processed files after download.

---

## **Requirements**
- Python 3.9 or later.
- Flask and required Python packages (see `requirements.txt`).
- Docker and Docker Compose installed and configured.
- ODM Docker image available (e.g., `opendronemap/odm`).

---

## **Setup**

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd <repository-name>

### **2. Install Dependencies**
Install dependencies:
```bash
pip install -r requirements.txt
```

### **3. Configure the Application**
Ensure the `uploads` directory exists:
```bash
mkdir -p app/uploads
```

### **4. Build and Run the Application**
Run the included setup script:
```bash
./setup_and_run.sh
```

The script provides two options:
- **First-Time Setup**: Replaces paths in `odm_handler.py` and `docker-compose.yml` and builds the container.
- **Recurring Usage**: Skips path replacement and only rebuilds the container.

### **5. Access the Application**
Open your browser and go to:
```
http://localhost:5000
```

---

## **Usage**
1. **Upload Images**:
   - Navigate to `/upload` and select your images.

2. **Process Images**:
   - After uploading, the app processes the images using OpenDroneMap (ODM). Just wait for the page to load, and if you want to check the progress, open docker and go to the logs for the new ODM container made. Do not exit out of the page while it is running. Once ODM is done, you will automatically be taken to a results page.

3. **Results**:
   - Once you have been taken to the results page, just click on download as a zip, and just wait for it to download. This will effectively clear out the directory of the docker container so that you can run another task safely in the future, and also download all of the files including the pointcloud and textures.

---

## **File Structure**
```
.
├── app/
│   ├── static/
│   │   └── styles.css
│   ├── templates/
│   │   ├── index.html
│   │   ├── upload.html
│   │   ├── processing.html
│   │   └── results.html
│   ├── uploads/
│   ├── __init__.py
│   ├── routes.py
│   └── odm_handler.py
├── Dockerfile
├── docker-compose.yml
├── setup_and_run.sh
├── requirements.txt
└── README.md
```

---

## **Notes**
- Ensure Docker is running and configured properly.
- Adjust `MAX_CONTENT_LENGTH` in `__init__.py` for larger uploads.
- Use `FLASK_ENV=development` for debugging during development.

---

## **Troubleshooting**
- **Permission Errors**:
  - Ensure `uploads` directory has the correct permissions.

- **Docker Issues**:
  - Verify Docker is installed and running.
  - Confirm Docker Compose is configured.

- **ODM Errors**:
  - Check logs for specific errors during processing.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.
```

---
