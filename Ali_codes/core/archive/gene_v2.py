from __future__ import division
import sys
sys.path.append('../../')
from tools.userError import userError
from copy import deepcopy

class gene(object):
    """
    A class holding the information about a gene 

    Ali R. Zomorrodi - Segre Lab @ BU
    Last updated: 11-24-2014
    """

    def __init__(self, id, compartment = None, name = None, synonyms = [], locus_pos = None, expression_level = None, notes = None): 
    
        # Gene id 
        self.id = id

        # Gene compartment (case insensitive string)
        self.compartment = compartment

        # Gene name (case insensitive string)
        self.name = name

        # Name synonyms
        self.synonyms = synonyms

        # A tuple of type (start,end) indicating the start and end locus position of the gene 
        self.locus_pos = locus_pos

        # Expression level of the gene 
        self.expression_level = expression_level
  
        # Notes and comments
        self.notes = notes
  
