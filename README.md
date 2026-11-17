# advanced-programming-python
Python projects from my Advanced Programming course: MP1-MP3 and one assignment

Python File I/O, Data Processing & Tkinter Basics (Assignment-1.py)

What the Project Does: This collection of scripts tackles ten foundational Python exercises split into file/data manipulation and basic GUI programming. It parses university course records from JSON, analyzes student demographics and GPAs from Excel, searches directories recursively, reverses text files, and calculates character frequencies, alongside building interactive Tkinter widgets.
Technologies: Python 3, json, os, openpyxl (for Excel spreadsheets), and tkinter (for desktop GUI windows and widgets).
Main Features: Automated JSON/Excel aggregation, recursive .py file discovery, defensive try-except blocks for division and missing files, and event-driven GUI apps featuring checkbuttons, dynamic text entries, and single-select listboxes.
How to Run It: Install the required Excel library via pip install openpyxl. Ensure sample input files (university_data.json, school_data.xlsx, abc.txt, words.txt) exist in your working directory, then run python Assignment-1.py in your terminal (note: GUI windows will open sequentially as you close each one).
What I Learned: I learned how to extract and transform structured data across JSON, Excel, and plain-text formats while implementing robust exception handling (ValueError, ZeroDivisionError, FileNotFoundError) and binding user events to Tkinter widgets.


Healthy Lifestyle Planner (MiniProject-1.py)

What the Project Does: The Healthy Lifestyle Planner is an interactive desktop application designed to help users organize weekly routines across three categories: Sports, Food Plans, and Activities. Users can load options from an external spreadsheet, curate up to seven items per category, or generate a balanced weekly schedule automatically.
Technologies: Python 3, tkinter and tkinter.ttk (for GUI layout, listboxes, and comboboxes), openpyxl (for reading and writing .xlsx files), json, and random.
Main Features: Excel file importing via file dialogs, dual-listbox item management with a 7-item cap per category, one-click randomization using random.sample(), live text previewing, and multi-format exporting (.txt, .json, and .xlsx) labeled by week number.
How to Run It: Install openpyxl using pip install openpyxl. Launch the app with python MiniProject-1.py, click Import excel file to load a spreadsheet with Sports, Food Plans, and Activities columns, select or randomize your weekly items, enter a week number, and click Export.
What I Learned: Through this project, I gained hands-on experience structuring an object-oriented Tkinter GUI (Frame subclassing), managing state synchronization across multiple UI widgets, and handling multi-format file exports cleanly.



Two-Player Go Fish Card Game (MiniProject-2.py)

What the Project Does: This project is a digital, two-player implementation of the classic card game Go Fish built with an interactive graphical interface. Players take turns requesting card ranks from their opponent to form matching pairs, drawing from a shuffled 52-card deck ("going fish") when the opponent lacks the requested rank.
Technologies: Python 3, tkinter (for dynamic button rendering, frames, dropdown menus, and message boxes), and random (for deck shuffling).
Main Features: Object-oriented Card, Player, and Go_Fish classes, turn-based card masking (🂠) to hide the opponent's hand, automatic pair detection and scoring, a temporary 3-second "Show Opponent's Card" peek feature, and automated end-of-game winner announcements.
How to Run It: No external third-party packages are required since tkinter and random are part of Python's standard library. Simply execute python MiniProject-2.py in your terminal, select a rank from your hand or the dropdown menu, and click Ask to play.
What I Learned: Building this game taught me how to model game rules and turn-based state machines using OOP, dynamically rebuild Tkinter frames on every turn, and schedule non-blocking UI updates using root.after().




Visual Data Explorer (MiniProject-3.py)

What the Project Does: The Visual Data Explorer is a desktop data-analysis and visualization tool that allows users to load any CSV dataset, inspect summary statistics, filter numeric ranges, and generate interactive statistical plots. It streamlines exploratory data analysis without requiring users to write code.
Technologies: Python 3, pandas and numpy (for data manipulation and correlation matrices), matplotlib (with FigureCanvasTkAgg for embedding plots), and tkinter / ttk (for the desktop interface).
Main Features: Dynamic CSV uploading, live .describe() statistical summaries per column, min/max numeric range filtering, embedded popup windows for Histograms, Line Plots, Scatter Plots, Pie Charts, and Correlation Heatmaps, plus a Save Last Plot feature to export charts as .png images.
How to Run It: Install the required data libraries via pip install pandas numpy matplotlib. Run python MiniProject-3.py, click Upload CSV to select your dataset, filter or pick columns from the dropdowns, and click any chart button to visualize your data.
What I Learned: I learned how to bridge data science libraries (pandas and matplotlib) with a desktop GUI using FigureCanvasTkAgg, filter DataFrames dynamically from user inputs, and manage multi-window Tkinter applications (Toplevel).
