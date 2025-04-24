Running GENeSYS-MOD.jl
=====================


Running a case
--------------

Create a folder where you will be able to store your scripts, inputs and
outputs of the model. You can then include tyhe following at the top of
your script:

.. code:: julia

   Pkg.develop(path="..\\GENeSYS_MOD.jl")
   using GENeSYS_MOD

Where you replace the path with the relative or absolute path to the
package. Note the “\\”.This will allow you to use the package functions.

You can then run the model by running the function ``genesysmod`` with
the appropriate ``Switch``.

Using the published dataset
---------------------------

A dataset is published on the repository GENeSYS-MOD.data:
(https://github.com/GENeSYS-MOD/GENeSYS_MOD.data) This repository
contains the data including the sources and assumptions necessay to run
the model at a european level with a country resolution. Data for over
regions may be added with time. It also conmtains the tools necessary to
produce the input file for the model from this data. The tools are
accessed via a jupyter notebook script. More information can be found on
the repository.