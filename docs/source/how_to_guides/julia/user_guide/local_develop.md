# Advanced Installation

If you want to delve deeper into the GENeSYS-MOD source code and functions, and might want to add or change things, or even [contribute](/get_involved), then another installation method might suit you more. Below is an outline of how to install GENeSYS-MOD.jl for development purposes:

## Installation

As with the [quick-start guide](/how_to_guides/julia/quick_start/quick-start), we advise you to use [Visual Studio Code](https://code.visualstudio.com/).

1.	Clone the GitHub repository for [GENeSYSMOD.jl](https://github.com/GENeSYS-MOD/GENeSYSMOD.jl)
  *	Download git: [Git - Downloads](https://git-scm.com/)
  *	Navigate to the folder where you want the repo to be located.
  * Open Git Bash by right clicking in the chosen folder and choosing "Git Bash Here"
  * Type the following command in Git Bash:

```
git clone https://github.com/GENeSYS-MOD/GENeSYSMOD.jl.git
git pull
```

2.	Open GENeSYS-MOD folder in Visual Studios
  *	File > Open folder

3.	Change to Julia environment for GENeSYSMOD.jl.

If you have cloned the repository and plan on changing the code of the model locally, you can then include the following at the top of your script: 

```julia
Pkg.develop(path="..\\GENeSYSMOD.jl")
using GENeSYSMOD
```
Where you replace the path with the relative or absolute path to the package. Note the "\\".

4. You can now continue using the model as normal (see [quick-start guide](/how_to_guides/julia/quick_start/quick-start)), but now, all source files are easily visible, accessible, and changeable for you. *We will add a more thorough guide for the different files in the near future.*
