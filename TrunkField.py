import PySimpleGUI as sg

class TrunkField:

    sg.theme('Default1')

    # 商品取得タブのレイアウト
    productAcquisitionPage = [
        [sg.Text('ホームページ',size = (10,1)),sg.InputText(key='-page-')],
        [sg.Text('カテゴリー',size = (10,1)),sg.InputText(key='-category-')],
        [sg.Text('ディレクトリ',size = (10,1)),sg.InputText(key='-productDirectory-')],
        [sg.Column([[sg.Button('取得', key = '-get-',size = (6,2))]],justification='r')]
    ]

    # 出品タブのレイアウト
    displayPage = [
        [sg.Text('ディレクトリ',size = (10,1)),sg.InputText(key='-displayDirectory-')],
        [sg.Column([[sg.Button('商品詳細設定', key = '-productDetails-')]],justification='r')],
        [sg.Canvas(background_color = 'PaleTurquoise',size = (300,380),pad = ((20,50),(0,0))),sg.Canvas(background_color = 'PaleTurquoise',size = (430,380))],
       
        [sg.Column([[sg.Button('出品', key = '-display-',size = (6,2))]],justification='r')]
    ]

    # 設定タブのレイアウト
    settingPage = [
        [sg.Text('ブラウザ設定',size = (10,1)),sg.Combo([],readonly=True)],
        [sg.Text('バージョン',size = (10,1)),sg.Text('1.0')]
    ]

    tab1 = sg.Tab('商品取得', productAcquisitionPage)
    tab2 = sg.Tab('出品',displayPage)
    tab3 = sg.Tab('設定',settingPage)

    tabSummary = [
        [tab1, tab2, tab3]
    ]

    layout = [
        [sg.TabGroup(tabSummary,tab_location='lefttop',size = (940,530),selected_background_color = 'DeepSkyBlue')]
    ]

    window = sg.Window('メインページ', layout,size = (950,540))


    def openPage(self):

        while True:
            
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                print('Window closed.')
                break

        self.window.close()