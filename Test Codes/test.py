# import required libraries
import requests
import time
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

# create an object to ToastNotifier class
n = ToastNotifier()

for r in range(5):
    n.show_toast("You're Dumb", duration = 1)
    time.sleep(0.25)
    