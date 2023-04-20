'''
DESCRIPTION
        Save a selection to pdb-format and run reduce on it to build hydrogens

ARGUMENTS
        selection = string: a valid PyMOL selection {default: all}
        returns: object called selection_H, the reduced object. 

SEE ALSO
        http://kinemage.biochem.duke.edu/software/README.reduce.html

# @AUTHOR: Anthe Janssen
# Copyright (c) 2021, Anthe Janssen
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following
# conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice, this list of conditions and the following
#     * disclaimer.
#     * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
#     * disclaimer in the documentation and/or other materials provided with the distribution.
#     * Neither the name of the <ORGANIZATION> nor the names of its contributors may be used to endorse or promote products derived
#     * from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# DATE  : 2021-02-17
# REV   : 1

'''

from pymol import cmd
from pymol import stored
import subprocess

def reduce(selection='all'):

    export_filename = selection + '_to_reduce.pdb'
    import_filename = selection + '_reduced.pdb' 
    imported_object = selection + '_H'

    model = cmd.get_model(selection)
    cmd.save(export_filename, selection)

    reduce_cmd = '/home/janssenapa/Software/Reduce/reduce -Quiet -build ' + export_filename + ' > ' + import_filename
    with open('reduce_output.txt','w+') as ferr:
        process=subprocess.run(reduce_cmd, shell=True, universal_newlines=True, stderr=ferr)

    cmd.load(import_filename, imported_object)

    return_string = 'Reduced object loaded as ' + selection + '_H' 
    print(return_string)

    return return_string

cmd.extend("reduce", reduce)
