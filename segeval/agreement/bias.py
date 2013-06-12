'''
Arstein Poesio's annotator bias [ArtsteinPoesio2008]_.

.. moduleauthor:: Chris Fournier <chris.m.fournier@gmail.com>
'''
from . import __fnc_metric__
from .kappa import __fleiss_kappa_linear__
from .pi import __fleiss_pi_linear__


def __artstein_poesio_bias_linear__(dataset, **kwargs):
    '''
    Artstein and Poesio's annotator bias, or B (Artstein and Poesio, 2008,
    pp. 572).
    
    Arguments:
    segs_set_all -- A list of document segments for each coder (each in the
                    same item order), e.g.: [an1, an2, an3], where an1 = 
                    [d1, d2, d3], where d1 = segmass_d1.
    
    Returns:
    B as a Decimal object.
    '''
    # pylint: disable=C0103,W0142
    metric_kwargs = dict(kwargs)
    metric_kwargs['return_parts'] = True
    # Arguments
    return_parts = kwargs['return_parts']
    # Compute
    A_pi_e = __fleiss_pi_linear__(dataset, **metric_kwargs)[1]
    A_fleiss_e = __fleiss_kappa_linear__(dataset, **metric_kwargs)[1]
    bias = A_pi_e - A_fleiss_e
    # Return
    if return_parts:
        return A_pi_e, A_fleiss_e
    else:
        return bias


def artstein_poesio_bias_linear(dataset, **kwargs):
    # pylint: disable=W0142
    return __fnc_metric__(__artstein_poesio_bias_linear__, dataset, **kwargs)
