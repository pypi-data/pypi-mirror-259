"""Identifying system information"""

class _bm:
    from subprocess import CalledProcessError, TimeoutExpired, run
    from sys import executable, maxsize, platform, version
    from socket import gethostname
    from typing import Dict, Tuple

    def check(cmd: str, shell: bool=False):
        return _bm.run(cmd, shell=shell, capture_output=True).stdout.decode().splitlines()

macOS_releases: _bm.Dict[str, str] = {
    "10.0":  "Cheetah",
    "10.1":  "Puma",
    "10.2":  "Jaguar",
    "10.3":  "Panther",
    "10.4":  "Tiger",
    "10.5":  "Leopard",
    "10.6":  "Snow Leopard",
    "10.7":  "Lion",
    "10.8":  "Mountain Lion",
    "10.9":  "Mavericks",
    "10.10": "Yosemite",
    "10.11": "El Capitan",
    "10.12": "Sierra",
    "10.13": "High Sierra",
    "10.14": "Mojave",
    "10.15": "Catalina",
    "11":    "Big Sur",
    "12":    "Monterey",
    "13":    "Ventura",
    "14":    "Sonoma"
}
"""List of all current MacOS versions"""

python_version:         str = _bm.version.split('(')[0].strip()
"""Current Python interpreter version"""
name:                   str = _bm.gethostname()
"""The network name of computer"""
bitsize                     = 64 if (_bm.maxsize > 2 ** 32) else 32
"""The bit limit of the current Python interpreter"""
interpreter:            str = _bm.executable
"""Location of current Python interpreter"""

_st = _bm.platform.startswith
if _st('linux'):
    _tplatform = _tdplatform = 'Linux'
elif _st('win'):
    _tplatform = _tdplatform = 'Windows'
elif _st('cygwin'):
    _tplatform, _tdplatform = 'Windows', 'Cygwin'
elif _st('msys'):
    _tplatform, _tdplatform = 'Windows', 'MSYS2'
elif _st('darwin'):
    _tplatform, _tdplatform = 'MacOS', 'Darwin'
elif _st('os2'):
    _tplatform = _tdplatform = 'OS2'
elif _st('risc'):
    _tplatform, _tdplatform = 'Linux', 'RiscOS'
elif _st('athe'):
    _tplatform, _tdplatform = 'Linux', 'AtheOS'
elif _st('freebsd'):
    _tplatform, _tdplatform = 'BSD', 'FreeBSD'
elif _st('openbsd'):
    _tplatform, _tdplatform = 'BSD', 'OpenBSD'
elif _st('aix'):
    _tplatform = _tdplatform = 'AIX'
else:
    _tplatform = _tdplatform = _bm.platform

platform:          str = _tplatform
"""Name of current operating system"""
detailed_platform: str = _tdplatform
"""Detailed name of current operating system"""

if platform.lower() == 'macos':
    _tpver: list = [_bm.check(['sw_vers', '-productVersion'])[0]]

    if len(_tpver[0].split('.')) > 1:
        if _tpver[0][:2] in ('11', '12', '13', '14'):
            _tpver.append(macOS_releases[_tpver[0][:2]])
        else:
            _tpver.append(macOS_releases['.'.join(_tpver[0].split('.')[:2])])
    else:
        _tpver.append(macOS_releases[_tpver[0]])
    
    _tarch:     str = _bm.check('arch')[0]
    _tsysinfo: list = list(filter(None, _bm.check(['system_profiler', 'SPHardwareDataType'])))
    _tmodel:    str = _tsysinfo[2].split(': ')[1]
    _tcpu:      str = _tsysinfo[5].split(': ')[1]
    _tcores:    int = int(_tsysinfo[6].split(': ')[1].split(' (')[0])
    _tram:      str = _tsysinfo[7].split(': ')[1]
    if 'GB' in _tram:
        _tram: int = int(_tram.split(' ')[0]) * 1024
    else:
        _tram: int = int(_tram.split(' ')[0])
    _tmanufacturer:  str = 'Apple Inc.'
    _tserial_number: str = _tsysinfo[10].split(': ')[1]
    _tboot_drive:    str = _bm.check(['bless', '--info', '--getBoot'])[0]

