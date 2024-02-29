
import pickle
from importlib import resources

from application_model.data_processing.data_processor import DataProcessor


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

    # load model pickled
    with resources.path("application_model.resources", "model.pkl") as path:
        print(">>> ", path)
        #with open(path, "rb") as file:
        #    model = pickle.load(file)

    # load data_processor pickle with model metadata
    with resources.path("application_model.resources", "data_processor.pkl") as path:
        print(">>> ", path)
        #with open(path, "rb") as file:
        #    dataprocessor = pickle.load(file)

    return 0.8973