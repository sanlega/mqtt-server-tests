# MQTT Data Logger with MySQL and Docker
## Description

This project sets up an MQTT broker using Eclipse Mosquitto and logs MQTT messages into a MySQL database. All services are containerized with Docker for easy setup and distribution.
## Installation
### Prerequisites
- Docker and Docker Compose installed
- Python 3.x
### Steps
1. Clone the repository.

```bash
git clone https://github.com/sanlega/mqtt-server-tests
```


1. Change into the project directory.

```bash
cd mqtt-server-tests
```


1. Start the Docker containers.

```bash
docker-compose up -d
```


1. Run the Python script to create the MySQL table.

```bash
python create_table.py
```


## Usage

To start the MQTT Data Logger:

```bash
python mqtt_data_logger.py
```


Once the MQTT broker is running, you can publish messages to the topic `test/#` (or any topic you've configured). The messages will be logged into the MySQL database.
## Project Structure 
- `mqtt_data_logger.py`: Main script that subscribes to MQTT topics and logs messages into MySQL. 
- `create_table.py`: Python script to create the MySQL table if it doesn't exist. 
- `docker-compose.yml`: Docker Compose file to set up Mosquitto and MySQL. 
- `mosquitto.conf`: Configuration file for the Mosquitto MQTT broker.
## Contributing

This is a work-in-progress, and contributions are welcome. Please open an issue or submit a pull request.
## License

This project is open source, under the [MIT License](https://chat.openai.com/c/LICENSE) .---

You can update the repository URL and other project-specific information. Once done, you can push this README.md file to your GitHub repository.
