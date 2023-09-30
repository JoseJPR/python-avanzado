def ordered_parameters(firstName, lastName, *args, **kwargs):
    pass

# this function has a bad order
def bad_ordered_parameters(*args, **kwargs, firstName):
    pass