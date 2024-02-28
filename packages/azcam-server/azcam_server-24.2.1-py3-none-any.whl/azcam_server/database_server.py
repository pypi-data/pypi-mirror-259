"""
Contains the azcam database class for azcamserver.

There is only one instance of this class which is referenced as `azcam.db` and contains
temporary data for this current process.
"""

from azcam.database import AzcamDatabase
from azcam_server.parameters_server import ParametersServer
from azcam_server.cmdserver import CommandServer
from azcam_server.webtools.webserver.fastapi_server import WebServer
from azcam_server.monitor.monitorinterface import AzCamMonitorInterface


class AzcamDatabaseServer(AzcamDatabase):
    """
    The azcam database class.
    """

    parameters: ParametersServer
    """parameters object"""

    cmdserver: CommandServer
    """command server object"""

    webserver: WebServer
    """webserver object"""

    servermode: str
    """server mode"""

    monitor = AzCamMonitorInterface
    """azzcammonitor object"""

    process_name = ""
    """process name for azcammonitor"""
