FROM python:3.11

# Set the working directory in the container
#WORKDIR /fastapi-streamlit/car_evaluation_streamlit
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install streamlit --upgrade
COPY . .
EXPOSE 8501
ENTRYPOINT [ "streamlit", "run" ]
CMD [ "app.py", "--server.fileWatcherType", "none","--browser.gatherUsageStats", "false"]
#CMD [ "app.py", "--server.headless", "true", "--server.fileWatcherType", "none", "--browser.gatherUsageStats", "false"]