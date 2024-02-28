=======
History
=======

1.1.2 (2024-02-26)
------------------

* Added FPID setting to part, otherwise only the fp_name and not the fp_lib appears in the final board.
* Added iterator to connect all pads of the same number to a given net. This mimics the behavior of the GUI editor.
* Added Python 3.12 to test environments.


1.1.1 (2023-09-10)
------------------

* `net.get_pins()` is now used when a SKiDL Circuit object is used as the input for generating a PCB.


1.1.0 (2022-08-13)
------------------

* Added `--libraries` command-line option to specify footprint library directories.


1.0.1 (2022-06-30)
------------------

* Fixed incompatibilities with KiCad V6 Python API (pcbnew).


1.0.0 (2021-09-16)
------------------

* Decided this tool was mature to the point it could be called 1.0.0.


0.1.3 (2021-05-19)
------------------

* The parts in the PCB are now given a non-overlapping arrangement
  grouped according to their hierarchical nesting.


0.1.2 (2021-05-18)
------------------

* The ``kinet2pcb()`` function will now generate a KiCad PCB file when given
  a netlist file name, a PyParsing object, or a SKiDL Circuit object.
* ``kinet2pcb`` can now be installed in the default Python interpreter on
  a system and it will look in ``/usr/lib/python3/dist-packages`` to find
  the ``pcbnew`` module installed by KiCad.  If the ``pcbnew`` module
  is not found there, add the correct location to the ``PYTHONPATH``
  environment variable.


0.1.1 (2019-03-09)
------------------

* Now runs under Python 2 & 3.


0.1.0 (2019-10-28)
------------------

* First release on PyPI.
