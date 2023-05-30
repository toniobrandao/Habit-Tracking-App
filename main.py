import requests
from datetime import datetime, timedelta
from ui import HabitTrackingApp

#https://pixe.la/v1/users/toniobrandao/graphs/graph1.html

# Get current date and time.
current_date = datetime.now()

#Iniciando o aplicativo.
app = HabitTrackingApp(current_date)


#Criando o usuário
#pixela_endpoint = "https://pixe.la/v1/users"
#USERNAME = "toniobrandao"
#TOKEN = "akokf3020d"
#GRAPH_ID = "graph1"
#user_params = {"token":TOKEN,
#               "username":USERNAME,
#               "agreeTermsOfService":"yes",
#               "notMinor":"yes"
#}
#response = requests.post(url=pixela_endpoint, json = user_params)