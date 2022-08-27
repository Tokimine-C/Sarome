import PySimpleGUI as sg

class LoginPageField:

    sg.theme('Default1')

    col1 = [[sg.Text('Yahoo! ID',size = (10,1)),sg.InputText(key='-id-')]]

    col2 = [[sg.Text('パスワード',size = (10,1)),sg.InputText(key='-pass-')]]

    col3 = [[sg.Button('ログイン', key = '-login-')]]



    layout = [
        [sg.Column(col1, justification='c',pad = ((0,0),(100,0)))],
        [sg.Column(col2, justification='c')],
        [sg.Column(col3, justification='r',pad = ((0,0),(20,0)))]
    ]

    window = sg.Window('ログイン', layout,size = (520,340))


    def openPage(self):

        """
        ログインページを開く

        Returns
        -------
        goNext : boolean
            次のページに進むか

        """

        goNext = True
        
        
        while True:

            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                print('Window closed.')
                break
            
            if event == '-login-':
                print(values['-id-'])
                print(values['-pass-'])
                break

        self.window.close()

        return goNext