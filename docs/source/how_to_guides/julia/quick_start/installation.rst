Julia Installation
===================

1. We suggest using `Visual Studio
   Code <https://code.visualstudio.com/>`__.

2. Download the latest stable version of `the Julia Programming Language
   (julialang.org) <https://julialang.org/downloads/>`__.

3. Install Julia extension in Visual Studio Code:

   -  Click ‘Extensions’ buttion in Visual Studio Code on the left
      ribbon.
   -  Search for ‘Julia’, then install.

4. Download an optimization solver and get a license:

   -  Gurobi

      -  Academic licensed are issued by
         `Gurobi <https://www.gurobi.com/academia/academic-program-and-licenses/>`__.
      -  Commercial License.

   -  `CPLEX <https://www.ibm.com/products/ilog-cplex-optimization-studio/cplex-optimizer>`__
   -  `HiGHS <https://highs.dev/>`__, open source solver.

5. Clone the GitHub repository for
   `GENeSYS_MOD.jl <https://github.com/GENeSYS-MOD/GENeSYS_MOD.jl>`__

   -  Download git: `Git - Downloads <https://git-scm.com/>`__
   -  Navigate to the folder where you want the repo to be located.
   -  Open Git Bash by right clicking in the chosen folder and choosing
      “Git Bash Here”
   -  Type the following command in Git Bash:

::

   git clone https://github.com/GENeSYS-MOD/GENeSYS_MOD.jl.git
   git pull

6.  Open GENeSYS-MOD folder in Visual Studios

    -  File > Open folder

7.  Change to Julia environment for GENeSYS_MOD.jl.

8.  Open the Julia REPL by using the Alt+J+O command. The
    REPL(read-eval-print loop) is the interactive command line interface
    in Julia.

9.  Install packages in Visual Studio:

    -  In the REPL terminal, type ‘]’ to change to enter pkg mode
    -  Type ‘add ’, where package is equal to:

       -  JuMP
       -  Dates
       -  XLSX
       -  DataFrames
       -  CSV
       -  Ipopt
       -  

10. Open ‘test.jl’ and try to run using “Julia: Execute active file in
    REPL”.