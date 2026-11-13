# crawlora-openligadb — OpenLigaDB API client for Python

Python client for Crawlora's hosted OpenLigaDB API. It exposes 22 API endpoints covering sports and league discovery, fixtures, match results, standings, scorers, and team match history. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=openligadb-python-homepage); the package does not run a browser or scrape
OpenLigaDB locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
OpenLigaDB or its owners.

## Install

```sh
python -m pip install crawlora-openligadb
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=openligadb-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=openligadb-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_openligadb import OpenLigaDBClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with OpenLigaDBClient(api_key=api_key) as client:
    result_1 = client.leagues(season=2026)
    print(result_1)
    result_2 = client.sports()
    print(result_2)
    result_3 = client.result_types()
    print(result_3)
```

The package also exports `Client` as an alias for `OpenLigaDBClient`. Operation
methods are available directly in snake_case and through the `openligadb`
group. The async package client is `AsyncOpenLigaDBClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-openligadb/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-openligadb/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_openligadb import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.leagues(season=2026)
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-openligadb/blob/main/examples/python.py) for a complete usage example.

## Supported OpenLigaDB API endpoints

This package exposes every route below through direct snake_case methods and the `openligadb` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-openligadb/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/openligadb/current-group` | `openligadb-current-group` | Get the current league matchday |
| `GET` | `/openligadb/current-matchday` | `openligadb-current-matchday` | Get current matchday fixtures and results |
| `GET` | `/openligadb/goal-getters` | `openligadb-goal-getters` | List league season goal-getters |
| `GET` | `/openligadb/groups` | `openligadb-groups` | List league matchdays and rounds |
| `GET` | `/openligadb/last-changed` | `openligadb-last-changed` | Get a matchday's last update time |
| `GET` | `/openligadb/last-match` | `openligadb-last-match` | Get a league's last match |
| `GET` | `/openligadb/last-team-match` | `openligadb-last-team-match` | Get a team's last match in a league |
| `GET` | `/openligadb/league-team-matches` | `openligadb-league-team-matches` | Find a team's matches in one league season |
| `GET` | `/openligadb/leagues` | `openligadb-leagues` | List OpenLigaDB league seasons |
| `GET` | `/openligadb/match` | `openligadb-match` | Get one OpenLigaDB match |
| `GET` | `/openligadb/matchday-matches` | `openligadb-matchday-matches` | List one league matchday |
| `GET` | `/openligadb/matches` | `openligadb-league-matches` | List a league season's matches |
| `GET` | `/openligadb/matches-by-team` | `openligadb-matches-by-team` | Find recent and upcoming matches by team name |
| `GET` | `/openligadb/matches-by-team-id` | `openligadb-matches-by-team-id` | Find recent and upcoming matches by team id |
| `GET` | `/openligadb/next-match` | `openligadb-next-match` | Get a league's next match |
| `GET` | `/openligadb/next-team-match` | `openligadb-next-team-match` | Get a team's next match in a league |
| `GET` | `/openligadb/result-infos` | `openligadb-result-infos` | List result types configured for a league |
| `GET` | `/openligadb/result-types` | `openligadb-result-types` | List global result types |
| `GET` | `/openligadb/sports` | `openligadb-sports` | List OpenLigaDB sports |
| `GET` | `/openligadb/table` | `openligadb-table` | Get a league season's table |
| `GET` | `/openligadb/team-pair-matches` | `openligadb-team-pair-matches` | List matches between two teams |
| `GET` | `/openligadb/teams` | `openligadb-teams` | List teams in a league season |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
