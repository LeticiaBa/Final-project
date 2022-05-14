from gui import *


def main():

    window = Tk()
    window.title('Calulation')
    window.geometry('300x300')
    widgets = GUI(window)
    window.mainloop()
    window.resizable(False, False)


if __name__ == '__main__':
    main()
