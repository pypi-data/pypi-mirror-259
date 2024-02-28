"""HTTP/1.1 simple interface"""


class _bm:
    from http.client import (HTTPSConnection, HTTPConnection, InvalidURL, 
                             HTTPResponse)
    from ssl import SSLError, SSLCertVerificationError, SSLContext, get_default_verify_paths
    from json import dumps, loads, JSONDecodeError
    from os.path import abspath, exists
    from shutil import copyfileobj
    from typing import Union, Dict
    from logging import getLogger
    from base64 import b64encode
    from gzip import decompress
    from socket import gaierror
    from typing import List
    from os import remove

    from ..errors import (ActiveRequestError, InvalidRequestURL, ConnectionError, 
                          ConnectionTimeoutExpired, InvalidWifiConnection,
                          StatusCodeError, SSLCertificateFailed, 
                          RequestRedirectError, RequestCodecError)
    from ..info import _loadCache, _loadConfig, _editCache, _deleteCacheKey, version, _makeFunc
    from ._helpers import ctx, prep_url, connected
    from ..os.info import platform, python_version
    from ..os import getCurrentWifiName

    if python_version.split('.')[1] == '7':
        GzipError = OSError
    else:
        from gzip import BadGzipFile

        GzipError = BadGzipFile

    class FileDescriptorOrPath:
        pass

    class HTTP_Port:
        pass

    def propertyTest(value, types: tuple, name: str):
        if value is None:
            return types[0]()
        elif not isinstance(value, types):
            raise TypeError(name + ' must be a valid \'' + types[0].__name__ + '\' instance')
        else:
            return value
    
    def _logger(module: str):
        logger = _bm.getLogger('tooltils' + module)

        checkID = lambda msg, id: msg if id == -1 else f'R{id} | {msg}'

        logger._debug    = lambda msg, func, id: logger.debug(checkID(msg, id), extra={"caller": _bm._makeFunc(module, func)})
        logger._info     = lambda msg, func, id: logger.info(checkID(msg, id), extra={"caller": _bm._makeFunc(module, func)})
        logger._warning  = lambda msg, func, id: logger.warning(checkID(msg, id), extra={"caller": _bm._makeFunc(module, func)})
        logger._error    = lambda msg, func, id: logger.error(checkID(msg, id), extra={"caller": _bm._makeFunc(module, func)})
        logger._critical = lambda msg, func, id: logger.critical(checkID(msg, id), extra={"caller": _bm._makeFunc(module, func)})

        return logger
    
    newestID: int = 0

_bm.logger = _bm._logger('.requests')

import tooltils.requests.urllib as urllib


status_codes: _bm.Dict[int, str] = _bm.StatusCodeError.status_codes
"""List of official HTTP response status codes"""
defaultVerificationMethod:  bool = bool(_bm._loadConfig('requests')['defaultVerificationMethod'])
redirectLimit:               int = _bm._loadConfig('requests')['redirectLimit']

def where() -> tuple:
    """Return default certificate file and path locations used by Python"""

    # if get_default_verify_paths().cafile is None then it's using openssl

    data = _bm.get_default_verify_paths()

    if data.cafile == None:
        return (data.openssl_capath, data.openssl_cafile)
    else:
        return (data.capath, data.cafile)

def connected() -> bool:
    """Get the connectivity status of the currently connected wifi network"""

    _bm.logger._debug('A blocking function was called and the cache may be updated', 'requests.connected', -1)
    
    return _bm.connected()

def ctx(verify: bool=True, cert: str=None) -> _bm.SSLContext:
    """Create a custom SSLContext instance"""

    return _bm.ctx(verify, cert)

def prep_url(url: str, 
             data: dict=None,
             https: bool=True,
             order: bool=False
             ) -> str:
    """Configure a URL making it viable for requests"""

    return _bm.prep_url(url, data, https, order)

def verifiable() -> bool:
    """Determine whether requests can be verified with a valid ssl certificate on the current connection"""

    _bm.logger._debug('A blocking function was called and the cache may be updated', 'requests.verifiable', -1)

    caching: bool = bool(_bm._loadConfig('requests')["verifiableCaching"])
    wifiName: str = _bm.getCurrentWifiName()

    if wifiName == None:
        return False
    
    if caching:
        configData: dict = _bm._loadConfig('requests')
        cacheData:  dict = _bm._loadCache('requests')

        if cacheData["verifiableTimesChecked"] >= configData["verifiableCachingCheck"]:
            _bm._editCache('requests', {"verifiableTimesChecked": 0})
            _bm._deleteCacheKey('requests', wifiName, 'verifiableNetworkList')
        else:
            if wifiName in list(cacheData["verifiableNetworkList"].keys()):
                _bm._editCache('requests', 
                {"verifiableTimesChecked": cacheData["verifiableTimesChecked"] + 1})

                return cacheData["verifiableNetworkList"][wifiName]

    try:
        head('httpbin.org/get', mask=True, redirects=False)

        result: bool = True
    except (_bm.ConnectionError, _bm.SSLCertificateFailed):
        result: bool = False

    if caching:
        _bm._editCache('requests', {wifiName: result}, 'verifiableNetworkList')
        _bm._editCache('requests', {"verifiableTimesChecked": 1})

    return result

