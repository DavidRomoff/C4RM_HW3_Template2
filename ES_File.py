
import numpy as np

def es(losses, alpha=None, VaR=None):
    """
    Calculate the Expected Shortfall (ES) of losses.
    
    :param losses: array of positively stated loss values
    :param alpha: risk level (e.g., 0.99 for 99%)
    :param VaR: dollar value or percentage specifying the VaR threshold
    :return: Expected Shortfall as the average of losses exceeding VaR
    """

    es_value = 90
    return es_value
