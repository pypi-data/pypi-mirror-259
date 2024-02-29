Get-ChildItem -Path $PSScriptRoot\dist -Include * -File -Recurse | foreach { $_.Delete() }

py -m build $PSScriptRoot
pip install $PSScriptRoot\dist\pylualinker-0.0.4-py3-none-any.whl --force-reinstall
PyLuaLinker