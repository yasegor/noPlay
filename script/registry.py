import winreg

path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer'


def change_value(value):
    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey:
        with winreg.OpenKey(hkey, path, 0, winreg.KEY_ALL_ACCESS) as sub_key:
            winreg.SetValueEx(sub_key, 'DisallowRun', 0, winreg.REG_DWORD, value)


def show_value():
    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey:
        with winreg.OpenKey(hkey, path, 0, winreg.KEY_ALL_ACCESS) as sub_key:
            value = winreg.EnumValue(sub_key, 0)[1]
            return value
