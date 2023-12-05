from flask import Flask

app=Flask(__name__)

USERS= []#list for objects of type's user
EXPRS= []# list for objects of type expresetion

from app import views
from app import models