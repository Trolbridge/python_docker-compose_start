FROM python:3.10-slim

# set the working directory
# WORKDIR /code

# install dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the src to the folder

# COPY ./src ./src

# start the server
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
# CMD ["mypy", "src/main.py", "python3", "src/main.py"]
# CMD ["mypy", "src/main.py"]
# CMD ["/bin/bash", "-c", "mypy src/main.py;python3 src/main.py" ]
CMD ["/bin/bash", "-c", "mypy main.py;python3 main.py" ]
# CMD ["/bin/bash", "-c", "ls" ]