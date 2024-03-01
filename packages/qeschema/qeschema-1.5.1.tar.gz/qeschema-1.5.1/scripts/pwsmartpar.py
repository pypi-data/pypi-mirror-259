#
# Copyright (c), 2015-2020, Quantum Espresso Foundation and SISSA (Scuola
# Internazionale Superiore di Studi Avanzati). All rights reserved.
# This file is distributed under the terms of the MIT License. See the
# file 'LICENSE' in the root directory of the present distribution, or
# http://opensource.org/licenses/MIT.
#
# Authors: Davide Brunato
#
"""
reads xml inputs and suggest smart parallelization paremeters
"""
import sys

from pyrsistent import b
import qeschema
from qeschema.utils import etree_iter_path
 


def parse_args():
   """
   command arguent parsing
   """
   import argparse
   parser=argparse.ArgumentParser(
      description="This program reads an XML input and some information about the node"
                  "and prints a suggestion of smart parallelizazion parameters"
                  )
   parser.add_argument("-v", "--verbosity", action="count", default=1,
                        help="Increase output verbosity.")
   parser.add_argument('-in', metavar='FILE', required=True, help="XML input filename.")
   parser.add_argument('-nodes', metavar='INTEGER', required=False, default=1, 
                        help="Number of nodes")
   parser.add_argument('-cpus_per_node', metavar='INTEGER', required=False, default=1,
                     help="CPUS per node" )
   parser.add_argument('-mem', metavar="GigaBytes", required=True, help="Memory per Node in GB" )
   parser.add_argument('-pseudo_dir', metavar='PATH', required=False, default='./',help="PATH to pseudos")
   return parser.parse_args()

def get_doc_path(doc, path):
      if doc.schema.find(path):
         return doc.schema.find(path).decode(doc.find(path))
      else:
         return None
      
def count_kb(sp, pseudo_dir, positions):
   """
   :sp: dict with species infos
   :pseudo_dir: path to pseudos
   :positions: dict with atomic positions infos
   counts KB projectors in a calculation 
   :return: int  the number of KB used
   """
   from pathlib import Path
   from xml.etree import ElementTree as Etree
   p = Path(pseudo_dir, sp['pseudo_file'])
   tree = Etree.parse(p)
   betas = [_ for _ in tree.findall('.//PP_NONLOCAL/*') if 'PP_BETA' in _.tag]
   kb = sum((2 * int(dict( _.items())['angular_momentum']) + 1 for _ in betas)) 
   count_sp = sum((1 for _ in positions['atom'] if _['@name'] == sp['@name'] ))
   return count_sp*len(betas), count_sp*kb 

def estimate_grid(basis, cell):

   from math import sqrt
   a1 = cell['a1']
   a2 = cell['a2']
   a3 = cell['a3']
   if basis.get('ecutrho'):
      gcut = sqrt(float(basis.get('ecutrho')))
   else:
      gcut= 2.0 * sqrt(float.basis.get('ecutwfc'))
   
   import pdb
   pdb.set_trace()
   nr1 = int(round(gcut * sqrt(sum((x*x for x in a1))),0))
   nr2 = int(round(gcut * sqrt(sum((x*x for x in a2))),0)) 
   nr3 = int(round(gcut * sqrt(sum((x*x for x in a3))),0)) 
   return nr1, nr2, nr3 

if __name__=='__main__' :
   if sys.version_info < (3, 5, 0):
      sys.stderr.write("You need python 3.5 or later to run this program\n")
      sys.exit(1)

   args = parse_args()
   print("Smart parametrization parameters for  %r ...\n" % getattr(args, 'in'))

   if __package__ is None:
      from os import path
      sys.path.append(path.abspath(path.dirname(__file__)+'/../'))

   import qeschema
   import os
   import xml.etree.ElementTree as Etree 
   args = parse_args()
   input_fn = getattr(args,'in')
   pseudo_dir = getattr(args, 'pseudo_dir')  
   tree = Etree.parse(input_fn)
   root = tree.getroot() 
   element_name = root.tag.split('}')[-1]
   if element_name == 'espresso':
      doc = qeschema.PwDocument(source=input_fn)
   else: 
      sys.stderr.write("Could not find correct XML in %s, exiting...\n" % input_fn)
      sys.exit(1)
   root = None
   tree = None

   basis = get_doc_path(doc,'.//input//basis')
   cell  = get_doc_path(doc, './/input//cell')
   species = get_doc_path(doc, './/input//atomic_species')['species']
   try:
      positions = get_doc_path(doc, './/input//atomic_positions')
   except AttributeError:
      positions = get_doc_path(doc, './/input//crystal_positions')
   import pdb
   nkb   = sum((count_kb(_,pseudo_dir, positions)[0] for _ in species))
   nwfcat =  sum((count_kb(_,pseudo_dir, positions)[1] for _ in species)) 
   print (f"nkb={nkb}, n_wfc_at={nwfcat}")
   fft_grid = estimate_grid(basis, cell)
   print ("estimated fff grid = ("+":".join(["estimated fft grid (",]+[f"{_}" for _ in fft_grid])+")")  

         
      



                                                      