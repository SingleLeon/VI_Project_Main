# -*- mode: python -*-

block_cipher = None


a = Analysis(['GUI_Main.py'],
             pathex=['C:\\Users\\Lu\\Downloads\\WinPython-64bit-3.5.3.1Qt5\\python-3.5.3.amd64\\Lib', 'C:\\Users\\Lu\\Downloads\\WinPython-64bit-3.5.3.1Qt5\\python-3.5.3.amd64\\Lib\\site-packages', '', 'C:\\Users\\Lu\\PycharmProjects\\VI_Project_Main'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='GUI_Main',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
