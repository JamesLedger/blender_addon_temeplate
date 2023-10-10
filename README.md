# Blender Addon template
A template Blender addon with basic examples of operators, UI Panels and testing.

# How to install manually
To manually install this addon you can zip it up and then go to 
Edit > Preferences > Install > Select the .zip


# How to develop with VSCode Extension
There's a really helpful vscode extension by JacquesLucke called blender-development that I've found really helpful in speeding up iterating. It runs Blender through vscode so that whenever you make a change to the code you can just reload in the vscode command pallete and have your changes instantly reflected in Blender without having to manually reinstall the addon.

Once the extension is installed you can open up the command pallete and enter:
> Blender: Build
> Choose a new Blender executable
> Naviate to C:\Program Files\Blender Foundation\Blender 3.1\blender.exe
> Blender: Build and start

Bear in mind because this creates a symlink and therefore doing this means that you won't be able to manually install the addon until deleting this link, normally found in the AppData > Blender Foundation folder

# How to run tests
You first need to install pytest and bpy, this version of bpy (3.6) is seperate to the main Blender version you may have installed

`pip install pytest bpy`

To install the project as a package for testing run
`pip install -e .`

To actually run the tests run
`pytest`
