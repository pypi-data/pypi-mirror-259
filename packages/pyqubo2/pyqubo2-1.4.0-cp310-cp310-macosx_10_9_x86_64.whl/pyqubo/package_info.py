# (major, minor, patch, prerelease)

VERSION = (1, 4, 0, "")
__shortversion__ = '.'.join(map(str, VERSION[:3]))
__version__ = '.'.join(map(str, VERSION[:3])) + "".join(VERSION[3:])

__package_name__ = 'pyqubo2'
__contact_names__ = 'MXNXV-ERR'
__contact_emails__ = 'angbymtg@gmail.com'
__homepage__ = 'https://pyqubo.readthedocs.io/en/latest/'
__repository_url__ = 'https://github.com/MXNXV-ERR/pyqubo'
__download_url__ = 'https://github.com/MXNXV-ERR/pyqubo'
__description__ = 'PyQUBO allows you to create QUBOs or Ising models from mathematical expressions with support for Python 3.12'
__license__ = 'Apache 2.0'
__keywords__ = 'QUBO, quantum annealing, annealing machine, ising model, optimization'
