"""Operating system specific methods, information and interaction"""


import tooltils.os.info as info

class _bm:
    from subprocess import run, CalledProcessError, TimeoutExpired, DEVNULL
    from typing import NoReturn, Union, List, Tuple

    from ..errors import (SubprocessExecutionError, SubprocessCodeError, 
                          SubprocessTimeoutExpired, SubprocessLookupNotFound, 
                          SubprocessPermissionError)
    from ..info import _logger

    if info.platform.lower() == 'windows':
        from ctypes import windll, sizeof, byref, Structure, wintypes, POINTER, c_char

        k32 = windll.kernel32
    
_bm.logger = _bm._logger('.os')


if info.platform.lower() == 'windows':
    class _PROCESSENTRY32(_bm.Structure):
        _fields_: list = [
            ('dwSize', _bm.wintypes.DWORD),
            ('cntUsage', _bm.wintypes.DWORD),
            ('th32ProcessID', _bm.wintypes.DWORD),
            ('th32DefaultHeapID', _bm.POINTER(_bm.wintypes.ULONG)),
            ('th32ModuleID', _bm.wintypes.DWORD),
            ('cntThreads', _bm.wintypes.DWORD),
            ('th32ParentProcessID', _bm.wintypes.DWORD),
            ('pcPriClassBase', _bm.wintypes.LONG),
            ('dwFlags', _bm.wintypes.DWORD),
            ('szExeFile', _bm.c_char * 260)
        ]

def exit(details: str='', code: int=1) -> _bm.NoReturn:
    """Print some text and exit the current thread"""

    if type(details) is not str:
        raise TypeError('Details must be a valid \'str\' instance')
    if type(code) is not int:
        raise TypeError('Code must be a valid \'int\' instance')

    if details == '':
        print('', end='')
    else:
        print(details)
    
    _bm.logger._info(f'Exiting the current thread with exit code {code}', 'os.exit')

    _bm.exit(code)

def clear() -> None:
    """Clear the terminal history"""

    if info.platform.lower() == 'windows':
        _bm.run('cls', shell=True)
    else:
        _bm.run('clear')

    _bm.logger._debug('Terminal history was cleared', 'os.clear')

class system():
    """Call a system program and return some information"""

    def __init__(self, 
                 cmds: _bm.Union[str, list, tuple], 
                 shell: bool=False,
                 timeout: _bm.Union[int, float]=10, 
                 check: bool=False,
                 capture: bool=True,
                 print: bool=True):
        error = None

        if cmds == '' and not shell:
            raise ValueError('The call will fail because the input command is an invalid alias')

        if not isinstance(cmds, (str, list, tuple)):
            raise TypeError('Cmds must be a valid \'str\', \'list\' or \'tuple\' instance')
        if not isinstance(timeout, (int, float)):
            raise TypeError('Timeout must be a valid \'int\' or \'float\' instance')
        
        name: str = cmds if type(cmds) is str else ' '.join(cmds)

        try:
            if print:
                self.rdata = _bm.run(cmds, shell=bool(shell), check=bool(check), 
                                     capture_output=bool(capture), timeout=timeout)
            else:
                self.rdata = _bm.run(cmds, shell=bool(shell), check=bool(check), 
                                     stdout=_bm.DEVNULL, timeout=timeout)
        except _bm.CalledProcessError as err:
            error = _bm.SubprocessCodeError(code=err.returncode)
        except _bm.TimeoutExpired:
            error = _bm.SubprocessTimeoutExpired(timeout=self.timeout)
        except FileNotFoundError:
            error = _bm.SubprocessLookupNotFound(name=name)
        except PermissionError:
            error = _bm.SubprocessPermissionError(name=name)
        except Exception:
            error = _bm.SubprocessExecutionError('An unknown process execution error occured, read the above stack trace for info')
        
        _bm.logger._debug(f'Called child program/command with shell: {bool(shell)}', 'os.system')
        
        if error:
            raise error
        
        self.cmds: _bm.Union[list, str, tuple] = cmds
        self.timeout:    _bm.Union[int, float] = timeout
        self.list_text:              list[str] = []
        self.clean_list_text:        list[str] = []

        self.shell:   bool = bool(shell)
        self.check:   bool = bool(check)
        self.capture: bool = bool(capture)
        self.print:   bool = bool(print)
        self.code:     int = self.rdata.returncode
        self.raw:    bytes = b''
        self.text:     str = ''

        if capture:
            self.raw:                 bytes = self.rdata.stdout
            self.text:                  str = self.raw.decode()
            self.list_text:       list[str] = self.text.splitlines()
            self.clean_list_text: list[str] = list(filter(None, self.list_text))

    def __str__(self) -> str:
        return f'<System instance [{hex(id(self))}]>'