class advancedContext():
    """Create an advanced context intended to be used for extended functionality with requesting"""

    def __init__(self, 
                 redirectLimit: int=redirectLimit, 
                 extraLogs: bool=False, 
                 SSLContext: _bm.SSLContext=None):
        if type(redirectLimit) is not int:
            raise TypeError('RedirectLimit must be a valid \'int\' instance')
        elif redirectLimit < 1:
            raise ValueError('RedirectLimit must be bigger than 1')
        if type(SSLContext) is not _bm.SSLContext and SSLContext is not None:
            raise TypeError('SSLContext must be a valid \'ssl.SSLContext\' instance')
    
        self.redirectLimit: int = redirectLimit
        self.extraLogs:    bool = extraLogs
        self.SSLContext         = SSLContext

class tooltilsResponse():
    """
    Create a tooltils style response class from the `http.client.HTTPResponse` attribute \n
    This class is not intended to be called directly because there is other data that requires
    attributes from the actual connection reference, but exists to allow Python text highlighters
    to show the return properties
    """
    def __init__(self, data: _bm.HTTPResponse, url: str, method: str, 
                 encoding: _bm.Union[str, tuple]=('utf-8', 'ISO-8859-1'), 
                 _agent: str=None, _headers: dict=None, 
                 _clog: bool=None, _rID: int=-1):
        if type(data) is not _bm.HTTPResponse:
            raise TypeError('Data must be a valid \'http.client.HTTPResponse\' instance')
        
        if type(url) is not str:
            raise TypeError('Uri must be a valid \'str\' instance')
        
        if type(method) is not str:
            raise TypeError('Method must be a valid \'str\' instance')
        
        if type(encoding) is not str and type(encoding) is not tuple:
            raise TypeError('Encoding must be a valid \'str\' or \'tuple\' instance')

        if _clog:
            caller: str = 'openConnection().send'
        elif _clog == False:
            caller: str = 'request().send'
        else:
            caller: str = 'tooltilsResponse'

        self.data             = data
        self.code:        int = self.data.status
        self.reason:      str = self.data.reason
        self.status_code: str = f'{self.code} {self.reason}'
        self.headers:    dict = dict(self.data.getheaders())
        self.pos:         int = 0

        class end_data():
            def __init__(self, url, headers, agent):
                self.url          = url
                self.sent_headers = headers
                self.agent        = agent
        
        # do some weird inline comparisons to make sure the type is reported as str | None
        _agent = _agent if _agent else str(self.headers.get(
                 'User-Agent', None)) if self.headers.get(
                 'User-Agent', None) else None

        self.end_data = end_data(url, _headers, _agent)

        if method == 'HEAD':
            self.raw  = None
            self.text = None
            self.json = None
            
            return

        self.raw: bytes = self.data.read()

        try:
            self.text = _bm.decompress(self.raw)
        except _bm.GzipError as err:
            if 'Not a gzipped file' in str(err):
                _bm.logger._debug('Request response body was not gzipped', 
                                  'requests.' + caller, _rID)
                            
            self.text = self.raw

        if type(encoding) is str:
            try:
                self.text: str = str(self.text.decode(encoding))
            except UnicodeDecodeError:
                pass
        else:
            for i in encoding:
                try:
                    self.text: str = str(self.text.decode(i))

                    break
                except UnicodeDecodeError:
                    pass
                        
            if type(self.text) is not str:
                raise _bm.RequestCodecError('None of the specified encodings were able to decipher the ' + 
                                            'request response body', encoding)
                        
            try:
                self.json: dict = _bm.loads(self.text)
            except _bm.JSONDecodeError:
                self.json = None

                _bm.logger._debug('Request response body is not json', 
                                  'requests.' + caller, _rID)
                        
    def read(self, amt: int=None) -> bytes:
        """
        Read the request response body or up to amt bytes \n
        This method only exists for cross compatibility"""

        if self.raw == None:
            raise ValueError('The request response body was unable to be read')

        if type(amt) is not int and amt != None:
            raise TypeError('Amt must be a valid \'int\' instance')
        elif amt:
            if (self.pos + amt) > len(self.raw):
                raise ValueError('Tried to read over the length of the request response body')
            elif amt < 0:
                raise ValueError('Amt must be bigger than 0')

        if amt:
            try:
                raw        = self.raw[self.pos:self.pos + amt]
                self.pos += amt

                return raw
            except IndexError:
                raise ValueError('Tried to read over the length of the request response body')
        else:
            return self.raw

    def readlines(self, amt: int=None) -> _bm.List[str]:
        """
        Read the request response body or up to amt bytes and return as a list split at every newline \n
        This method only exists for cross compatibility
        """

        if self.raw == None:
            raise ValueError('The request response body was unable to be read')

        if type(amt) is not int and amt != None:
            raise TypeError('Amt must be a valid \'int\' instance')
        elif amt:
            if (self.pos + amt) > len(self.raw):
                raise ValueError('Tried to read over the length of the request response body')
            elif amt < 0:
                raise ValueError('Amt must be bigger than 0')
        
        if amt:
            try:
                text       = self.text[self.pos:self.pos + amt].splitlines()
                self.pos += amt

                return text
            except IndexError:
                raise ValueError('Tried to read over the length of the request response body')
        else:
            return self.text.splitlines()
    
    def seek(self, pos: int) -> None:
        """Seek to a position in the request response body \n
        This method only exists for cross compatibility"""

        if self.raw == None:
            raise ValueError('The request response body text position was unable to be changed')

        if type(pos) is not int:
            raise TypeError('Pos must be a valid \'int\' instance')
        if pos > len(self.text):
            raise ValueError('Tried to read over the length of the request response body')
        if pos < 0:
            raise ValueError('Pos must be bigger than 0')
        
        self.pos = pos
    
    def close(self) -> None:
        """This method does nothing and only exists for cross compatibility"""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == None:
            return True
    
    def __str__(self):
        return f"<Request {'/'.join(self.end_data.url.split('/')[2:])} [{self.status_code}]>"

    def __repr__(self):
        return f"<Request {'/'.join(self.end_data.url.split('/')[2:])} [{self.status_code}]>"

