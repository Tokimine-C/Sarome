from LoginPageField import LoginPageField
from TrunkField import TrunkField

goNext = LoginPageField().openPage()

if goNext:
    TrunkField().openPage()

else:
    print("end")
