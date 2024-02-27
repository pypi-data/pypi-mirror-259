import logging
import subprocess

from pathlib import Path

import psutil
import pytest

from .addon import mitm_log
from .system_proxy import set_proxy

logger = logging.getLogger(__name__)


class MitmProxyManager:
    def __init__(self):
        self._mitmproxy_process = None
        self._addon_file = Path(__file__).parent / 'addon.py'

    @staticmethod
    def _kill_existing_mitmproxy_processes():
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == 'mitmdump.exe':
                proc.terminate()
                proc.wait()

    def _start_mitmproxy(self, url_filter):
        self._kill_existing_mitmproxy_processes()
        set_proxy(enable_proxy=True, proxy_address="http://127.0.0.1:8080")
        mitmproxy_command = ['mitmdump', '-s', self._addon_file, '-q', '--set', f'url_filter={url_filter}']
        # 启动mitmproxy
        logger.debug("启动mitmproxy")
        self._mitmproxy_process = subprocess.Popen(mitmproxy_command)

    def _stop_mitmproxy(self):
        self._mitmproxy_process.terminate()
        self._mitmproxy_process.wait()
        set_proxy(enable_proxy=False)

    @staticmethod
    def get_urls():
        with open(mitm_log, 'r') as f:
            urls = [line.strip() for line in f.readlines()]
            return urls


def pytest_addoption(parser):
    parser.addini("mitm_url_filter", help="Filter for URLs in mitmproxy tests.")
    parser.addoption(
        "--mitm-url-filter",
        action="store",
        default=None,
        help="Filter for URLs in mitmproxy tests.",
    )


@pytest.fixture
def mitmdump_proxy(request):
    """启用mitmdump抓取数据"""
    mitm_url_filter = request.config.getoption("mitm_url_filter") or request.config.getini("mitm_url_filter")
    # print(f"{mitm_url_filter=}")
    assert bool(mitm_url_filter) is True, "使用fixture需要配置mitm_url_filter参数"
    manager = MitmProxyManager()
    manager._start_mitmproxy(url_filter=mitm_url_filter)

    def finalize():
        manager._stop_mitmproxy()

    request.addfinalizer(finalize)
    return manager
