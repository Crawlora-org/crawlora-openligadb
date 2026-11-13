"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class OpenLigaDBClient(CrawloraClient):
    """Synchronous OpenLigaDB API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-openligadb-python/0.1.0')
        super().__init__(*args, **kwargs)

    def current_group(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-current-group', params, response_type=response_type, timeout=timeout, headers=headers)

    def current_matchday(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-current-matchday', params, response_type=response_type, timeout=timeout, headers=headers)

    def goal_getters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-goal-getters', params, response_type=response_type, timeout=timeout, headers=headers)

    def groups(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-groups', params, response_type=response_type, timeout=timeout, headers=headers)

    def last_changed(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-last-changed', params, response_type=response_type, timeout=timeout, headers=headers)

    def last_match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-last-match', params, response_type=response_type, timeout=timeout, headers=headers)

    def last_team_match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-last-team-match', params, response_type=response_type, timeout=timeout, headers=headers)

    def league_team_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-league-team-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def leagues(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-leagues', params, response_type=response_type, timeout=timeout, headers=headers)

    def match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-match', params, response_type=response_type, timeout=timeout, headers=headers)

    def matchday_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-matchday-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def league_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-league-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def matches_by_team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-matches-by-team', params, response_type=response_type, timeout=timeout, headers=headers)

    def matches_by_team_id(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-matches-by-team-id', params, response_type=response_type, timeout=timeout, headers=headers)

    def next_match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-next-match', params, response_type=response_type, timeout=timeout, headers=headers)

    def next_team_match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-next-team-match', params, response_type=response_type, timeout=timeout, headers=headers)

    def result_infos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-result-infos', params, response_type=response_type, timeout=timeout, headers=headers)

    def result_types(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-result-types', params, response_type=response_type, timeout=timeout, headers=headers)

    def sports(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-sports', params, response_type=response_type, timeout=timeout, headers=headers)

    def table(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-table', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_pair_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-team-pair-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('openligadb-teams', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncOpenLigaDBClient(AsyncCrawloraClient):
    """Asynchronous OpenLigaDB API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-openligadb-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def current_group(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-current-group', params, response_type=response_type, timeout=timeout, headers=headers)

    async def current_matchday(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-current-matchday', params, response_type=response_type, timeout=timeout, headers=headers)

    async def goal_getters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-goal-getters', params, response_type=response_type, timeout=timeout, headers=headers)

    async def groups(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-groups', params, response_type=response_type, timeout=timeout, headers=headers)

    async def last_changed(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-last-changed', params, response_type=response_type, timeout=timeout, headers=headers)

    async def last_match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-last-match', params, response_type=response_type, timeout=timeout, headers=headers)

    async def last_team_match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-last-team-match', params, response_type=response_type, timeout=timeout, headers=headers)

    async def league_team_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-league-team-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def leagues(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-leagues', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-match', params, response_type=response_type, timeout=timeout, headers=headers)

    async def matchday_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-matchday-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def league_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-league-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def matches_by_team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-matches-by-team', params, response_type=response_type, timeout=timeout, headers=headers)

    async def matches_by_team_id(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-matches-by-team-id', params, response_type=response_type, timeout=timeout, headers=headers)

    async def next_match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-next-match', params, response_type=response_type, timeout=timeout, headers=headers)

    async def next_team_match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-next-team-match', params, response_type=response_type, timeout=timeout, headers=headers)

    async def result_infos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-result-infos', params, response_type=response_type, timeout=timeout, headers=headers)

    async def result_types(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-result-types', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sports(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-sports', params, response_type=response_type, timeout=timeout, headers=headers)

    async def table(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-table', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_pair_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-team-pair-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('openligadb-teams', params, response_type=response_type, timeout=timeout, headers=headers)
