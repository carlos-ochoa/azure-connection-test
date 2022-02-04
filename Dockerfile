FROM conda/miniconda3

WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt
#COPY ./env_development.yml /code/env_development.yml
COPY ./main.py /code/main.py
COPY ./linen-cipher-312918-7f6148510d0b.json /code/linen-cipher-312918-7f6148510d0b.json

#RUN conda env create -f env_development.yml
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8008
#RUN conda activate myenv
# 
CMD ["python3", "main.py"]