class openConnection():
    """Open a re-usable connection to a URL"""

    def __init__(self, 
                 host: str, 
                 port: int=(80, 443),
                 https: bool=True,
                 verify: bool=defaultVerificationMethod,
                 redirects: bool=True,
                 redirect_loops: bool=False,
                 auth: tuple=None,
                 data: dict=None,
                 headers: dict=None,
                 cookies: dict=None,
                 cert: str=None,
                 file_name: str=None,
                 write_binary: bool=False,
                 override: bool=False,
                 timeout: _bm.Union[int, float]=15,
                 encoding: _bm.Union[str, tuple]=('utf-8', 'ISO-8859-1'),
                 mask: bool=False,
                 agent: str=None,
                 proxy: str=None,
                 advContext: advancedContext=None,
                 _clog: bool=True,
                 _redirect: bool=False):
        # this is for logging to help differentiate requests
        self.rID      = _bm.newestID
        _bm.newestID += 1

        if _redirect:
            self.rID     -= 1
            _bm.newestID -= 1

        # variables that are defined once and never changed
        self._setStartVariables(host, port, https, verify, cert, timeout, proxy, advContext)

        # variables that may change
        self._setVariables(redirects, redirect_loops, auth, data, headers, cookies, 
                           file_name, write_binary, override, encoding, mask, agent)
        
        self.state:   str = str('Defined')
        self._state:  int = 0
        self._clog:  bool = bool(_clog)
        self._caller: str = 'openConnection' if _clog else 'request'
        
        if _clog:
            _bm.logger._debug('Setting up http{}/1.1 connection to <{}:{}>'.format(
                              's' if self.https else '', self._host, self.port), 
                              'requests.openConnection', self.rID)
        
        if self.port != 80 and self.port != 443:
            _bm.logger._debug('Connection is not using port 80 or 443, it may fail', 
                              f'requests.{self._caller}', self.rID)
        
        # create request reference
        self._setup()
        
        # connect to the host
        self.open()

    def __str__(self):
        return f'<Connection {self._host} [{self.state}]>'
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == None:
            self._state = 1
            self.close()

            return True
    
    def _setStartVariables(self, host: str, port: int, https: bool, verify: bool,
                           cert: str, timeout: _bm.Union[int, float], proxy: str, 
                           advContext: advancedContext):
        self.verify: bool = bool(verify)
        self.https:  bool = bool(https)
        self.host:    str = prep_url(host, https=self.https)
        self._host:   str = self.host.replace('http' + ('s' if self.https else '') + '://', '')

        if '/' in self._host:
            raise _bm.InvalidRequestURL('The host should only contain the website name and extension (etc httpbin.org)')
        elif '.' not in self._host:
            raise _bm.InvalidRequestURL('The host should the website name and extension (etc httpbin.org)')

        quote: bool = False

        for i in self._host:
            if quote:
                if i == '\'' or i == '"':
                    quote: bool = False
            else:
                if i == '\'' or i == '"':
                    quote: bool = True
                else:
                    if i == ':':
                        raise _bm.InvalidRequestURL('You may not include a colon in the URL (this includes ports)')

        if self.https and self.verify:
            if cert is None:
                self.cert: str = where()[1]
            else:
                if type(cert) is not str:
                    raise TypeError('Certificate must be a valid \'str\' instance')
                elif cert.split('.')[-1] != 'pem':
                    raise FileNotFoundError('Invalid certificate file path')
                elif not _bm.exists(cert) and cert != where()[1]:
                    raise FileNotFoundError('The certificate file does not exist')
                else:
                    self.cert = cert
        else:
            self.cert = None

        if type(timeout) is not int and type(timeout) is not float:
            raise TypeError('Timeout must be a valid \'int\' or \'float\' instance')
        else:
            self.timeout: _bm.Union[int, float] = timeout

        if port == (80, 443):
            self.port: int = int(443 if self.https else 80)
        elif type(port) is not int:
            raise TypeError('Port must be a valid \'int\' instance')
        else:
            self.port: int = port
        
        if proxy is None:
            self.proxy = None
        elif type(proxy) is not str:
            raise TypeError('Proxy must be a valid \'str\' instance')
        else:
            if ':' not in proxy:
                raise ValueError('Proxy must have the format \'host:port\'')

            self.proxy: str = proxy

        if advContext is None:
            self.advContext         = None
            self.redirectLimit: int = redirectLimit
            self.extraLogs:    bool = False
            self.SSLContext         = None
        elif type(advContext) is not advancedContext:
            raise TypeError('AdvContext must be a valid \'tooltils.requests.advancedContext\' instance')
        else:
            self.advContext         = advContext
            self.redirectLimit: int = advContext.redirectLimit
            self.extraLogs:    bool = advContext.extraLogs
            self.SSLContext         = advContext.SSLContext

    def _setVariables(self, redirects: bool, redirect_loops: bool, auth: tuple, 
                      data: dict, headers: dict, cookies: dict, file_name: str,
                      write_binary: bool, override: bool, 
                      encoding: _bm.Union[str, tuple], mask: bool, agent: str,
                      set: bool=True):
        if set:
            self.redirect_loops: bool = bool(redirect_loops)
            self.write_binary:   bool = bool(write_binary)
            self.redirects:      bool = bool(redirects)
            self.override:       bool = bool(override)
            self.mask:           bool = bool(mask)
            self.cookies:        dict = dict(_bm.propertyTest(cookies, (dict,), 'Cookies'))
            self.headers:        dict = dict(_bm.propertyTest(headers, (dict,), 'Headers'))
            self.data:           dict = dict(_bm.propertyTest(data, (dict, ), 'Data'))
        else:
            redirect_loops: bool = bool(redirect_loops)
            write_binary:   bool = bool(write_binary)
            redirects:      bool = bool(redirects)
            override:       bool = bool(override)
            mask:           bool = bool(mask)
            cookies:        dict = dict(_bm.propertyTest(cookies, (dict,), 'Cookies'))
            headers:        dict = dict(_bm.propertyTest(headers, (dict,), 'Headers'))
            data:           dict = dict(_bm.propertyTest(data, (dict,), 'Data'))

        if auth is None:
            self.auth = None
        elif type(auth) is not tuple:
            raise TypeError('Authentiction must be a valid \'tuple\' instance')
        elif len(auth) != 2:
            raise ValueError('Invalid authentication details')
        else:
            if set:
                self.auth: tuple = tuple(auth)
            else:
                auth: tuple = tuple(auth)

        if file_name is None:
            self.file_name = None
        elif type(file_name) != str:
            raise TypeError('File_name must be a valid \'str\' instance')
        else:
            if set:
                self.file_name: str = file_name

        if agent is None:
            self.agent = None
        elif type(agent) is not str:
            raise TypeError('Agent must be a valid \'str\' instance')
        else:
            if set:
                self.agent: str = agent

        if type(encoding) is not str and type(encoding) is not tuple:
            raise TypeError('Encoding must be a valid \'str\' or \'tuple\' instance')
        else:
            if set:
                self.encoding: _bm.Union[str, tuple] = encoding
        
        if not set:
            return {"redirects": redirects, "redirect_loops": redirect_loops, 
                    "auth": auth, "data": data, "headers": headers, 
                    "cookies": cookies, "file_name": file_name, 
                    "write_binary": write_binary, "override": override, 
                    "encoding": encoding, "mask": mask, "agent": agent}
    
    def _setup(self) -> None:
        _bm.logger._debug('Creating request reference', f'requests.{self._caller}', self.rID)

        if self.proxy:
            self._req = _bm.HTTPConnection(self.proxy.split(':')[0], self.proxy.split(':')[1], 
                                           timeout=self.timeout)

            self._req.set_tunnel(self._host, self.port)

            return

        if self.https:
            if self.SSLContext:
                _ctx = self.SSLContext

                if self.extraLogs:
                    _bm.logger._debug('Using custom SSLContext instance', f'requests.{self._caller}', self.rID)
            else:
                _ctx = ctx(self.verify, self.cert)

                if self.extraLogs:
                    _bm.logger._debug('Using request created SSLContext instance', f'requests.{self._caller}', self.rID)

            self._req = _bm.HTTPSConnection(self._host, self.port, timeout=self.timeout, context=_ctx)
        else:
            self._req = _bm.HTTPConnection(self._host, self.port, timeout=self.timeout)
    
    def _prepare(self, method: str, auth: tuple, data: dict, headers: dict, 
                 cookies: dict, mask: str, agent: str, close: bool) -> None:
        _bm.logger._debug('Preparing a request', f'requests.{self._caller}().send', self.rID)

        _data = None

        if not close:
            connection: str = 'keep-alive'
        else:
            connection: str = 'close'
        
        if agent is None:
            agent: str = f'Python-tooltils/{_bm.version}'

        if mask:
            if _bm.platform.lower() == 'windows':
                agent: str = 'Windows NT 10.0; Win64; x64'
            elif _bm.platform.lower() == 'macos':
                agent: str = 'Macintosh; Intel Mac OS X 14.2'
            else:
                agent: str = 'X11; Ubuntu; Linux i686'
            
            agent: str = str('Mozilla/5.0 (' + agent + '; rv:109.0) Gecko/20100101 Firefox/121.0')

        if method in ('POST', 'PUT') and data:
            _data: dict = _bm.dumps(data).encode()

            headers.update({"Content-Length": str(len(_data))})

            if self.extraLogs:
                _bm.logger._debug('Adding \'Content-Length\' to headers because the method is POST or PUT', f'requests.{self._caller}().send', self.rID)

        elif method == 'TRACE':
            headers.update({"Content-Type": "message/http"})

            if self.extraLogs:
                _bm.logger._debug('Adding \'Content-Type\': \'message/http\' to headers because the method is TRACE', f'requests.{self._caller}().send', self.rID)

        headers.update({"Connection": connection, "User-Agent": agent, 
                        "Accept": "*/*", "Accept-Encoding": "gzip, deflate"})
        
        for i in list(cookies.keys()):
            headers.update('Cookie', f'{str(i)}={str(cookies[i])}')
        
        if auth:
            headers.update({"Authorization": "Basic {}".format(
                    _bm.b64encode(f'{auth[0]}:{auth[1]}'.encode()).decode('ascii'))})

        if self.extraLogs:
            _bm.logger._debug('Adding necessary request headers', f'requests.{self._caller}().send', self.rID)

            if cookies:
                _bm.logger._debug('Adding cookies to request headers', f'requests.{self._caller}().send', self.rID)
            
            if auth:
                _bm.logger._debug('Adding authorisation to request headers', f'requests.{self._caller}().send', self.rID)

        return (_data, headers)
    
    def close(self) -> None:
        """Close the connection to the host"""

        if self._state == 0:
            raise _bm.ConnectionError('The connection to the host has not been opened yet', self.host)
        elif self._state == 2:
            raise _bm.ConnectionError('A request is currently in progress', self.host)
        
        self._req.close()
        
        self.state:  str = str('Closed')
        self._state: int = 0

        caller: str = 'close' if self._clog else 'send'

        _bm.logger._debug('The connection was closed', f'requests.{self._caller}().{caller}', self.rID)

    def open(self) -> None:
        """Open the connection to the host"""

        if self._state == 1:
            raise _bm.ConnectionError('The connection to the host is already active', self.host)
        elif self._state == 2:
            raise _bm.ConnectionError('A request is currently in progress', self.host)

        caller: str = 'open' if self._clog else 'send'

        try:
            self._req.connect()
        except _bm.InvalidURL as err:
            if 'nonnumeric port' in str(err):
                raise _bm.InvalidRequestURL('You may not include a colon in the URL (this includes ports)')
            elif 'control characters' in str(err):
                raise _bm.InvalidRequestURL('URL contains intransmissible objects')
            else:
                raise _bm.InvalidRequestURL('An unknown url related error occured, check the above stack trace for more info')
        except ConnectionResetError:
            raise _bm.ActiveRequestError('The host ended the connection without a response', self.host)
        except _bm.SSLCertVerificationError:
            raise _bm.SSLCertificateFailed()
        except _bm.gaierror:
            # call the _helpers.py version because it doesn't have the different logging call
            if _bm.connected():
                error = _bm.StatusCodeError(404)
            else:
                error = _bm.InvalidWifiConnection()
            
            _bm.logger._debug('tooltils.requests.connected() was called and may update the cache', f'requests.{self._caller}().{caller}', self.rID)

            raise error
        except TimeoutError:
            raise _bm.ConnectionTimeoutExpired(timeout=self.timeout)
        except OSError:
            raise _bm.ConnectionError('An unknown error occured, check the above stack trace for more info')

        self.state:  str = str('Connected')
        self._state: int = 1

        _bm.logger._debug('The connection was opened', f'requests.{self._caller}().{caller}', self.rID)
    
    def change(self, **params: object) -> None:
        """
        Change the data being sent for requests made to this host \n
        You may pass the parameters `redirects`, `redirect_loops`, `auth`, `data`, `headers`, `cookies`, `cert`,
        `file_name`, `write_binary`, `override`, `encoding`, `mask` and `agent` as seen in the `openConnection`
        class definition
        """

        self._setVariables(
            params.get('redirects', self.redirects), params.get('redirect_loops', self.redirect_loops),
            params.get('auth', self.auth), params.get('data', self.data), 
            params.get('headers', self.headers), params.get('cookies', self.cookies), 
            params.get('file_name', self.file_name), params.get('write_binary', self.write_binary), 
            params.get('override', self.override), params.get('encoding', self.encoding), 
            params.get('mask', self.mask), params.get('agent', self.agent)
        )

    def send(self,
             method: str='GET',
             page: str='',
             close: bool=False,
             _redirectData: dict=None,
             **params: object
             ) -> tooltilsResponse:
        """
        Send the request to the host \n
        You may pass any kwarg parameters from the `.change()` method as kwargs for single use request data
        """

        self.state:  str = 'Request in Progess'
        self._state: int = 2

        newData = self._setVariables(
            params.get('redirects', self.redirects), params.get('redirect_loops', self.redirect_loops),
            params.get('auth', self.auth), params.get('data', self.data), 
            params.get('headers', self.headers), params.get('cookies', self.cookies), 
            params.get('file_name', self.file_name), params.get('write_binary', self.write_binary), 
            params.get('override', self.override), params.get('encoding', self.encoding), 
            params.get('mask', self.mask), params.get('agent', self.agent), set=False
        )

        redirects      = newData['redirects']
        redirect_loops = newData['redirect_loops']
        auth           = newData['auth']
        data           = newData['data']
        headers        = newData['headers']
        cookies        = newData['cookies']
        file_name      = newData['file_name']
        write_binary   = newData['write_binary']
        override       = newData['override']
        encoding       = newData['encoding']
        mask           = newData['mask']
        agent          = newData['agent']

        if type(method) is str:
            if method.upper() not in ('GET', 'POST', 'PUT', 'DOWNLOAD', 'HEAD', 
                                      'PATCH', 'OPTIONS', 'TRACE', 'DELETE'):
                raise ValueError('Invalid http method \'{}\''.format(method))
            else:
                _method = method = method.upper()
            
            if method == 'DOWNLOAD':
                _method: str = 'GET'
        else:
            raise TypeError('Method must be a valid \'str\' instance')
        
        if type(page) is not str:
            raise TypeError('Page must be a valid \'str\' instance')
        else:
            if page and '/' not in page:
                raise _bm.InvalidRequestURL('The page must include a forward slash at the start if specified')

            try:
                if page[-1] == '/':
                    page = page[:-1]
            except IndexError:
                pass

        try:
            error           = None
            _data, _headers = self._prepare(method, auth, data, headers, cookies, 
                                            mask, agent, close)

            _bm.logger._debug('Sending request', f'requests.{self._caller}().send', self.rID)
            _bm.logger._debug(f'Sending headers: {_headers}', f'requests.{self._caller}().send', self.rID)

            if _data:
                _bm.logger._debug(f'Sending data with length: {len(_data)}', f'requests.{self._caller}().send', self.rID)

            self._req.request(_method, page, _data, _headers)
     
            rdata = self._req.getresponse()

            redirectDir = rdata.getheader('location')

            # get response data here because if close=True then it can't be read later

            resp = tooltilsResponse(rdata, redirectDir if redirectDir else self.host + page,
                                    method, encoding, _headers['User-Agent'], _headers, 
                                    self._clog, self.rID)

            _bm.logger._debug('Obtained request response from server', f'requests.{self._caller}().send', self.rID)

            self.state:  str = str('Connected')
            self._state: int = 1
            
            if close:
                self.close()

            if rdata.status >= 400:
                error = _bm.StatusCodeError(rdata.status, rdata.reason)
            else:
                # test for redirect
                if self.redirects and redirectDir is not None:
                    if _redirectData:
                        if _redirectData['redirected'] >= _redirectData['limit']:
                            error = _bm.RequestRedirectError(limit=_redirectData['redirected'])
                        else:
                            _redirectData['redirected'] += 1
                    
                        if not redirect_loops and redirectDir in _redirectData['redirectList']:
                            error = _bm.RequestRedirectError('Redirect loop detected')
                        else:
                            _redirectData['redirectList'].append(redirectDir)
                    else:
                        _redirectData: dict = {"redirected": 1, "redirectList": [redirectDir],
                                               "limit": self.redirectLimit}
                    
                    if error is None:
                        try:
                            try:
                                redirectDir  = prep_url(redirectDir, https=self.https)
                                redirectHost = redirectDir.split('/')[2]
                                redirectPage = '/'.join(redirectDir.split('/')[3:])
                            except IndexError:
                                redirectHost = prep_url(redirectDir, https=self.https).split('/')[2]
                                redirectPage = ''
                        except (TypeError, _bm.InvalidRequestURL):
                            raise _bm.ActiveRequestError('The request redirected but returned a malformed location header',
                                                         self.host + page)

                        if self.extraLogs:
                            _bm.logger._debug(f'Request was redirected to {redirectHost}', 
                                              f'requests.{self._caller}().send', self.rID)

                        return openConnection(redirectHost, self.port, self.https, self.verify,
                                              redirects, redirect_loops, auth, data, headers, 
                                              cookies, self.cert, file_name, write_binary, override,
                                              self.timeout, encoding, mask, agent, self.proxy,
                                              self.advContext, _clog=self._clog, _redirect=True
                                              ).send(method, redirectPage, close=True, 
                                                     _redirectData=_redirectData)
        except ConnectionResetError:
            error = _bm.ActiveRequestError('The host or client ended the connection without a response', self.host + page)
        except TimeoutError:
            error = _bm.ConnectionTimeoutExpired(timeout=self.timeout)
        except _bm.SSLCertVerificationError:
            error = _bm.SSLCertificateFailed()
        except _bm.SSLError:
            if _bm.connected():
                error = _bm.SSLCertificateFailed()
            else:
                error = _bm.ConnectionError('The connection was forcibly closed by the client')
            
            _bm.logger._debug('tooltils.requests.connected() was called and may update the cache', f'requests.{self._caller}().send', self.rID)
        except OSError:
            error = _bm.ConnectionError('An unknown error occured, check the above stack trace for more info')

        if error:
            _bm.logger._debug('Request failed due to: {}'.format(type(error).__name__),
                              f'requests.{self._caller}().send', self.rID)

            if self.port != 80 and self.port != 443:
                _bm.logger._debug('Request may have failed due to the port not being set to 80 or 443',
                                  f'requests.{self._caller}().send', self.rID)

            raise error

        resp.path       = None
        resp.redirected = True if _redirectData else False

        if method == 'DOWNLOAD':
            if file_name == None:
                try:
                    file_name = page.split('/')[-1]
                except IndexError:
                    file_name = self._host + '.downloadfile'

            if _bm.exists(file_name):
                _bm.remove(file_name)
                
            # test if the file_name is sanitary
                
            try:
                with open(file_name, 'a+') as _f:
                    pass

                _bm.remove(file_name)
            except OSError:
                raise FileNotFoundError('Unable to locate valid file_name descriptor from request url')

            if write_binary:
                with open(file_name, 'wb+') as _f:
                    _f.write(resp.raw)
            else:
                with open(file_name, 'a+') as _f:
                    _f.write(resp.text)

            resp.path = _bm.abspath(file_name)
            
        return resp

