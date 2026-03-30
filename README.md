SECOND UPDATE, VERSION 1.1.0

I added the tkinter function askopenfilenames() which allows you to select the file directly via a GUI, removing the need to write the path manually and raising
the possibility of writing syntax errors.

If the file selected is not found (For an unknown reason) an exception is raised, FileNotFoundError, which recalls the function, allowing you to select a valid file.

The user experience is now flexible and faster, allowing to select directly the file (<5 seconds), instead of writing the file path manually (>10seconds)
