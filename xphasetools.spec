# -*- mode: python ; coding: utf-8 -*-

import platform
import os

TURBOJPEG_DLLS = {'Windows' : os.path.join('pyinstaller_deps', 'libturbojpeg.dll'),
                    'Linux' : os.path.join('pyinstaller_deps', 'libturbojpeg.so')}
cnvdng_a = Analysis(
    ['cnv_jpeg_to_dng.py'],
    pathex=[],
    binaries=[(TURBOJPEG_DLLS[platform.system()], 'turbojpeg.libs')],
    datas=[],
    hiddenimports=[],
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
cnvdng_pyz = PYZ(cnvdng_a.pure)

cnvdng_exe = EXE(
    cnvdng_pyz,
    cnvdng_a.scripts,
    [],
    exclude_binaries=True,
    name='cnv_jpeg_to_dng',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)


cnvtif_a = Analysis(
    ['cnv_jpeg_to_tiff.py'],
    pathex=[],
    binaries=[(TURBOJPEG_DLLS[platform.system()], 'turbojpeg.libs')],
    datas=[],
    hiddenimports=[],
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
cnvtif_pyz = PYZ(cnvtif_a.pure)

cnvtif_exe = EXE(
    cnvtif_pyz,
    cnvtif_a.scripts,
    [],
    exclude_binaries=True,
    name='cnv_jpeg_to_tiff',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)


packori_a = Analysis(
    ['packori.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
packori_pyz = PYZ(packori_a.pure)

packori_exe = EXE(
    packori_pyz,
    packori_a.scripts,
    [],
    exclude_binaries=True,
    name='packori',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)


unpackori_a = Analysis(
    ['unpackori.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
unpackori_pyz = PYZ(unpackori_a.pure)

unpackori_exe = EXE(
    unpackori_pyz,
    unpackori_a.scripts,
    [],
    exclude_binaries=True,
    name='unpackori',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    unpackori_exe,
    unpackori_a.binaries,
    unpackori_a.datas,
    packori_exe,
    packori_a.binaries,
    packori_a.datas,
    cnvdng_exe,
    cnvdng_a.binaries,
    cnvdng_a.datas,
    cnvtif_exe,
    cnvtif_a.binaries,
    cnvtif_a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='xphasetools',
)