class request():
    """Open a single-use connection to a URL"""

    def __init__(self, 
                 url: str,
                 method: str,
                 port: int=(80, 443),
                 https: bool=True,
                 verify: bool=defaultVerificationMethod,
                 redirects: bool=True,
                 redirect_loops: bool=False,
                 auth: tuple=None,
                 data: dict=None,
                 headers: dict=None,
                 cookies: dict=None,
                 cert: str=None, 
                 file_name: str=None,
                 write_binary: bool=False,
                 override: bool=False,
                 timeout: _bm.Union[int, float]=15, 
                 encoding: _bm.Union[str, tuple]=('utf-8', 'ISO-8859-1'),
                 mask: bool=False,
                 agent: str=None,
                 proxy: str=None,
                 advContext: advancedContext=None):
        try:
            self._host: str = url.split('/')[0]
            self._page: str = '/'.join(url.split('/')[1:])
        except IndexError:
            self._host: str = url
            self._page: str = ''
        
        if type(method) is str:
            if method.upper() not in ('GET', 'POST', 'PUT', 'DOWNLOAD', 'HEAD', 
                                      'PATCH', 'OPTIONS', 'TRACE', 'DELETE'):
                raise ValueError('Invalid http method \'{}\''.format(method))
            else:
                self.method = method.upper()
            
            if method.upper() == 'DOWNLOAD':
                self.method: str = 'GET'
        else:
            raise TypeError('Method must be a valid \'str\' instance')

        if port == (80, 443):
            port = 443 if https else 80

        _bm.logger._debug('Setting up http{}/1.1 {} request to <{}:{}>'.format(
                          's' if https else '', self.method, self._host, port), 
                          'requests.request', _bm.newestID)

        self._req = openConnection(self._host, port, https, verify, redirects, redirect_loops,
                                   auth, data, headers, cookies, cert, file_name,
                                   write_binary, override, timeout, encoding, mask, agent,
                                   proxy, advContext, _clog=False)

        self.redirected: bool = False
        self.sent:       bool = False
        self.rID:         int = self._req.rID

        self.url:             str = url
        self.port:            int = port
        self.https:          bool = https
        self.verify:         bool = verify
        self.redirects:      bool = redirects
        self.redirect_loops: bool = redirect_loops
        self.auth:          tuple = auth
        self.data:           dict = data
        self.headers:        dict = headers
        self.cookies:        dict = cookies
        self.cert:            str = cert
        self.file_name:       str = file_name
        self.write_binary:   bool = write_binary
        self.override:       bool = override
        self.mask:           bool = mask
        self.agent:          bool = agent
        self.proxy:           str = proxy
        self.timeout:  _bm.Union[int, float] = timeout
        self.encoding: _bm.Union[str, tuple] = encoding
        self.advContext:     advancedContext = advContext

    def __str__(self):
        return '<{} {} {}>'.format(self.method,
                                   self._host if self.method != 'DOWNLOAD' else self.file_name,
                                   '[Unsent]' if not self.sent else f'[{self._code}]')
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == None:
            return True

    def send(self) -> tooltilsResponse:
        """Send the request"""

        resp = self._req.send(self.method, ('/' + self._page) if self._page else '', close=True)

        self._code:       int = resp.code
        self.redirected: bool = True if resp.redirected else False

        _bm.logger._debug(f'Server replied with [{resp.status_code}]', 'requests.request().send', self.rID)
        _bm.logger._debug('Connection to server has been discarded', 'requests.request().send', self.rID)

        return resp

