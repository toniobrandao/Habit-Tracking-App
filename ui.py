from tkinter import *
import requests
# ---------------------------- CONSTANTS ------------------------------- #
USERNAME = "toniobrandao"
TOKEN = "akokf3020d"
GRAPH_ID = "graph1"
THEME_COLOR = "#375362"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
HEADERS = headers = {"X-USER-TOKEN":TOKEN}
# ---------------------------- CONSTANTS ------------------------------- #

from datetime import datetime
class HabitTrackingApp:
    def __init__(self,date: datetime):
        self.date = date
        self.date_formatted = self.date.strftime('%Y%m%d')
        self.window = Tk()
        self.window.title("Hábito leitura Livros")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=100, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            50,
            width=280,
            text="Quantas páginas você leu hoje?",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.date_label = Label(text= self.date.strftime("%d/%m/%Y") , fg="White", bg=THEME_COLOR,font=("Arial", 12, "bold"),anchor="center")
        self.date_label.grid(row=0, column=0)
        # Buttons
        #true_img = PhotoImage(file="images/true.png")
        correct_btn = Button(text = "Atualizar",highlightthickness=0, command=self.atualiza_paginas)
        correct_btn.grid(row=2, column=1)

        #Entry
        self.entry = Entry(width=30)
        self.insere_no_entry_as_paginas_lidas()
        self.entry.grid(row=2, column=0)

        self.window.mainloop()
    def atualiza_paginas(self):
        if self.entry.get() == 0:
            self.add_data()
        else:
            self.update_data()


    def add_data(self):
       incrementing_graph_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}'

       graph_increment = {"date":self.date_formatted,
       "quantity":str(self.entry.get())}
       response = requests.post(url=incrementing_graph_endpoint,json=graph_increment, headers = headers)

       print(response.text)
    def update_data(self):
        updating_graph_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{self.date_formatted}'

        graph_update = {
            "quantity": str(self.entry.get())}
        response = requests.put(url=updating_graph_endpoint, json=graph_update, headers=headers)

    def insere_no_entry_as_paginas_lidas(self):
        # Vendo detalhes do gráfico

        graph_details_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{self.date_formatted}"

        print(graph_details_endpoint)

        response = requests.get(url=graph_details_endpoint, headers=HEADERS)
        mensagem = response.json()

        if 'quantity' in mensagem:
            quantity = int(mensagem['quantity'])
        else:
            quantity = 0
        self.entry.insert(END, string=str(quantity))