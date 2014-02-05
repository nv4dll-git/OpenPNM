
"""
module Physics
===============================================================================

"""
import OpenPNM
import scipy as sp
from functools import partial

class GenericPhysics(OpenPNM.Base.Utilities):
    r"""
    GenericPhysics - Base class to generate pore scale physics properties

    Parameters
    ----------

    """
    def __init__(self,network,fluid,**kwargs):
        super(GenericPhysics,self).__init__(**kwargs)
        self._logger.debug("Construct class")
        self._prop_list = []
        self._fluid = []
        #bind objects togoether
        self._fluid.append(fluid) #attach fluid to physics
        fluid._physics.append(self)
        self._net = network

    def regenerate(self):
        r'''
        This updates all properties using the methods indicated in the recipe.
        '''
        for item in self._prop_list:
            getattr(self,item)()
            
    def add_method(self,prop='',**args):
        try:
            function = getattr( getattr(OpenPNM.Physics, prop), args['model'] ) # this gets the method from the file
            preloaded_fn = partial(function, physics=self, network=self._net, fluid=self._fluid[0], **args) #
            setattr(self, prop, preloaded_fn)
            self._logger.info("Successfully loaded {}.".format(prop))
            self._prop_list.append(prop)
        except AttributeError: print('could not find',args['model'])