def get(url: str,
        port: _bm.HTTP_Port=(80, 443),
        https: bool=True,
        verify: bool=defaultVerificationMethod,
        redirects: bool=True,
        redirect_loops: bool=False,
        auth: tuple=None,
        data: dict=None,
        headers: dict=None,
        cookies: dict=None,
        cert: _bm.FileDescriptorOrPath=None, 
        timeout: _bm.Union[int, float]=15, 
        encoding: _bm.Union[str, tuple]=('utf-8', 'ISO-8859-1'),
        mask: bool=False,
        agent: str=None,
        proxy: str=None,
        advContext: advancedContext=None
        ) -> tooltilsResponse:
    """Send a GET request"""

    return request(url, 'GET', port, https, verify, redirects,
                   redirect_loops, auth, data, headers, cookies, 
                   cert, None, None, None, timeout, encoding, 
                   mask, agent, proxy, advContext).send()

def post(url: str,
         port: _bm.HTTP_Port=(80, 443),
         https: bool=True,
         verify: bool=defaultVerificationMethod,
         redirects: bool=True,
         redirect_loops: bool=False,
         auth: tuple=None,
         data: dict=None,
         headers: dict=None,
         cookies: dict=None,
         cert: str=None, 
         timeout: _bm.Union[int, float]=15, 
         encoding: _bm.Union[str, tuple]=('utf-8', 'ISO-8859-1'),
         mask: bool=False,
         agent: str=None,
         proxy: str=None,
         advContext: advancedContext=None
         ) -> tooltilsResponse:
    """Send a POST request"""

    return request(url, 'POST', port, https, verify, redirects,
                   redirect_loops, auth, data, headers, cookies, 
                   cert, None, None, None, timeout, encoding, 
                   mask, agent, proxy, advContext).send()

