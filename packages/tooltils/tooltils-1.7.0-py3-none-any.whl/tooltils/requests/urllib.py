"""
Internet requesting access methods - `urllib.request` version

This is the old version of the requesting module, using the basis of `urllib.request` as the source,
though it is not as featured or advanced as the `http.client` module, so that is being favoured
over this implementation.
"""


class _bm:
    from ssl import SSLCertVerificationError, get_default_verify_paths
    from json import JSONDecodeError, loads, dumps
    from urllib.error import URLError, HTTPError
    from http.client import RemoteDisconnected
    from os.path import abspath, exists
    from shutil import copyfileobj
    from typing import Any, Dict
    from gzip import decompress
    from socket import gaierror
    import urllib.request as u

    from ..errors import (ConnectionError, ConnectionTimeoutExpired, InvalidWifiConnection,
                          StatusCodeError, SSLCertificateFailed)
    from ..info import _loadConfig, version, _logger
    from ._helpers import ctx, prep_url, connected
    from ..os.info import platform, python_version

    if python_version.split('.')[1] == '7':
        GzipError = OSError
    else:
        from gzip import BadGzipFile

        GzipError = BadGzipFile
    
    class FileDescriptorOrPath:
        pass
    
    class url_response:
        pass

    def propertyTest(value, types: tuple, name: str):
        if value is None:
            return types[0]()
        elif not isinstance(value, types):
            raise TypeError(name + ' must be a valid \'' + types[0].__name__ + '\' instance')
        else:
            return value
    
_bm.logger = _bm._logger('.requests.urllib')


status_codes: _bm.Dict[int, str] = _bm.StatusCodeError.status_codes
"""List of official HTTP response status codes"""
defaultVerificationMethod: bool  = bool(_bm._loadConfig('requests')['defaultVerificationMethod'])

class NoRedirects(_bm.u.HTTPRedirectHandler):
    """An opener to prevent redirects in urllib requests"""

    def redirect_request(self, req, fp, code, msg, headers, newurl) -> None:
        return None

