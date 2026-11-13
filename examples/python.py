import os

from crawlora_openligadb import OpenLigaDBClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with OpenLigaDBClient(api_key=api_key) as client:
    leagues = client.leagues(season=2026)
    print('leagues', leagues)
    sports = client.sports()
    print('sports', sports)
    result_types = client.result_types()
    print('result_types', result_types)
