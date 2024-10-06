import binascii
import json
from pathlib import Path

from requests_cache import CachedSession
from rich.console import Console

from ..lib.CatalogDecrypter import CatalogDecrypter
from .CatalogFetcher import catalog_url


class CatalogParser:
    def __init__(self, catalog_url: str | None = None):
        self.root = Path(__file__).parent.parent
        self.console = Console()
        self.catalog_url = catalog_url or None

    @staticmethod
    def _calculate_crc32(file_path: Path) -> int:
        with open(file_path, 'rb') as f:
            return binascii.crc32(f.read()) & 0xFFFFFFFF

    @staticmethod
    def _fetch_bytes(catalog: str, file: str, cache: str) -> bytes:
        with CachedSession(cache, use_temp=True) as session:
            return session.get(f'{catalog}{file}').content

    @staticmethod
    def _load_json(file_path: Path) -> dict:
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def save_json(file_path: Path, data: dict) -> None:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def _fetch_table_bytes(self, catalog: str) -> bytes:
        return self._fetch_bytes(catalog, '/TableBundles/TableCatalog.bytes', 'tablebytes')

    def _fetch_media_bytes(self, catalog: str) -> bytes:
        return self._fetch_bytes(catalog, '/MediaResources/MediaCatalog.bytes', 'mediabytes')

    def _fetch_data(self, url: str, cache_name: str) -> dict:
        with CachedSession(cache_name=cache_name, use_temp=True) as session:
            try:
                return session.get(url).json()

            except (ConnectionError, TimeoutError) as e:
                self.console.log('[bold red]Error: Connection failed.[/bold red]')
                raise SystemExit(1) from e

    def fetch_catalog_url(self) -> str:
        server_api = self.catalog_url if self.catalog_url else catalog_url()
        server_data = self._fetch_data(server_api, 'serverapi')
        return server_data['ConnectionGroups'][0]['OverrideConnectionGroups'][-1]['AddressablesCatalogUrlRoot']

    def fetch_catalogs(self) -> None:
        server_url = self.fetch_catalog_url()

        self.console.print('[cyan]Fetching catalogs...[/cyan]')

        bundle_data = self._fetch_data(f'{server_url}/Android/bundleDownloadInfo.json', 'catalogurl')
        self.save_json(self.root / 'public' / 'jp' / 'bundleDownloadInfo.json', bundle_data)

        table_data = self._fetch_table_bytes(catalog=server_url)
        table_catalog = CatalogDecrypter.from_bytes(table_data, server_url, media=False)
        table_catalog.to_json(self.root / 'public' / 'jp' / 'TableCatalog.json', media=False)

        media_data = self._fetch_media_bytes(catalog=server_url)
        media_catalog = CatalogDecrypter.from_bytes(media_data, server_url, media=True)
        media_catalog.to_json(self.root / 'public' / 'jp' / 'MediaCatalog.json', media=True)

    def get_game_files(self) -> dict:
        server_url = self.fetch_catalog_url()

        bundle_data = self._load_json(self.root / 'public' / 'jp' / 'bundleDownloadInfo.json')
        table_data = self._load_json(self.root / 'public' / 'jp' / 'TableCatalog.json')
        media_data = self._load_json(self.root / 'public' / 'jp' / 'MediaCatalog.json')

        return {
            'AssetBundles': [
                {
                    'url': f'{server_url}/Android/{asset["Name"]}',
                    'crc': asset.get('Crc', 0),
                }
                for asset in bundle_data['BundleFiles']
            ],
            'TableBundles': [
                {
                    'url': f'{server_url}/TableBundles/{key}',
                    'crc': asset.get('crc', 0),
                }
                for key, asset in table_data['TableBundles'].items()
            ],
            'MediaResources': [
                {
                    'url': f'{server_url}/MediaResources/{value["path"]}',
                    'path': value['path'],
                    'crc': value.get('crc', 0),
                }
                for key, value in media_data['MediaResources'].items()
            ],
        }

    def fetch_version(self) -> str:
        server_index = 'https://prod-noticeindex.bluearchiveyostar.com/prod/index.json'
        server_data = self._fetch_data(server_index, 'serverindex')
        return server_data['LatestClientVersion']
