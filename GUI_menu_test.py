import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        fileItem2 = fileMenu.Append(wx.ID_NEW, 'New', 'New Application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)
        self.Bind(wx.EVT_MENU, self.OnNew, fileItem2)

        self.SetSize((300, 200))
        self.SetTitle('GUI_menu')
        self.Centre()

    def OnQuit(self, e):
        self.Close()

    def OnNew(self, e):
        new = wx.App()
        ex2 = Example(None)
        ex2.Show()
        new.MainLoop()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()