def check(cmds: _bm.Union[str, list, tuple], 
          shell: bool=False, 
          timeout: _bm.Union[int, float]=10,
          check: bool=False,
          clean: bool=False,
          listify: bool=True,
          raw: bool=False
          ) -> _bm.Union[str, bytes, _bm.List[str]]:
    """Call a system program and return the output"""

    data = system(cmds, shell, timeout, check)

    if raw:
        return data.raw
    else:
        if listify:
            if clean:
                return data.clean_list_text
            else:
                return data.list_text
        else:
            return data.text

def call(cmds: _bm.Union[str, list, tuple], 
         shell: bool=False, 
         timeout: _bm.Union[int, float]=10,
         check: bool=False,
         print: bool=True
         ) -> int:
    """Call a system program and return the exit code"""
    
    return system(cmds, shell, timeout, check, False, print).code

def pID(name: str, strict: bool=False) -> _bm.Union[_bm.Tuple[int], None]:
    """Get the process ID of an app or binary by name"""

    if type(name) is not str:
        raise TypeError('Name must be a valid \'str\' instance')
    elif len(name) == 0:
        raise ValueError('Invalid name')

    if info.platform.lower() in ('macos', 'linux'):
        ids: list = [int(i) for i in check(['pgrep', '-x' if strict else '-i', name])]
        #ids: list = [int(i) for i in check(f'ps -ax | awk \'/[{name[0]}]{name[1:]}/' + '{print $1}\'', True)]

    elif info.platform.lower() == 'windows':
        snapshot  = _bm.k32.CreateToolhelp32Snapshot(0x2, 0)
        ids: list = []

        if snapshot != -1:
            procEntry = _PROCESSENTRY32()
            procEntry.dwSize = _bm.sizeof(_PROCESSENTRY32)

            if _bm.k32.Process32First(snapshot, _bm.byref(procEntry)):
                while _bm.k32.Process32Next(snapshot, _bm.byref(procEntry)):
                    entryName: str = procEntry.szExeFile.decode('utf-8')

                    if strict:
                        for i in ['bat', 'bin', 'cmd', 'com', 'cpl', 'exe', 'gadget', 
                                  'inf1', 'ins', 'inx', 'isu', 'job', 'jse', 'lnk', 
                                  'msc', 'msi', 'msp', 'mst', 'paf', 'pif', 'ps1', 
                                  'reg', 'rgs', 'scr', 'sct', 'shb', 'shs', 'u3p', 
                                  'vb', 'vbe', 'vbs', 'vbscript', 'ws', 'wsf', 'wsh']:
                            if name + '.' + i == entryName:
                                ids.append(int(procEntry.th32ProcessID))
                    elif name.lower() in entryName.lower():
                        ids.append(int(procEntry.th32ProcessID))
        
        _bm.k32.CloseHandle(snapshot)
    else:
        return None

    return tuple(ids)

def getCurrentWifiName() -> _bm.Union[str, None]:
    """Get the currently connected wifi name"""

    if info.platform.lower() == 'macos':
        wifiName = check(['/System/Library/PrivateFrameworks/Apple80211.' +
                          'framework/Versions/Current/Resources/airport', '-I'])
            
        if 'AirPort: Off' in wifiName[0]:
            return None
        else:
            v: int = 0

            for i, it in enumerate(wifiName):
                if it.lstrip()[:4] == 'SSID':
                    v = i

                    break
            
            return wifiName[v].lstrip()[6:]

    elif info.platform.lower() == 'windows':
        data: list = check(['netsh', 'wlan', 'show', 'interfaces'])
        v:     int = 0

        for i, it in enumerate(data):
            if it.lstrip()[:4] == 'SSID':
                v = i

                break

        if v == 0:
            return None
        else:
            return data[v].lstrip()[4:].lstrip()[1:].lstrip()

    elif info.platform.lower() == 'linux':
        data = check(['iwgetid', '-r'])

        return data if data else None

    else:
        return None
