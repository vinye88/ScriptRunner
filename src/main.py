import wx

def main():
    app = wx.App()
    w = wx.Frame(None)
    w.SetTitle('Script Runner')
    w.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()