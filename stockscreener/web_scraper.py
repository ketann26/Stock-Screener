import numpy as np
import pandas as pd

import requests
import bs4
from bs4 import BeautifulSoup

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer

from fastnumbers import isfloat
from fastnumbers import fast_float
from multiprocessing.dummy import Pool as ThreadPool

import matplotlib.pyplot as plt
import seaborn as sns
import json
from tidylib import tidy_document

sns.set_style('whitegrid')
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
Base = declarative_base()



class Stock(Base):

    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)

engine = create_engine('sqlite:///stock_database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def ffloat(string):
    if string is None:
        return np.nan
    if type(string)==float or type(string)==np.float64:
        return string
    if type(string)==int or type(string)==np.int64:
        return string
    return fast_float(string.split(" ")[0].replace(',','').replace('%',''),
                      default=np.nan)

def ffloat_list(string_list):
    return list(map(ffloat,string_list))

def get_stock_data(url):

    response = requests.get(url, timeout=240)
    content = BeautifulSoup(response.content, "html.parser")

    name = content.find("div", attrs={"id":'stockName'}).h1.text.strip()
    price = ffloat(content.find("div", attrs={"id": 'nsecp'})['rel'])

    stock = Stock(name=name, price=price)
    session.add(stock)
    session.commit()

if __name__ == '__main__':

    url = 'https://www.moneycontrol.com/india/stockpricequote/auto-2-3-wheelers/heromotocorp/HHM'
    get_stock_data(url)

