"""
module __Boundary__: Subclass of GenericGeometry for Boundary Pores
==================================================================

.. warning:: The classes of this module should be loaded through the 'Geometry.__init__.py' file.

"""

import OpenPNM
from OpenPNM.Geometry import models as gm
from OpenPNM.Geometry.__GenericGeometry__ import GenericGeometry
import scipy as sp

class Boundary(GenericGeometry):
    r"""
    Boundary subclass of GenericGeometry.

    Parameters
    ----------
    loglevel : int
        Level of the logger (10=Debug, 20=INFO, 30=Warning, 40=Error, 50=Critical)

    """

    def __init__(self, **kwargs):
        r"""
        Initialize
        """
        super(Boundary,self).__init__(**kwargs)
        self._logger.debug("Method: Constructor")
        self._generate()
        
    def _generate(self):
        r'''
        '''
        self.add_model(propname='pore.seed',model=gm.pore_misc.constant,value=0.9999)
        self.add_model(propname='pore.diameter',model=gm.pore_misc.constant,value=0)
        self.add_model(propname='throat.seed',
                       model=gm.throat_misc.neighbor,
                       pore_prop='pore.seed',
                       mode='max')
        self.add_model(propname='throat.diameter',
                       model=gm.throat_misc.neighbor,
                       pore_prop='pore.diameter',
                       mode='max')
        self['pore.volume'] = 0.0
        self.add_model(propname='throat.length',model=gm.throat_length.straight)
        self.add_model(propname='throat.volume',model=gm.pore_misc.constant,value=0.0)
        self.add_model(propname='throat.area',model=gm.throat_area.cylinder)
        self.add_model(propname='throat.surface_area',model=gm.throat_surface_area.cylinder)
        self['pore.area'] = 1.0
        
if __name__ == '__main__':
    pn = OpenPNM.Network.TestNet()
    pass
