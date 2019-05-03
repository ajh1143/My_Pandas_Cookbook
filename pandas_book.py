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
    elif values and not bins:
        print('Error, bin parameter is empty/must be populated')
    elif not values and bins:
        print('Error, values parameter is empty/must be populated')
    else:
        print('Error, both bins and values parameters are empty/must be populated')


