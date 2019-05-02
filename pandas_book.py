import pandas as pd


def binner(values, bins):
    """ Group data according to a set bins
    :param values: List of data values to be set to bins
    :param bins: List of bins to be applied to values
    :return:
    """
    if values and bins:
        binned_data = pd.cut(values, bins)
        print(f'Bins: {binned_data}')
        return binned_data
    else:
        print('Error, values/bins must be populated')