elif platform.lower() == 'windows':
    def _wmic(*cmds: tuple) -> str:
        return [i.strip() for i in _bm.check('wmic ' + cmds[0] + ' get ' + cmds[1])][2]

    _tcpu:           str = _wmic('cpu', 'name')
    _tcores:         str = _wmic('cpu', 'NumberOfCores')
    _tserial_number: str = _wmic('bios', 'SerialNumber')
    _tarch:          str = _wmic('os', 'OSArchitecture').replace('Processor', '').strip()

    _tsysinfo: list = list(filter(None, _bm.check('systeminfo')))

    _tversion:      str = _tsysinfo[2]
    _tmanufacturer: str = _tsysinfo[11]
    _tmodel:        str = _tsysinfo[12]
    _tboot_drive:   str = _tsysinfo[19]
    _tram:          str = _tsysinfo[23]

    for i in ['_tversion', '_tmanufacturer', '_tmodel', '_tboot_drive', '_tram']:
        locals()[i] = locals()[i].split(': ')[1].strip()

    _tpver:  str = _tversion.split(' ')[0]
    _tpver: list = [_tpver.split('.')[0], _tpver]
    _tram:   int = int(_tram.split(' ')[0].replace(',', ''))
    
elif platform.lower() == 'linux':
    _tcpu:      str = _bm.check('lscpu | grep \'Model:\'', True)[0].split(':')[1].strip()
    _tarch:     str = _bm.check('arch')[0]
    _tsysinfo: list = _bm.check(['cat', '/etc/os-release'])
    _tpver:    list = [_tsysinfo[3].split('"')[1].split(' ')[0], _tsysinfo[1].split('"')[1]]
    _tmodel:    str = _bm.check(['cat', '/sys/devices/virtual/dmi/id/product_name'])[0]
    _tcores:    int = _bm.check('lscpu | grep \'Core(s) per socket:\'', True)[0].split(':')[1].strip()
    _tram:      int = round(int(_bm.check('cat /proc/meminfo | grep \'MemTotal:\'', True)[0].split(':')[1].strip().split(' ')[0]) / 1000)
    _tmanufacturer:  str = _bm.check(['cat', '/sys/devices/virtual/dmi/id/sys_vendor'])[0]
    _tserial_number: str = ''
    _tboot_drive:    str = _bm.check('df /boot | grep -Eo \'/dev/[^ ]+\'', True)[0]

    _bm.logger.warning('Serial_number property is unobtainable on Linux', 
                       'os.info.__main__')

else:
    _tcpu:   str = ''
    _tarch:  str = ''
    _tpver: list = []
    _tmodel: str = ''
    _tcores: int = 0
    _tram:   int = 0
    _tmanufacturer:  str = ''
    _tserial_number: str = ''
    _tboot_drive:    str = ''

cpu:                     str = str(_tcpu)
"""Name of the currently in use cpu of your computer"""
arch:                    str = str(_tarch)
"""Architecture of your computer"""
platform_version: _bm.Tuple[str] = tuple([str(i) for i in _tpver])
"""Version number and or name of current OS"""
model:                   str = str(_tmodel)
"""The model or manufacturer of your computer"""
cores:                   int = int(_tcores)
"""The amount of cores in your computer cpu"""
ram:                     int = int(_tram)
"""The amount of ram in megabytes in your computer"""
manufacturer:            str = str(_tmanufacturer)
"""The organisation or company that created your computer"""
serial_number:           str = str(_tserial_number)
"""The identifiable code or tag string of your computer"""
boot_drive:              str = str(_tboot_drive)
"""The location of the boot drive currently being used on your computer"""


for i in ('_bm', '_st', '_tcpu', '_tarch', '_tpver',
          '_tplatform', '_tdplatform', '_tmodel',
          '_tcores', '_tram', '_tserial_number',
          '_tboot_drive', '_tmanufacturer',
          '_tsysinfo', '_tversion', '_wmic', 'i'):
    try:
        del globals()[i]
    except KeyError:
        continue