def download(url: str,
             port: _bm.HTTP_Port=(80, 443),
             https: bool=True,
             verify: bool=defaultVerificationMethod,
             redirects: bool=True,
             redirect_loops: bool=False,
             auth: tuple=None,
             data: dict=None,
             headers: dict=None,
             cookies: dict=None,
             cert: str=None, 
             file_name: str=None,
             write_binary: bool=False,
             override: bool=False,
             timeout: _bm.Union[int, float]=15, 
             encoding: _bm.Union[str, tuple]=('utf-8', 'ISO-8859-1'),
             mask: bool=False,
             agent: str=None,
             proxy: str=None,
             advContext: advancedContext=None
             ) -> tooltilsResponse:
    """Download a file onto the disk"""

    return request(url, 'DOWNLOAD', port, https, verify, redirects,
                   redirect_loops, auth, data, headers, cookies, cert, 
                   file_name, write_binary, override, timeout, encoding, 
                   mask, agent, proxy, advContext).send()

def head(url: str,
         port: _bm.HTTP_Port=(80, 443),
         https: bool=True,
         verify: bool=defaultVerificationMethod,
         redirects: bool=True,
         redirect_loops: bool=False,
         auth: tuple=None,
         data: dict=None,
         headers: dict=None,
         cookies: dict=None,
         cert: str=None, 
         timeout: _bm.Union[int, float]=15, 
         encoding: _bm.Union[str, tuple]=('utf-8', 'ISO-8859-1'),
         mask: bool=False,
         agent: str=None,
         proxy: str=None,
         advContext: advancedContext=None
         ) -> tooltilsResponse:
    """Send a HEAD request"""

    return request(url, 'HEAD', port, https, verify, redirects,
                   redirect_loops, auth, data, headers, cookies, 
                   cert, None, None, None, timeout, encoding, 
                   mask, agent, proxy, advContext).send()

