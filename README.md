# FC51-MQTT-SERVER

# Detection System Server & Visualization

## Prerequisites

### 1. Python Installation
Ensure Python is installed on your system.

#### Windows:
- Download the installer from [python.org](https://python.org).
- Follow the installation steps.

#### Mac:
- Run the command:
  ```bash
  brew install python3

#### Linux:
- Run the command:
    ```bash
    sudo apt install python3 python3-pip

### 2. Mosquitto Broker Setup
#### Windows:

Download Mosquitto from mosquitto.org.
During installation, enable the "Install as Service" option.
Edit the configuration file located at: C:\Program Files\mosquitto\mosquitto.conf:

listener 1883
allow_anonymous true
Start the Mosquitto service:

bash: net start mosquitto

#### Mac:
Install Mosquitto using Homebrew:
bash: brew install mosquitto

Configure Mosquitto:
bash: echo "listener 1883\nallow_anonymous true" > /opt/homebrew/etc/mosquitto/mosquitto.conf

Start the Mosquitto service:
bash: brew services start mosquitto

#### Linux:
Install Mosquitto:
bash: sudo apt install mosquitto

Configure Mosquitto:
bash: echo "listener 1883\nallow_anonymous true" | sudo tee /etc/mosquitto/mosquitto.conf

Start the Mosquitto service:
bash: sudo systemctl start mosquitto

### 3. Python Requirements
Install the required Python packages:

bash: pip install paho-mqtt streamlit plotly pandas

Running the System
Start the Mosquitto broker:

Ensure Mosquitto is running on your machine.
Run the MQTT Subscriber:

python subscriber.py

Run the Visualization App:

streamlit run data_viz.py