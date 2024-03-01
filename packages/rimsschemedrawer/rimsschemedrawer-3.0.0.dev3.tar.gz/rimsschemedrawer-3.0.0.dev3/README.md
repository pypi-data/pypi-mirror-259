# RIMSSchemeDrawer

A drawing program to create publishable RIMS schemes.  

Help with the installation / compilation can be found [here](INSTALLATION.md).


## How to use

Generally, the GUI should be fairly self-explanatory.
Tool tips are furthermore implemented to help you navigate what you need to do.

Below is a screenshot of the main window in the software
that is configured to mostly reproduce 
the Titanium resonance ionization scheme published by 
[Trappitsch et al. (2018)](https://doi.org/10.1039/C8JA00269J). 

![Example Ti](examples/screenshot_titanium.png)

### State / transition information

Information on the transitions are entered on the left hand side of the software.
You can select if you would like to enter the information in nm (wavelength)
or in cm<sup>-1</sup> (wavenumbers). 
The term symbols can also be given, but are optional. 
Furthermore, if you have low-lying states, 
check the according box, 
and you can now add the associated information.
If a transition is forbidden,
check the box and it will either be crossed out,
or not shown (depending on the configuration selected).

### Plotting

On the right hand side of the program are the settings.
Many parameters of the plot can be configured here. 
It is worth playing with various parameters. 
The `Plot` button will quickly allow you to see the figure in a new window. 
It will also allow you to save the figure (see toolbar).
Available formats can be found
[here](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html).

In the background, RIMSSchemeDrawer uses matplotlib to draw the figures
and to display them nicely. 
Feel free to tinker with the code and explore additional styles.

### Loading and saving configurations

If you want to load / save the configurations
you can use the according `Load Config` and `Save Config` buttons. 
The data is saved as a `json` file. 
You can open a saved file with any text editor and have a look, 
but please note that bad things can happen 
if you change the file right there, 
unless of course you know what you're doing. 
The file should be fairly self-explanatory. 

If you are interested: 
The file with the configurations shown in the image above can be found [here](examples/example_titanium.json).


## Issues/enhancements

If you find bugs in the software or would like to have an additional feature, 
please raise an Issue [here](https://github.com/RIMS-Code/RIMSSchemeDrawer/issues).
Please also browse the issues to first see if the bug/feature request 
you want to report is already listed. 

If you furthermore have ideas on how to implement/fix the bug already, 
please feel free to discuss it through in the Issues tab 
and create a pull request. 
Contributions are always welcome!
Please follow [best practices](https://chris.beams.io/posts/git-commit/) in your commit messages.


## License

RIMSSchemeDrawer is Copyright (C) 2020-2024 Reto Trappitsch  
It is licensed under the MIT license.
