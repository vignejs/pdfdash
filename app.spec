# -*- mode: python -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['/mnt/c/Users/vigne/PycharmProjects/pdfdash'],
             binaries=[],
             datas=[('/home/vignesh/anaconda3/envs/pdfdash/lib/python3.6/site-packages/plotly/package_data/','./plotly/package_data/'),
                    ('/home/vignesh/anaconda3/envs/pdfdash/lib/python3.6/site-packages/dash_core_components/metadata.json','./dash_core_components/'),
                    ('/home/vignesh/anaconda3/envs/pdfdash/lib/python3.6/site-packages/dash_html_components/metadata.json','./dash_html_components/'),
                    ('/mnt/c/Users/vigne/PycharmProjects/pdfdash/assets','./assets')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='app')

