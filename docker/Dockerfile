# Use the Apache Spark 3.1.2 image as a parent image
FROM apache/spark

# Recreate missing directory for APT
USER root
RUN mkdir -p /var/lib/apt/lists/partial

# Install system dependencies
RUN apt-get update && apt-get install -y default-jre wget

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Install Kafka
RUN wget -qO- https://packages.confluent.io/archive/6.2/confluent-community-6.2.0.tar.gz | tar xvz -C /opt && \
    ln -s /opt/confluent-6.2.0 /opt/kafka

# Install Apache Airflow
RUN pip install apache-airflow

# Set environment variables for Spark, Kafka, and Airflow
ENV SPARK_HOME /opt/spark
ENV KAFKA_HOME /opt/kafka
ENV AIRFLOW_HOME /app/airflow
ENV PATH $PATH:$SPARK_HOME/bin:$KAFKA_HOME/bin

# Copy your pipeline code into the container
COPY . /app
WORKDIR /app

# Expose necessary ports for Kafka, Spark, and Airflow
EXPOSE 9092 7077 8080

# Initialize the Airflow metadata database
RUN airflow db init

# Set the Airflow username and password
ARG AIRFLOW_USERNAME='airflow' 
ARG AIRFLOW_PASSWORD='airflow' 

# Replace the default Airflow username and password
RUN sed -i "s/^# default_ui_username = .*/default_ui_username = ${AIRFLOW_USERNAME}/" $AIRFLOW_HOME/airflow.cfg && \
    sed -i "s/^# default_ui_password = .*/default_ui_password = ${AIRFLOW_PASSWORD}/" $AIRFLOW_HOME/airflow.cfg

# Define default command to run Airflow
CMD ["airflow", "webserver"]