class request():
    """Initiate and send a request to a url"""

    def _setVariables(self, url: str, method: str, auth: tuple, 
                      data: dict, headers: dict, cookies: dict, 
                      cert: str, file_name: str, timeout: int, 
                      encoding: str, mask: bool, agent: str, 
                      verify: bool, redirects: bool,
                      override: bool):
        self.redirects: bool = bool(redirects)
        self.override:  bool = bool(override)
        self.verified:  bool = bool(verify)
        self.mask:      bool = bool(mask)
        self.sent:      bool = False
        self.cookies:   dict = _bm.propertyTest(cookies, (dict,), 'Cookies')
        self.data:      dict = _bm.propertyTest(data, (dict,), 'Data')
        self.headers: dict[str, str] = _bm.propertyTest(headers, (dict,), 'Headers')

        self.url:    str = _bm.prep_url(url, self.data)
        self._url:   str = self.url.replace('https://', '').replace('http://', '').split('/')
        self.port:   int = 443
        self.https: bool = True

        if type(method) is str:
            if method.upper() not in ['GET', 'POST', 'PUT', 'DOWNLOAD',
                                      'HEAD', 'PATCH', 'DELETE']:
                raise ValueError('Invalid http method \'{}\''.format(method))
            else:
                if method.upper() == 'DOWNLOAD':
                    self._method: str = 'GET'
                else:
                    self._method: str = method.upper()

                self.method: str = method.upper()
        else:
            raise TypeError('Method must be a valid \'str\' instance')
        if cert is None:
            self.cert: str = _bm.get_default_verify_paths().cafile
        else:
            if type(cert) is not str:
                raise TypeError('Certificate must be a valid \'str\' instance')
            elif not _bm.exists(cert) or cert.split('.')[-1] != 'pem':
                raise FileNotFoundError('Invalid certificate file path')
            elif verify:
                self.cert: str = cert
            else:
                self.cert: str = _bm.get_default_verify_paths().cafile
        if auth is None:
            self.auth = None
        elif type(auth) is not tuple and type(auth) is not list:
            raise TypeError('Authentiction must be a valid \'tuple\' instance')
        elif len(auth) != 2:
            raise ValueError('Invalid authentication details')
        else:
            self.auth: tuple = tuple(auth)
        if type(timeout) is not int and type(timeout) is not float:
            raise TypeError('Timeout must be a valid \'int\' instance')
        elif timeout > 999 or timeout < 1:
            raise ValueError('Timeout cannot be bigger than 999 or smaller than 0 seconds')
        else:
            self.timeout: int = int(timeout)
        if file_name is None:
            if self.method == 'DOWNLOAD':
                if (override and _bm.exists(self.url.split('/')[-1])) or (not _bm.exists(self.url.split('/')[-1])):
                    self.file_name: str = self.url.split('/')[-1]
                elif not override and _bm.exists(self.url.split('/')[-1]):
                    raise FileExistsError('Destination file already exists')
                else:
                    self.file_name: str = self.url.split('/')[-1]
            else:
                self.file_name = None
        elif type(file_name) != str:
            raise TypeError('File_name must be a valid \'str\' instance')
        else:
            if (override and _bm.exists(file_name)) or (not _bm.exists(file_name)):
                self.file_name: str = file_name
            elif not override and _bm.exists(file_name):
                raise FileExistsError('Destination file already exists')
        if agent is None:
            self.agent: str = f'Python-tooltils/{_bm.version}'
        else:
            self.agent: str = str(agent)
        if mask:
            if _bm.platform.lower() == 'windows':
                self.agent: str = 'Mozilla/5.0 (Windows NT 10.0; ' + \
                                  'rv:10.0) Gecko/20100101 Firefox/10.0'
            elif _bm.platform.lower() == 'macos':
                self.agent: str = f'Mozilla/5.0 (Macintosh; Intel Mac OS ' + \
                                  '10.15; rv:10.0) Gecko/20100101 Firefox/10.0'
            else:
                self.agent: str = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) ' + \
                                  'Gecko/20100101 Firefox/10.0'
        if type(encoding) is not str:
            raise TypeError('Encoding must be a valid \'str\' instance')
        else:
            self.encoding: str = encoding
    
    def _prepare(self):
        _headers: dict = {"User-Agent": self.agent, "Accept": "*/*", 
                          "Accept-Encoding": "gzip, deflate"}

        if self.method == 'POST' or self.method == 'PUT':
            self.headers.update({"Content-Type": "application/json;charset=utf-8"})

        for i in list(self.headers.keys()):
            _headers.update({str(i): str(self.headers[i])})

        for i in list(self.cookies.keys()):
            _headers.update('Cookie', f'{str(i)}={str(self.cookies[i])}')
        
        if self.method == 'POST' or self.method == 'PUT':
            _headers.update({"Content-Length": str(len(self.data)),
                             "Accept": "application/json"})
        
        self.headers: dict = _headers
        self._req          = _bm.u.Request(self.url, self.headers, method=self._method)
    
    def send(self) -> _bm.url_response:
        """Send the request"""

        if self.sent:
            raise _bm.ConnectionError('The request has already been sent')

        _data:    dict = self.data
        _encoding: str = self.encoding
        _openers: list = []
        error          = None

        if self.data:
            _bm.logger._debug(f'Sending data with length {len(self.data)}', 'requests.urllib.request().send')
    
        _bm.logger._debug(f'Sending headers: {self.headers}', 'requests.urllib.request().send')
        
        if self.method == 'POST' or self.method == 'PUT':
            _data: dict = _bm.dumps(_data).encode()
        
        if self.auth:
            man = _bm.u.HTTPPasswordMgrWithDefaultRealm()
            man.add_password(None, self.url, self.auth[0], self.auth[1])
            _openers.append(_bm.u.HTTPBasicAuthHandler(man))

        if self.redirects:
            _openers.append(NoRedirects)

        if _openers != []:
            _bm.u.install_opener(_bm.u.build_opener(*_openers))

        try:
            rdata = _bm.u.urlopen(self._req, _data, timeout=self.timeout,
                                  context=_bm.ctx(self.verified, self.cert))
        except _bm.RemoteDisconnected:
            error = _bm.ConnectionError('The server ended the connection without a response')
        except _bm.SSLCertVerificationError:
            error = _bm.SSLCertificateFailed()
        except _bm.HTTPError as err:
            if err.code not in list(_bm.StatusCodeError.status_codes.keys()):
                error = _bm.StatusCodeError(reason=f'{err.code} - Unofficial http status code')
            else:
                error = _bm.StatusCodeError(err.code)
        except _bm.URLError as err:
            if '[Errno 8]' in str(err) or '[Errno 11001]' in str(err):
                if _bm.connected():
                    error = _bm.StatusCodeError(404)
                else:
                    error = _bm.InvalidWifiConnection()

                _bm.logger.debug('tooltils.requests.connected() was called and may update the cache', 'requests.urllib.request().send') 
            elif 'ssl' in str(err):
                error = _bm.SSLCertificateFailed()
            else:
                error = err
        except _bm.gaierror:
            if _bm.connected():
                error = _bm.StatusCodeError(404)
            else:
                error = _bm.InvalidWifiConnection()
            
            _bm.logger.debug('tooltils.requests.connected() was called and may update the cache', 'requests.urllib.request().send')
        except TimeoutError:
            error = _bm.ConnectionTimeoutExpired('The request connection operation timed out')
        except ValueError:
            error = ValueError('Invalid URL \'' + self.url + '\'')

        _bm.u.install_opener(None)
        self.sent: bool = True

        if error:
            _bm.logger._debug('Request to <{}:{}> failed due to: {}'.format(self.url.split('/')[2], 
                                                                            self.port, type(error).__name__),
                              'requests.urllib.request().send')

            raise error

        self.rdata            = rdata
        self.code:        int = rdata.getcode()
        self.reason:      str = status_codes[self.code]
        self.status_code: str = f'{self.code} {self.reason}'
        self.headers:    dict = dict(self.headers)

        for i in rdata.getheaders():
            self.headers.update({i[0]: i[1]})
        
        if self.method != 'HEAD':
            if self.method != 'DOWNLOAD':
                text = self.rdata.read()

                try:
                    text = _bm.decompress(text)
                except _bm.GzipError:
                    pass

                self.text = text.decode(_encoding)
                self.raw  = text
                self.html = None
                self.path = None
            else:
                with open(self.file_name, 'wb+') as _f:
                    _bm.copyfileobj(rdata, _f)

                self.path: str = _bm.abspath(self.file_name)

            try:
                self.json: dict = _bm.loads(self.text)
            except _bm.JSONDecodeError:
                self.json = None

                try:
                    if self.text[0] == '<' or self.text[-1] == '>':
                        self.html: str = self.text
                except IndexError:
                    self.text = None
                    self.html = None
            except AttributeError:
                self.json = None
                self.text = None
                self.raw  = None
                self.html = None
        else:
            self.text = None
            self.raw  = None
            self.html = None
            self.json = None
            self.path = None
        
        _bm.logger._debug(f'Server replied with [{self.status_code}]', 'requests.urllib.request().send')
        _bm.logger._debug('Connection to server has been discarded', 'requests.urllib.request().send')
        
        return self

    def __init__(self, 
                 url: str,
                 method: str,
                 auth: tuple=None,
                 data: dict=None,
                 headers: dict=None,
                 cookies: dict=None,
                 cert: _bm.FileDescriptorOrPath=None, 
                 file_name: _bm.FileDescriptorOrPath=None,
                 timeout: int=15, 
                 encoding: str='utf-8',
                 mask: bool=False,
                 agent: str=None,
                 verify: bool=defaultVerificationMethod,
                 redirects: bool=True,
                 override: bool=False):
        self._setVariables(url, method, auth, data, headers, cookies, 
                           cert, file_name, timeout, encoding, mask, 
                           agent, verify, redirects, override)
        
        self._prepare()

        _bm.logger._debug('Setting up http{}/1.1 {} request to <{}:{}>'.format(
                          's' if self.verified else '', self.method, self.url.split('/')[2], self.port),
                          'requests.urllib.request().__init__')
        
    def __str__(self):
        if self.sent:
            code: str = '[' + str(self.code) + ']'
        else:
            code: str = '[Unsent]'

        return '<{} {} {}>'.format(self.method, self.url.split('/')[2], code)

    def read(self) -> _bm.Any:
        """Read the request file and return the raw data"""

        return self.raw

    def readlines(self) -> list:
        """Read the request file and return the data as a list split at every newline"""

        return self.text.splitlines()


