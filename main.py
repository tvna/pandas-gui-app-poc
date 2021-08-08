#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import subprocess

import pandas as pd
import openpyxl
import PySimpleGUI as sg

class GUI_Controller(object):
    def __init__(self) -> None:
        self._license_info = None

    def _get_licenses(self):
        if self._license_info is None:
            json_licenses = json.loads(
                subprocess.check_output(
                    "pip-licenses --with-license-file --no-license-path --format=json"
                )
            )

            double_break = chr(10) * 2
            self._license_info = double_break.join([
                text["Name"] + " (" + text["Version"] + ")" + chr(10) + text["LicenseText"] for text in json_licenses
            ])

    def open(self):

        default_path = os.environ["USERPROFILE"] + "\Desktop"

        sg.theme('DarkAmber')
        
        menu_def = [    
            [
                "Docs", 
                [
                    "Open pandas docs (Original)", 
                    "Open pandas docs (Japanese translated)", 
                    "Open openpyxl docs", 
                    "Open PySimpleGUI docs (Original)", 
                    "Open PySimpleGUI docs (Japanese translated)", 
                    "Open nuitka docs",
                ]
            ],     
            [
                "About", 
                [
                    "Show licenses", 
                ]
            ],
        ]
        
        layout = [
            [sg.Menu(menu_def, )],      
            [sg.Text(
                    "pandas version is " + pd.__version__
                    + " / PySimpleGUI version is " + sg.__version__
                )
            ],
            [sg.Text("openpyxl version is " + openpyxl.__version__)],
            [sg.Text("")],
            [sg.Text('Select export path (sample excel)')],
            [sg.InputText(default_text=default_path)],
            [sg.OK(), sg.Cancel()],
        ]

        # Create the Window
        window = sg.Window('pandas with Nuitka GUI App PoC', layout)
        
        while True:             
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Cancel'):
                break

            if event == "Show licenses":
                self._get_licenses()
                sg.popup_scrolled(
                    self._license_info, 
                    title="Licenses", 
                    keep_on_top=True,
                    size=(80, 20),
                )

            if event == "Open pandas documents (Original)":
                os.system("start https://pandas.pydata.org/docs/")

            if event == "Open pandas documents (Japanese translated)":
                os.system("start https://note.nkmk.me/pandas/")
            
            if event == "Open openpyxl documents":
                os.system("start https://openpyxl.readthedocs.io/en/stable/index.html")
            
            if event == "Open PySimpleGUI documents (Original)":
                os.system("start https://pysimplegui.readthedocs.io/en/latest/call%20reference/")

            if event == "Open PySimpleGUI documents (Japanese translated)":
                os.system("start http://www.k-techlabo.org/www_python/PySimpleGUI.pdf")

            if event == "Open nuitka documents":
                os.system("start https://nuitka.net/pages/documentation.html")

        window.close()

if __name__ == "__main__":
    gc = GUI_Controller()
    gc.open()