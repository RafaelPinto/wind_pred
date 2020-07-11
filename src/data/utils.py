from pathlib import Path
import io
import zipfile
import requests


class DataDownloader():
    '''
    Download data using URL, destination directory, and file type.

    Parameters
    ----------
    url : str
          Target URL with data to be downloaded.
    dst : str
          Destination directory to save downloaded content.
    payload: dict, optional
          Parameters to be used with the URL in the get request.
          (default is None)
    zip: bool, optional
          Does the target URL retrieves a zipped file?
          (default is False)
    '''

    def __init__(self, url, dst, payload=None, zipped=False):
        self.dst = dst
        self._payload = payload
        self._zipped = zipped

        self._res = None

        # This calls get request
        self.url = url

    @property
    def dst(self):
        return self._dst

    @dst.setter
    def dst(self, new_dst):
        dst = Path(new_dst)
        self._dst = dst

    @property
    def zipped(self):
        return self._zipped

    @property
    def res(self):
        return self._res

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, new_url):
        res = requests.get(new_url, params=self._payload)

        res.raise_for_status()

        self._url = new_url
        self._res = res

    def write(self, dst_fname=''):
        if not self.dst.is_dir():
            self.dst.mkdir(parents=True)

        if self.zipped:
            zipped = zipfile.ZipFile(io.BytesIO(self.res.content))
            zipped.extractall(self.dst)
        else:
            with open(self.dst / dst_fname, 'wb') as fd:
                for chunk in self.res.iter_content(chunk_size=128):
                    fd.write(chunk)