def get(url: str, 
        auth: tuple=None,
        data: dict=None,
        headers: dict=None,
        cookies: dict=None,
        cert: _bm.FileDescriptorOrPath=None, 
        timeout: int=15, 
        encoding: str='utf-8',
        mask: bool=False,
        agent: str=None,
        verify: bool=defaultVerificationMethod,
        redirects: bool=True,
        override: bool=False
        ) -> _bm.url_response:
    """Send a GET request"""

    return request(url, 'GET', auth, data, 
                   headers, cookies, cert, 
                   None, timeout, encoding, 
                   mask, agent, verify, 
                   redirects, override).send()

def post(url: str, 
         auth: tuple=None,
         data: dict=None,
         headers: dict=None,
         cookies: dict=None,
         cert: _bm.FileDescriptorOrPath=None, 
         timeout: int=15, 
         encoding: str='utf-8',
         mask: bool=False,
         agent: str=None,
         verify: bool=defaultVerificationMethod,
         redirects: bool=True,
         override: bool=False
         ) -> _bm.url_response:
    """Send a POST request"""

    return request(url, 'POST', auth, data, 
                   headers, cookies, cert, 
                   None, timeout, encoding, 
                   mask, agent, verify, 
                   redirects, override).send()

def download(url: str, 
             auth: tuple=None,
             data: dict=None,
             headers: dict=None,
             cookies: dict=None,
             cert: _bm.FileDescriptorOrPath=None, 
             file_name: _bm.FileDescriptorOrPath=None,
             timeout: int=15, 
             encoding: str='utf-8',
             mask: bool=False,
             agent: str=None,
             verify: bool=defaultVerificationMethod,
             redirects: bool=True,
             override: bool=False
             ) -> _bm.url_response:
    """Download a file onto the disk"""

    return request(url, 'DOWNLOAD', auth, data, 
                   headers, cookies, cert, 
                   file_name, timeout, encoding, 
                   mask, agent, verify, 
                   redirects, override).send()

