#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    errors_dict = {abs(predictions[i][0] - net_worths[i][0]) : i for i in range(len(predictions))}
    keys_sorted = sorted(errors_dict.keys())[:-(len(predictions) // 10)]
    for i in keys_sorted:
        cleaned_data.append((ages[errors_dict[i]], net_worths[errors_dict[i]], i))

    
    return cleaned_data

