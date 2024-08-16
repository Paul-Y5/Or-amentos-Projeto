from tkinter import *
import customtkinter

# Tema, fonte e tamanho
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Criação da janela
root = customtkinter.CTk()

root.title('Expense Mananger')
root.geometry('800x600')
root.resizable(True, True)

