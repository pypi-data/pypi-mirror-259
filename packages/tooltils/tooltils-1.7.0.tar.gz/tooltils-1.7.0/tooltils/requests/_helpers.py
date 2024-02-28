from ssl import create_default_context, get_default_verify_paths, SSLError, CERT_NONE
from urllib.parse import urlencode, urlparse, urlunparse
from socket import create_connection, gethostbyname

from ..info import _loadCache, _loadConfig, _editCache, _deleteCacheKey
from ..errors import InvalidRequestURL
from ..os import getCurrentWifiName


def connected() -> bool:
    caching: bool = bool(_loadConfig('requests')["connectedCaching"])
    wifiName: str = getCurrentWifiName()
    result:  bool = True

    if wifiName == None:
        return False

    if caching:
        configData: dict = _loadConfig('requests')
        cacheData:  dict = _loadCache('requests')

        if cacheData["connectedTimesChecked"] >= configData["connectedCachingCheck"]:
            _editCache('requests', {"connectedTimesChecked": 0})
            _deleteCacheKey('requests', wifiName, 'connectedNetworkList')
        else:
            if wifiName in list(cacheData["connectedNetworkList"].keys()):
                _editCache('requests', {"connectedTimesChecked": cacheData["connectedTimesChecked"] + 1})

                return cacheData["connectedNetworkList"][wifiName]

    try:
        create_connection((gethostbyname('httpbin.org'), 80), 3).close()
    except (TimeoutError, OSError):
        result: bool = False

    if caching:
        _editCache('requests', {wifiName: result}, 'connectedNetworkList')
        _editCache('requests', {"connectedTimesChecked": 1})

    return result

def ctx(verify: bool=True, cert: str=None):
    try:
        if type(cert) is not str and cert is not None:
            raise TypeError('Certificate must be a valid file path')

        if not verify:
            cert = None
        
        if cert == get_default_verify_paths().openssl_cafile:
            cert = None

        ctx = create_default_context(cafile=cert)
        ctx.  set_alpn_protocols(['https/1.1'])
    except (FileNotFoundError, IsADirectoryError, SSLError):
        raise FileNotFoundError('Not a valid certificate file path')
        
    if not verify:         
        ctx.check_hostname = False
        ctx.verify_mode    = CERT_NONE
        ctx.                 set_ciphers('RSA')
        
    return ctx

def _check(url: str, https: bool) -> bool:
    try:
        urls  = urlparse(url)
        valid = (all((urls.scheme, urls.netloc)), urls.scheme, urls.netloc, urls.path, urls)
    except Exception:
        valid = (False, None, None, None, None)

    if not valid[0]:
        if not all((valid[1], valid[2])):
            if valid[3]:
                if not url.startswith('https://') and not url.startswith('http://'):
                    url: str = 'http' + ('s' if https else '') + '://' + url

                    return _check(url, https)

        return (0,) + valid
    elif valid[0]:
        if valid[1] != 'http' and valid[1] != 'https':
            return (1,) + valid

        if '.' not in valid[2]:
            return (2,) + valid

        return (3,) + valid

def prep_url(url: str, 
             data: dict=None,
             https: bool=True,
             order: bool=False
             ) -> str:
    if type(url) is not str:
        raise TypeError('Url must be a valid \'str\' instance')
    elif url == '':
        raise InvalidRequestURL('URL is empty')
    elif ' ' in url:
        url: str = url.replace(' ', '%20')

    if data is None:
        data = {}
    elif type(data) is not dict:
        raise TypeError('Data must be a valid \'dict\' instance')

    if url[0] == '/' or url.startswith('file:///') or url.startswith('C:\\'):
        raise InvalidRequestURL('URL must be a http URI instance, not a file path', url)
    
    valid = _check(url, https)

    if valid[0] == 0:
        if not valid[2] and valid[3]:
            if not url.startswith('https://') and not url.startswith('http://'):
                url: str = 'http' + ('s' if https else '') + '://' + url
        else:
            raise InvalidRequestURL('URL does not contain either a scheme or host, or both', url)
    elif valid[0] == 1:
        raise InvalidRequestURL('An unknown protocol scheme was found', url)
    elif valid[0] == 2:
        raise InvalidRequestURL('URL does not contain a valid host', url)
    elif valid[0] == 3:
        url: str = urlunparse(valid[5])
    
    if url.startswith('https://') and not https:
        url: str = 'http://' + '://'.join(url.split('://')[1:])
    elif url.startswith('http://') and https:
        url: str = 'https://' + '://'.join(url.split('://')[1:])
    
    if url[-1] == '/':
        url: str = url[:-1]

    if data != {}:
        url += '?' + urlencode(data, doseq=order, safe='/')

    return url