def head(url: str, 
         auth: tuple=None,
         data: dict=None,
         headers: dict=None,
         cookies: dict=None,
         cert: _bm.FileDescriptorOrPath=None, 
         timeout: int=15, 
         encoding: str='utf-8',
         mask: bool=False,
         agent: str=None,
         verify: bool=defaultVerificationMethod,
         redirects: bool=True,
         override: bool=False
        ) -> _bm.url_response:
    """Send a HEAD request"""

    return request(url, 'HEAD', auth, data, 
                   headers, cookies, cert, 
                   None, timeout, encoding, 
                   mask, agent, verify, 
                   redirects, override).send()

def put(url: str, 
        auth: tuple=None,
        data: dict=None,
        headers: dict=None,
        cookies: dict=None,
        cert: _bm.FileDescriptorOrPath=None, 
        timeout: int=15, 
        encoding: str='utf-8',
        mask: bool=False,
        agent: str=None,
        verify: bool=defaultVerificationMethod,
        redirects: bool=True,
        override: bool=False
        ) -> _bm.url_response:
    """Send a PUT request"""

    return request(url, 'PUT', auth, data, 
                   headers, cookies, cert, 
                   None, timeout, encoding, 
                   mask, agent, verify, 
                   redirects, override).send()

def patch(url: str, 
          auth: tuple=None,
          data: dict=None,
          headers: dict=None,
          cookies: dict=None,
          cert: _bm.FileDescriptorOrPath=None, 
          timeout: int=15, 
          encoding: str='utf-8',
          mask: bool=False,
          agent: str=None,
          verify: bool=defaultVerificationMethod,
          redirects: bool=True,
          override: bool=False
          ) -> _bm.url_response:
    """Send a PATCH request"""

    return request(url, 'PATCH', auth, data, 
                   headers, cookies, cert, 
                   None, timeout, encoding, 
                   mask, agent, verify, 
                   redirects, override).send()

def delete(url: str, 
           auth: tuple=None,
           data: dict=None,
           headers: dict=None,
           cert: _bm.FileDescriptorOrPath=None,
           cookies: dict=None,
           timeout: int=15, 
           encoding: str='utf-8',
           mask: bool=False,
           verify: bool=defaultVerificationMethod,
           agent: str=None,
           redirects: bool=True,
           override: bool=False
           ) -> _bm.url_response:
    """Send a DELETE request"""
 
    return request(url, 'DELETE', auth, data, 
                   headers, cookies, cert, 
                   None, timeout, encoding, 
                   mask, agent, verify, 
                   redirects, override).send()
