index.py

from browser import document
from browser import html
nav = html.DIV('Python', Class="nav")
cnt = html.DIV('You can do really awesome stuff using a nice slack!', Class="content")
ftr = html.DIV('Made with luv by: Cabral', Class="footer")
document <= [nav, cnt, ftr]
