import os
import requests
from urllib.parse import urlparse
from osdata.analytics import AnalyticsService


def extract_dir_and_basename_from_url(url):
    """
    Extracts the directory and base name (file name) from a given URL.

    :param url: The URL from which to extract the directory and base name.
    :return: A tuple containing the directory path and the file name.
    """
    parsed_url = urlparse(url)
    path = parsed_url.path
    dir_path = os.path.dirname(path)
    dirs = dir_path.strip("/").split("/")
    parent_dir = dirs[-1] if len(dirs) > 1 else None
    basename = os.path.basename(path)
    return (parent_dir, basename)


class DataLoader:
    def __init__(self) -> None:
        self.metadata = None

    def find_by_alias(self, alias):
        categorical_metadata = "None"
        time_series_metadata = "None"
        url = "https://us-central1-osyris-1a1e5.cloudfunctions.net/findDatasetByAlias?alias={alias}".format(
            alias=alias)
        res = requests.get(url)
       # Check if the request was successful
        if res.status_code == 200:
            # Parse the JSON response into a Python dictionary
            dataset = res.json()['dataset']
            base_metadata = str(dataset['base_metadata'])
            if "time_series_metadata" in dataset:
                time_series_metadata = str(dataset['time_series_metadata'])
            if "categorical_metadata" in dataset:
                categorical_metadata = str(dataset['categorical_metadata'])
            self.metadata = {"base_metadata": base_metadata,
                             "time_series_metadata": time_series_metadata, "categorical_metadata": categorical_metadata}
            # Now you can work with the data object
            ds_path = dataset['download_path']
            loader = dataset['loader']
            return ds_path, loader
        else:
            print(
                f"Failed to retrieve data, status code: {res.status_code}")
            return None

    def download_file(self, ds_path, local_path):
        """
        Downloads a file from a given URL and saves it locally.
        """
        try:
            # root = os.path.expanduser('~')
            # local_path = os.path.join(root, file_path)
            dir = os.path.dirname(local_path)
            with requests.get(ds_path, stream=True) as r:
                r.raise_for_status()

                if not os.path.exists(dir):
                    os.makedirs(dir)
                with open(local_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            return local_path
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