def put(url: str,
        port: _bm.HTTP_Port=(80, 443),
        https: bool=True,
        verify: bool=defaultVerificationMethod,
        redirects: bool=True,
        redirect_loops: bool=False,
        auth: tuple=None,
        data: dict=None,
        headers: dict=None,
        cookies: dict=None,
        cert: str=None,
        timeout: _bm.Union[int, float]=15, 
        encoding: _bm.Union[str, tuple]=('utf-8', 'ISO-8859-1'),
        mask: bool=False,
        agent: str=None,
        proxy: str=None,
        advContext: advancedContext=None
        ) -> tooltilsResponse:
    """Send a PUT request"""

    return request(url, 'PUT', port, https, verify, redirects,
                   redirect_loops, auth, data, headers, cookies, 
                   cert, None, None, None, timeout, encoding, 
                   mask, agent, proxy, advContext).send()

def patch(url: str,
          port: _bm.HTTP_Port=(80, 443),
          https: bool=True,
          verify: bool=defaultVerificationMethod,
          redirects: bool=True,
          redirect_loops: bool=False,
          auth: tuple=None,
          data: dict=None,
          headers: dict=None,
          cookies: dict=None,
          cert: str=None, 
          timeout: _bm.Union[int, float]=15, 
          encoding: _bm.Union[str, tuple]=('utf-8', 'ISO-8859-1'),
          mask: bool=False,
          agent: str=None,
          proxy: str=None,
          advContext: advancedContext=None
          ) -> tooltilsResponse:
    """Send a PATCH request"""

    return request(url, 'PATCH', port, https, verify, redirects,
                   redirect_loops, auth, data, headers, cookies, 
                   cert, None, None, None, timeout, encoding, 
                   mask, agent, proxy, advContext).send()

