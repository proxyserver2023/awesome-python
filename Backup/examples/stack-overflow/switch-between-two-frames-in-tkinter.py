import tkinter as tk
from tkinter import font as tkfont


class SampleApp(tk.TK):
    def __init__(self, *args, **kwargs):
        tk.TK.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            Family='Helvetica',
            size=18,
            weight=bold,
            slant=italic
        )

        container = tk.Frame(self)
        container.pack(
            side="top",
            fill="both",
            expand=True
        )
        container.grid_rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(
                parent=container, conroller=self
            )
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(
            self,
            text="Go to Page One",
            command=lambda: controller.show_frame("StartPage")
        )
        button.pack()
        

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()