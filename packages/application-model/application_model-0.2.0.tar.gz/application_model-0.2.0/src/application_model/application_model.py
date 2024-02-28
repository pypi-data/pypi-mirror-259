

def generate_application_score(payload):
    """Generate score from ume application model.

    Parameters
    ----------
    payload : str
        Input data in json format.

    Returns
    -------
    float
        Application Score.

    Examples
    --------
    >>> json = {
        id: number,
        address: string
    }
    >>> generate_application_score(json)
    """

    return 0.8973