def options(url: str,
            port: _bm.HTTP_Port=(80, 443),
            https: bool=True,
            verify: bool=defaultVerificationMethod,
            redirects: bool=True,
            redirect_loops: bool=False,
            auth: tuple=None,
            data: dict=None,
            headers: dict=None,
            cookies: dict=None,
            cert: str=None, 
            timeout: _bm.Union[int, float]=15, 
            encoding: _bm.Union[str, tuple]=('utf-8', 'ISO-8859-1'),
            mask: bool=False,
            agent: str=None,
            proxy: str=None,
            advContext: advancedContext=None
            ) -> tooltilsResponse:
    """Send an OPTIONS request"""

    return request(url, 'OPTIONS', port, https, verify, redirects,
                   redirect_loops, auth, data, headers, cookies, 
                   cert, None, None, None, timeout, encoding, 
                   mask, agent, proxy, advContext).send()

def trace(url: str,
          port: _bm.HTTP_Port=(80, 443),
          https: bool=True,
          verify: bool=defaultVerificationMethod,
          redirects: bool=True,
          redirect_loops: bool=False,
          auth: tuple=None,
          headers: dict=None,
          cert: str=None, 
          timeout: _bm.Union[int, float]=15, 
          encoding: _bm.Union[str, tuple]=('utf-8', 'ISO-8859-1'),
          mask: bool=False,
          agent: str=None,
          proxy: str=None,
          advContext: advancedContext=None
          ) -> tooltilsResponse:
    """Send a TRACE request"""

    return request(url, 'TRACE', port, https, verify, redirects,
                   redirect_loops, auth, None, headers, None, 
                   cert, None, None, None, timeout, encoding, 
                   mask, agent, proxy, advContext).send()

def delete(url: str,
           port: _bm.HTTP_Port=(80, 443),
           https: bool=True,
           verify: bool=defaultVerificationMethod,
           redirects: bool=True,
           redirect_loops: bool=False,
           auth: tuple=None,
           data: dict=None,
           headers: dict=None,
           cookies: dict=None,
           cert: str=None, 
           timeout: _bm.Union[int, float]=15, 
           encoding: _bm.Union[str, tuple]=('utf-8', 'ISO-8859-1'),
           mask: bool=False,
           agent: str=None,
           proxy: str=None,
           advContext: advancedContext=None
           ) -> tooltilsResponse:
    """Send a DELETE request"""

    return request(url, 'DELETE', port, https, verify, redirects,
                   redirect_loops, auth, data, headers, cookies, 
                   cert, None, None, None, timeout, encoding, 
                   mask, agent, proxy, advContext).send()
