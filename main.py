#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import pandas as pd
import openpyxl
import PySimpleGUI as sg

class Gui_Controller(object):
    def open(self):

        default_path = os.environ["USERPROFILE"] + "\Desktop"

        sg.theme('DarkAmber')
        
        layout = [
            [sg.Text(
                    "pandas version is " + pd.__version__
                    + " / PySimpleGUI version is " + sg.__version__
                )
            ],
            [sg.Text("openpyxl version is " + openpyxl.__version__)],
            [sg.Text("")],
            [sg.Text('Select export path (sample excel)')],
            [sg.InputText(default_text=default_path)],
            [sg.OK(), sg.Cancel()]
        ]

        # Create the Window
        window = sg.Window('pandas with Nuitka GUI App PoC', layout)
        
        while True:             
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancel'):
                break

        window.close()

if __name__ == "__main__":
    gc = Gui_Controller()
    gc.open()