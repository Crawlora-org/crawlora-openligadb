from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelOpenligadbListResponseDoc = TypedDict('ModelOpenligadbListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelOpenligadbListSourceDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelOpenligadbListSourceDataDoc = TypedDict('ModelOpenligadbListSourceDataDoc', {
    'attribution': NotRequired[str],
    'data': NotRequired[list[dict[str, Any]]],
    'fetched_at': NotRequired[str],
    'source_license': NotRequired[str],
    'source_license_url': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelOpenligadbObjectResponseDoc = TypedDict('ModelOpenligadbObjectResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelOpenligadbObjectSourceDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelOpenligadbObjectSourceDataDoc = TypedDict('ModelOpenligadbObjectSourceDataDoc', {
    'attribution': NotRequired[str],
    'data': NotRequired[dict[str, Any]],
    'fetched_at': NotRequired[str],
    'source_license': NotRequired[str],
    'source_license_url': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelOpenligadbStringResponseDoc = TypedDict('ModelOpenligadbStringResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelOpenligadbStringSourceDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelOpenligadbStringSourceDataDoc = TypedDict('ModelOpenligadbStringSourceDataDoc', {
    'attribution': NotRequired[str],
    'data': NotRequired[str],
    'fetched_at': NotRequired[str],
    'source_license': NotRequired[str],
    'source_license_url': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

OpenligadbCurrentGroupResponse = ModelOpenligadbObjectResponseDoc
OpenligadbCurrentGroupParams = TypedDict('OpenligadbCurrentGroupParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbCurrentMatchdayResponse = ModelOpenligadbListResponseDoc
OpenligadbCurrentMatchdayParams = TypedDict('OpenligadbCurrentMatchdayParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbGoalGettersResponse = ModelOpenligadbListResponseDoc
OpenligadbGoalGettersParams = TypedDict('OpenligadbGoalGettersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbGroupsResponse = ModelOpenligadbListResponseDoc
OpenligadbGroupsParams = TypedDict('OpenligadbGroupsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbLastChangedResponse = ModelOpenligadbStringResponseDoc
OpenligadbLastChangedParams = TypedDict('OpenligadbLastChangedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_shortcut': Required[str],
    'season': Required[int],
    'group_order_id': Required[int],
}, total=False)

OpenligadbLastMatchResponse = ModelOpenligadbObjectResponseDoc
OpenligadbLastMatchParams = TypedDict('OpenligadbLastMatchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbLastTeamMatchResponse = ModelOpenligadbObjectResponseDoc
OpenligadbLastTeamMatchParams = TypedDict('OpenligadbLastTeamMatchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[int],
    'team_id': Required[int],
}, total=False)

OpenligadbLeagueTeamMatchesResponse = ModelOpenligadbListResponseDoc
OpenligadbLeagueTeamMatchesParams = TypedDict('OpenligadbLeagueTeamMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_shortcut': Required[str],
    'season': Required[int],
    'team_filter': Required[str],
}, total=False)

OpenligadbLeaguesResponse = ModelOpenligadbListResponseDoc
OpenligadbLeaguesParams = TypedDict('OpenligadbLeaguesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'season': NotRequired[int],
}, total=False)

OpenligadbMatchResponse = ModelOpenligadbObjectResponseDoc
OpenligadbMatchParams = TypedDict('OpenligadbMatchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'match_id': Required[int],
}, total=False)

OpenligadbMatchdayMatchesResponse = ModelOpenligadbListResponseDoc
OpenligadbMatchdayMatchesParams = TypedDict('OpenligadbMatchdayMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_shortcut': Required[str],
    'season': Required[int],
    'group_order_id': Required[int],
}, total=False)

OpenligadbLeagueMatchesResponse = ModelOpenligadbListResponseDoc
OpenligadbLeagueMatchesParams = TypedDict('OpenligadbLeagueMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbMatchesByTeamResponse = ModelOpenligadbListResponseDoc
OpenligadbMatchesByTeamParams = TypedDict('OpenligadbMatchesByTeamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_filter': Required[str],
    'weeks_past': Required[int],
    'weeks_future': Required[int],
}, total=False)

OpenligadbMatchesByTeamIdResponse = ModelOpenligadbListResponseDoc
OpenligadbMatchesByTeamIdParams = TypedDict('OpenligadbMatchesByTeamIdParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
    'weeks_past': Required[int],
    'weeks_future': Required[int],
}, total=False)

OpenligadbNextMatchResponse = ModelOpenligadbObjectResponseDoc
OpenligadbNextMatchParams = TypedDict('OpenligadbNextMatchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbNextTeamMatchResponse = ModelOpenligadbObjectResponseDoc
OpenligadbNextTeamMatchParams = TypedDict('OpenligadbNextTeamMatchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[int],
    'team_id': Required[int],
}, total=False)

OpenligadbResultInfosResponse = ModelOpenligadbListResponseDoc
OpenligadbResultInfosParams = TypedDict('OpenligadbResultInfosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[int],
}, total=False)

OpenligadbResultTypesResponse = ModelOpenligadbListResponseDoc
OpenligadbResultTypesParams = TypedDict('OpenligadbResultTypesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

OpenligadbSportsResponse = ModelOpenligadbListResponseDoc
OpenligadbSportsParams = TypedDict('OpenligadbSportsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

OpenligadbTableResponse = ModelOpenligadbListResponseDoc
OpenligadbTableParams = TypedDict('OpenligadbTableParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbTeamPairMatchesResponse = ModelOpenligadbListResponseDoc
OpenligadbTeamPairMatchesParams = TypedDict('OpenligadbTeamPairMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id_1': Required[int],
    'team_id_2': Required[int],
}, total=False)

OpenligadbTeamsResponse = ModelOpenligadbListResponseDoc
OpenligadbTeamsParams = TypedDict('OpenligadbTeamsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

class OpenligadbGroup:
    @overload
    def current_group(self, **params: Unpack[OpenligadbCurrentGroupStreamParams]) -> BinaryIO: ...
    @overload
    def current_group(self, **params: Unpack[OpenligadbCurrentGroupTextResponseParams]) -> str: ...
    @overload
    def current_group(self, **params: Unpack[OpenligadbCurrentGroupDefaultParams]) -> OpenligadbCurrentGroupResponse: ...
    @overload
    def current_matchday(self, **params: Unpack[OpenligadbCurrentMatchdayStreamParams]) -> BinaryIO: ...
    @overload
    def current_matchday(self, **params: Unpack[OpenligadbCurrentMatchdayTextResponseParams]) -> str: ...
    @overload
    def current_matchday(self, **params: Unpack[OpenligadbCurrentMatchdayDefaultParams]) -> OpenligadbCurrentMatchdayResponse: ...
    @overload
    def goal_getters(self, **params: Unpack[OpenligadbGoalGettersStreamParams]) -> BinaryIO: ...
    @overload
    def goal_getters(self, **params: Unpack[OpenligadbGoalGettersTextResponseParams]) -> str: ...
    @overload
    def goal_getters(self, **params: Unpack[OpenligadbGoalGettersDefaultParams]) -> OpenligadbGoalGettersResponse: ...
    @overload
    def groups(self, **params: Unpack[OpenligadbGroupsStreamParams]) -> BinaryIO: ...
    @overload
    def groups(self, **params: Unpack[OpenligadbGroupsTextResponseParams]) -> str: ...
    @overload
    def groups(self, **params: Unpack[OpenligadbGroupsDefaultParams]) -> OpenligadbGroupsResponse: ...
    @overload
    def last_changed(self, **params: Unpack[OpenligadbLastChangedStreamParams]) -> BinaryIO: ...
    @overload
    def last_changed(self, **params: Unpack[OpenligadbLastChangedTextResponseParams]) -> str: ...
    @overload
    def last_changed(self, **params: Unpack[OpenligadbLastChangedDefaultParams]) -> OpenligadbLastChangedResponse: ...
    @overload
    def last_match(self, **params: Unpack[OpenligadbLastMatchStreamParams]) -> BinaryIO: ...
    @overload
    def last_match(self, **params: Unpack[OpenligadbLastMatchTextResponseParams]) -> str: ...
    @overload
    def last_match(self, **params: Unpack[OpenligadbLastMatchDefaultParams]) -> OpenligadbLastMatchResponse: ...
    @overload
    def last_team_match(self, **params: Unpack[OpenligadbLastTeamMatchStreamParams]) -> BinaryIO: ...
    @overload
    def last_team_match(self, **params: Unpack[OpenligadbLastTeamMatchTextResponseParams]) -> str: ...
    @overload
    def last_team_match(self, **params: Unpack[OpenligadbLastTeamMatchDefaultParams]) -> OpenligadbLastTeamMatchResponse: ...
    @overload
    def league_team_matches(self, **params: Unpack[OpenligadbLeagueTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def league_team_matches(self, **params: Unpack[OpenligadbLeagueTeamMatchesTextResponseParams]) -> str: ...
    @overload
    def league_team_matches(self, **params: Unpack[OpenligadbLeagueTeamMatchesDefaultParams]) -> OpenligadbLeagueTeamMatchesResponse: ...
    @overload
    def leagues(self, **params: Unpack[OpenligadbLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    def leagues(self, **params: Unpack[OpenligadbLeaguesTextResponseParams]) -> str: ...
    @overload
    def leagues(self, **params: Unpack[OpenligadbLeaguesDefaultParams]) -> OpenligadbLeaguesResponse: ...
    @overload
    def match(self, **params: Unpack[OpenligadbMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[OpenligadbMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[OpenligadbMatchDefaultParams]) -> OpenligadbMatchResponse: ...
    @overload
    def matchday_matches(self, **params: Unpack[OpenligadbMatchdayMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def matchday_matches(self, **params: Unpack[OpenligadbMatchdayMatchesTextResponseParams]) -> str: ...
    @overload
    def matchday_matches(self, **params: Unpack[OpenligadbMatchdayMatchesDefaultParams]) -> OpenligadbMatchdayMatchesResponse: ...
    @overload
    def league_matches(self, **params: Unpack[OpenligadbLeagueMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def league_matches(self, **params: Unpack[OpenligadbLeagueMatchesTextResponseParams]) -> str: ...
    @overload
    def league_matches(self, **params: Unpack[OpenligadbLeagueMatchesDefaultParams]) -> OpenligadbLeagueMatchesResponse: ...
    @overload
    def matches_by_team(self, **params: Unpack[OpenligadbMatchesByTeamStreamParams]) -> BinaryIO: ...
    @overload
    def matches_by_team(self, **params: Unpack[OpenligadbMatchesByTeamTextResponseParams]) -> str: ...
    @overload
    def matches_by_team(self, **params: Unpack[OpenligadbMatchesByTeamDefaultParams]) -> OpenligadbMatchesByTeamResponse: ...
    @overload
    def matches_by_team_id(self, **params: Unpack[OpenligadbMatchesByTeamIdStreamParams]) -> BinaryIO: ...
    @overload
    def matches_by_team_id(self, **params: Unpack[OpenligadbMatchesByTeamIdTextResponseParams]) -> str: ...
    @overload
    def matches_by_team_id(self, **params: Unpack[OpenligadbMatchesByTeamIdDefaultParams]) -> OpenligadbMatchesByTeamIdResponse: ...
    @overload
    def next_match(self, **params: Unpack[OpenligadbNextMatchStreamParams]) -> BinaryIO: ...
    @overload
    def next_match(self, **params: Unpack[OpenligadbNextMatchTextResponseParams]) -> str: ...
    @overload
    def next_match(self, **params: Unpack[OpenligadbNextMatchDefaultParams]) -> OpenligadbNextMatchResponse: ...
    @overload
    def next_team_match(self, **params: Unpack[OpenligadbNextTeamMatchStreamParams]) -> BinaryIO: ...
    @overload
    def next_team_match(self, **params: Unpack[OpenligadbNextTeamMatchTextResponseParams]) -> str: ...
    @overload
    def next_team_match(self, **params: Unpack[OpenligadbNextTeamMatchDefaultParams]) -> OpenligadbNextTeamMatchResponse: ...
    @overload
    def result_infos(self, **params: Unpack[OpenligadbResultInfosStreamParams]) -> BinaryIO: ...
    @overload
    def result_infos(self, **params: Unpack[OpenligadbResultInfosTextResponseParams]) -> str: ...
    @overload
    def result_infos(self, **params: Unpack[OpenligadbResultInfosDefaultParams]) -> OpenligadbResultInfosResponse: ...
    @overload
    def result_types(self, **params: Unpack[OpenligadbResultTypesStreamParams]) -> BinaryIO: ...
    @overload
    def result_types(self, **params: Unpack[OpenligadbResultTypesTextResponseParams]) -> str: ...
    @overload
    def result_types(self, **params: Unpack[OpenligadbResultTypesDefaultParams]) -> OpenligadbResultTypesResponse: ...
    @overload
    def sports(self, **params: Unpack[OpenligadbSportsStreamParams]) -> BinaryIO: ...
    @overload
    def sports(self, **params: Unpack[OpenligadbSportsTextResponseParams]) -> str: ...
    @overload
    def sports(self, **params: Unpack[OpenligadbSportsDefaultParams]) -> OpenligadbSportsResponse: ...
    @overload
    def table(self, **params: Unpack[OpenligadbTableStreamParams]) -> BinaryIO: ...
    @overload
    def table(self, **params: Unpack[OpenligadbTableTextResponseParams]) -> str: ...
    @overload
    def table(self, **params: Unpack[OpenligadbTableDefaultParams]) -> OpenligadbTableResponse: ...
    @overload
    def team_pair_matches(self, **params: Unpack[OpenligadbTeamPairMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def team_pair_matches(self, **params: Unpack[OpenligadbTeamPairMatchesTextResponseParams]) -> str: ...
    @overload
    def team_pair_matches(self, **params: Unpack[OpenligadbTeamPairMatchesDefaultParams]) -> OpenligadbTeamPairMatchesResponse: ...
    @overload
    def teams(self, **params: Unpack[OpenligadbTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def teams(self, **params: Unpack[OpenligadbTeamsTextResponseParams]) -> str: ...
    @overload
    def teams(self, **params: Unpack[OpenligadbTeamsDefaultParams]) -> OpenligadbTeamsResponse: ...

OperationId = Literal[
    'openligadb-current-group',
    'openligadb-current-matchday',
    'openligadb-goal-getters',
    'openligadb-groups',
    'openligadb-last-changed',
    'openligadb-last-match',
    'openligadb-last-team-match',
    'openligadb-league-team-matches',
    'openligadb-leagues',
    'openligadb-match',
    'openligadb-matchday-matches',
    'openligadb-league-matches',
    'openligadb-matches-by-team',
    'openligadb-matches-by-team-id',
    'openligadb-next-match',
    'openligadb-next-team-match',
    'openligadb-result-infos',
    'openligadb-result-types',
    'openligadb-sports',
    'openligadb-table',
    'openligadb-team-pair-matches',
    'openligadb-teams',
]

class CrawloraClient:
    openligadb: OpenligadbGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-current-group'],
        params: OpenligadbCurrentGroupParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbCurrentGroupResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-current-matchday'],
        params: OpenligadbCurrentMatchdayParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbCurrentMatchdayResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-goal-getters'],
        params: OpenligadbGoalGettersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbGoalGettersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-groups'],
        params: OpenligadbGroupsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbGroupsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-last-changed'],
        params: OpenligadbLastChangedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbLastChangedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-last-match'],
        params: OpenligadbLastMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbLastMatchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-last-team-match'],
        params: OpenligadbLastTeamMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbLastTeamMatchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-league-team-matches'],
        params: OpenligadbLeagueTeamMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbLeagueTeamMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-leagues'],
        params: OpenligadbLeaguesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbLeaguesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-match'],
        params: OpenligadbMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbMatchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-matchday-matches'],
        params: OpenligadbMatchdayMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbMatchdayMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-league-matches'],
        params: OpenligadbLeagueMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbLeagueMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-matches-by-team'],
        params: OpenligadbMatchesByTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbMatchesByTeamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-matches-by-team-id'],
        params: OpenligadbMatchesByTeamIdParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbMatchesByTeamIdResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-next-match'],
        params: OpenligadbNextMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbNextMatchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-next-team-match'],
        params: OpenligadbNextTeamMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbNextTeamMatchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-result-infos'],
        params: OpenligadbResultInfosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbResultInfosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-result-types'],
        params: OpenligadbResultTypesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbResultTypesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-sports'],
        params: OpenligadbSportsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbSportsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-table'],
        params: OpenligadbTableParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbTableResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-team-pair-matches'],
        params: OpenligadbTeamPairMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbTeamPairMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['openligadb-teams'],
        params: OpenligadbTeamsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbTeamsResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-current-group'],
        params: OpenligadbCurrentGroupParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbCurrentGroupResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-current-matchday'],
        params: OpenligadbCurrentMatchdayParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbCurrentMatchdayResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-goal-getters'],
        params: OpenligadbGoalGettersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbGoalGettersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-groups'],
        params: OpenligadbGroupsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbGroupsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-last-changed'],
        params: OpenligadbLastChangedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbLastChangedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-last-match'],
        params: OpenligadbLastMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbLastMatchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-last-team-match'],
        params: OpenligadbLastTeamMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbLastTeamMatchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-league-team-matches'],
        params: OpenligadbLeagueTeamMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbLeagueTeamMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-leagues'],
        params: OpenligadbLeaguesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbLeaguesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-match'],
        params: OpenligadbMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbMatchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-matchday-matches'],
        params: OpenligadbMatchdayMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbMatchdayMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-league-matches'],
        params: OpenligadbLeagueMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbLeagueMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-matches-by-team'],
        params: OpenligadbMatchesByTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbMatchesByTeamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-matches-by-team-id'],
        params: OpenligadbMatchesByTeamIdParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbMatchesByTeamIdResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-next-match'],
        params: OpenligadbNextMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbNextMatchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-next-team-match'],
        params: OpenligadbNextTeamMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbNextTeamMatchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-result-infos'],
        params: OpenligadbResultInfosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbResultInfosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-result-types'],
        params: OpenligadbResultTypesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbResultTypesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-sports'],
        params: OpenligadbSportsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbSportsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-table'],
        params: OpenligadbTableParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbTableResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-team-pair-matches'],
        params: OpenligadbTeamPairMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbTeamPairMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['openligadb-teams'],
        params: OpenligadbTeamsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpenligadbTeamsResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class OpenLigaDBClient(CrawloraClient):
    def __enter__(self) -> OpenLigaDBClient: ...
    @overload
    def current_group(self, **params: Unpack[OpenligadbCurrentGroupStreamParams]) -> BinaryIO: ...
    @overload
    def current_group(self, **params: Unpack[OpenligadbCurrentGroupTextResponseParams]) -> str: ...
    @overload
    def current_group(self, **params: Unpack[OpenligadbCurrentGroupDefaultParams]) -> OpenligadbCurrentGroupResponse: ...
    @overload
    def current_matchday(self, **params: Unpack[OpenligadbCurrentMatchdayStreamParams]) -> BinaryIO: ...
    @overload
    def current_matchday(self, **params: Unpack[OpenligadbCurrentMatchdayTextResponseParams]) -> str: ...
    @overload
    def current_matchday(self, **params: Unpack[OpenligadbCurrentMatchdayDefaultParams]) -> OpenligadbCurrentMatchdayResponse: ...
    @overload
    def goal_getters(self, **params: Unpack[OpenligadbGoalGettersStreamParams]) -> BinaryIO: ...
    @overload
    def goal_getters(self, **params: Unpack[OpenligadbGoalGettersTextResponseParams]) -> str: ...
    @overload
    def goal_getters(self, **params: Unpack[OpenligadbGoalGettersDefaultParams]) -> OpenligadbGoalGettersResponse: ...
    @overload
    def groups(self, **params: Unpack[OpenligadbGroupsStreamParams]) -> BinaryIO: ...
    @overload
    def groups(self, **params: Unpack[OpenligadbGroupsTextResponseParams]) -> str: ...
    @overload
    def groups(self, **params: Unpack[OpenligadbGroupsDefaultParams]) -> OpenligadbGroupsResponse: ...
    @overload
    def last_changed(self, **params: Unpack[OpenligadbLastChangedStreamParams]) -> BinaryIO: ...
    @overload
    def last_changed(self, **params: Unpack[OpenligadbLastChangedTextResponseParams]) -> str: ...
    @overload
    def last_changed(self, **params: Unpack[OpenligadbLastChangedDefaultParams]) -> OpenligadbLastChangedResponse: ...
    @overload
    def last_match(self, **params: Unpack[OpenligadbLastMatchStreamParams]) -> BinaryIO: ...
    @overload
    def last_match(self, **params: Unpack[OpenligadbLastMatchTextResponseParams]) -> str: ...
    @overload
    def last_match(self, **params: Unpack[OpenligadbLastMatchDefaultParams]) -> OpenligadbLastMatchResponse: ...
    @overload
    def last_team_match(self, **params: Unpack[OpenligadbLastTeamMatchStreamParams]) -> BinaryIO: ...
    @overload
    def last_team_match(self, **params: Unpack[OpenligadbLastTeamMatchTextResponseParams]) -> str: ...
    @overload
    def last_team_match(self, **params: Unpack[OpenligadbLastTeamMatchDefaultParams]) -> OpenligadbLastTeamMatchResponse: ...
    @overload
    def league_team_matches(self, **params: Unpack[OpenligadbLeagueTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def league_team_matches(self, **params: Unpack[OpenligadbLeagueTeamMatchesTextResponseParams]) -> str: ...
    @overload
    def league_team_matches(self, **params: Unpack[OpenligadbLeagueTeamMatchesDefaultParams]) -> OpenligadbLeagueTeamMatchesResponse: ...
    @overload
    def leagues(self, **params: Unpack[OpenligadbLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    def leagues(self, **params: Unpack[OpenligadbLeaguesTextResponseParams]) -> str: ...
    @overload
    def leagues(self, **params: Unpack[OpenligadbLeaguesDefaultParams]) -> OpenligadbLeaguesResponse: ...
    @overload
    def match(self, **params: Unpack[OpenligadbMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[OpenligadbMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[OpenligadbMatchDefaultParams]) -> OpenligadbMatchResponse: ...
    @overload
    def matchday_matches(self, **params: Unpack[OpenligadbMatchdayMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def matchday_matches(self, **params: Unpack[OpenligadbMatchdayMatchesTextResponseParams]) -> str: ...
    @overload
    def matchday_matches(self, **params: Unpack[OpenligadbMatchdayMatchesDefaultParams]) -> OpenligadbMatchdayMatchesResponse: ...
    @overload
    def league_matches(self, **params: Unpack[OpenligadbLeagueMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def league_matches(self, **params: Unpack[OpenligadbLeagueMatchesTextResponseParams]) -> str: ...
    @overload
    def league_matches(self, **params: Unpack[OpenligadbLeagueMatchesDefaultParams]) -> OpenligadbLeagueMatchesResponse: ...
    @overload
    def matches_by_team(self, **params: Unpack[OpenligadbMatchesByTeamStreamParams]) -> BinaryIO: ...
    @overload
    def matches_by_team(self, **params: Unpack[OpenligadbMatchesByTeamTextResponseParams]) -> str: ...
    @overload
    def matches_by_team(self, **params: Unpack[OpenligadbMatchesByTeamDefaultParams]) -> OpenligadbMatchesByTeamResponse: ...
    @overload
    def matches_by_team_id(self, **params: Unpack[OpenligadbMatchesByTeamIdStreamParams]) -> BinaryIO: ...
    @overload
    def matches_by_team_id(self, **params: Unpack[OpenligadbMatchesByTeamIdTextResponseParams]) -> str: ...
    @overload
    def matches_by_team_id(self, **params: Unpack[OpenligadbMatchesByTeamIdDefaultParams]) -> OpenligadbMatchesByTeamIdResponse: ...
    @overload
    def next_match(self, **params: Unpack[OpenligadbNextMatchStreamParams]) -> BinaryIO: ...
    @overload
    def next_match(self, **params: Unpack[OpenligadbNextMatchTextResponseParams]) -> str: ...
    @overload
    def next_match(self, **params: Unpack[OpenligadbNextMatchDefaultParams]) -> OpenligadbNextMatchResponse: ...
    @overload
    def next_team_match(self, **params: Unpack[OpenligadbNextTeamMatchStreamParams]) -> BinaryIO: ...
    @overload
    def next_team_match(self, **params: Unpack[OpenligadbNextTeamMatchTextResponseParams]) -> str: ...
    @overload
    def next_team_match(self, **params: Unpack[OpenligadbNextTeamMatchDefaultParams]) -> OpenligadbNextTeamMatchResponse: ...
    @overload
    def result_infos(self, **params: Unpack[OpenligadbResultInfosStreamParams]) -> BinaryIO: ...
    @overload
    def result_infos(self, **params: Unpack[OpenligadbResultInfosTextResponseParams]) -> str: ...
    @overload
    def result_infos(self, **params: Unpack[OpenligadbResultInfosDefaultParams]) -> OpenligadbResultInfosResponse: ...
    @overload
    def result_types(self, **params: Unpack[OpenligadbResultTypesStreamParams]) -> BinaryIO: ...
    @overload
    def result_types(self, **params: Unpack[OpenligadbResultTypesTextResponseParams]) -> str: ...
    @overload
    def result_types(self, **params: Unpack[OpenligadbResultTypesDefaultParams]) -> OpenligadbResultTypesResponse: ...
    @overload
    def sports(self, **params: Unpack[OpenligadbSportsStreamParams]) -> BinaryIO: ...
    @overload
    def sports(self, **params: Unpack[OpenligadbSportsTextResponseParams]) -> str: ...
    @overload
    def sports(self, **params: Unpack[OpenligadbSportsDefaultParams]) -> OpenligadbSportsResponse: ...
    @overload
    def table(self, **params: Unpack[OpenligadbTableStreamParams]) -> BinaryIO: ...
    @overload
    def table(self, **params: Unpack[OpenligadbTableTextResponseParams]) -> str: ...
    @overload
    def table(self, **params: Unpack[OpenligadbTableDefaultParams]) -> OpenligadbTableResponse: ...
    @overload
    def team_pair_matches(self, **params: Unpack[OpenligadbTeamPairMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def team_pair_matches(self, **params: Unpack[OpenligadbTeamPairMatchesTextResponseParams]) -> str: ...
    @overload
    def team_pair_matches(self, **params: Unpack[OpenligadbTeamPairMatchesDefaultParams]) -> OpenligadbTeamPairMatchesResponse: ...
    @overload
    def teams(self, **params: Unpack[OpenligadbTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def teams(self, **params: Unpack[OpenligadbTeamsTextResponseParams]) -> str: ...
    @overload
    def teams(self, **params: Unpack[OpenligadbTeamsDefaultParams]) -> OpenligadbTeamsResponse: ...

class AsyncOpenLigaDBClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncOpenLigaDBClient: ...
    openligadb: _AsyncOpenligadbGroup
    @overload
    async def current_group(self, **params: Unpack[OpenligadbCurrentGroupStreamParams]) -> BinaryIO: ...
    @overload
    async def current_group(self, **params: Unpack[OpenligadbCurrentGroupTextResponseParams]) -> str: ...
    @overload
    async def current_group(self, **params: Unpack[OpenligadbCurrentGroupDefaultParams]) -> OpenligadbCurrentGroupResponse: ...
    @overload
    async def current_matchday(self, **params: Unpack[OpenligadbCurrentMatchdayStreamParams]) -> BinaryIO: ...
    @overload
    async def current_matchday(self, **params: Unpack[OpenligadbCurrentMatchdayTextResponseParams]) -> str: ...
    @overload
    async def current_matchday(self, **params: Unpack[OpenligadbCurrentMatchdayDefaultParams]) -> OpenligadbCurrentMatchdayResponse: ...
    @overload
    async def goal_getters(self, **params: Unpack[OpenligadbGoalGettersStreamParams]) -> BinaryIO: ...
    @overload
    async def goal_getters(self, **params: Unpack[OpenligadbGoalGettersTextResponseParams]) -> str: ...
    @overload
    async def goal_getters(self, **params: Unpack[OpenligadbGoalGettersDefaultParams]) -> OpenligadbGoalGettersResponse: ...
    @overload
    async def groups(self, **params: Unpack[OpenligadbGroupsStreamParams]) -> BinaryIO: ...
    @overload
    async def groups(self, **params: Unpack[OpenligadbGroupsTextResponseParams]) -> str: ...
    @overload
    async def groups(self, **params: Unpack[OpenligadbGroupsDefaultParams]) -> OpenligadbGroupsResponse: ...
    @overload
    async def last_changed(self, **params: Unpack[OpenligadbLastChangedStreamParams]) -> BinaryIO: ...
    @overload
    async def last_changed(self, **params: Unpack[OpenligadbLastChangedTextResponseParams]) -> str: ...
    @overload
    async def last_changed(self, **params: Unpack[OpenligadbLastChangedDefaultParams]) -> OpenligadbLastChangedResponse: ...
    @overload
    async def last_match(self, **params: Unpack[OpenligadbLastMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def last_match(self, **params: Unpack[OpenligadbLastMatchTextResponseParams]) -> str: ...
    @overload
    async def last_match(self, **params: Unpack[OpenligadbLastMatchDefaultParams]) -> OpenligadbLastMatchResponse: ...
    @overload
    async def last_team_match(self, **params: Unpack[OpenligadbLastTeamMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def last_team_match(self, **params: Unpack[OpenligadbLastTeamMatchTextResponseParams]) -> str: ...
    @overload
    async def last_team_match(self, **params: Unpack[OpenligadbLastTeamMatchDefaultParams]) -> OpenligadbLastTeamMatchResponse: ...
    @overload
    async def league_team_matches(self, **params: Unpack[OpenligadbLeagueTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def league_team_matches(self, **params: Unpack[OpenligadbLeagueTeamMatchesTextResponseParams]) -> str: ...
    @overload
    async def league_team_matches(self, **params: Unpack[OpenligadbLeagueTeamMatchesDefaultParams]) -> OpenligadbLeagueTeamMatchesResponse: ...
    @overload
    async def leagues(self, **params: Unpack[OpenligadbLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    async def leagues(self, **params: Unpack[OpenligadbLeaguesTextResponseParams]) -> str: ...
    @overload
    async def leagues(self, **params: Unpack[OpenligadbLeaguesDefaultParams]) -> OpenligadbLeaguesResponse: ...
    @overload
    async def match(self, **params: Unpack[OpenligadbMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[OpenligadbMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[OpenligadbMatchDefaultParams]) -> OpenligadbMatchResponse: ...
    @overload
    async def matchday_matches(self, **params: Unpack[OpenligadbMatchdayMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def matchday_matches(self, **params: Unpack[OpenligadbMatchdayMatchesTextResponseParams]) -> str: ...
    @overload
    async def matchday_matches(self, **params: Unpack[OpenligadbMatchdayMatchesDefaultParams]) -> OpenligadbMatchdayMatchesResponse: ...
    @overload
    async def league_matches(self, **params: Unpack[OpenligadbLeagueMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def league_matches(self, **params: Unpack[OpenligadbLeagueMatchesTextResponseParams]) -> str: ...
    @overload
    async def league_matches(self, **params: Unpack[OpenligadbLeagueMatchesDefaultParams]) -> OpenligadbLeagueMatchesResponse: ...
    @overload
    async def matches_by_team(self, **params: Unpack[OpenligadbMatchesByTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def matches_by_team(self, **params: Unpack[OpenligadbMatchesByTeamTextResponseParams]) -> str: ...
    @overload
    async def matches_by_team(self, **params: Unpack[OpenligadbMatchesByTeamDefaultParams]) -> OpenligadbMatchesByTeamResponse: ...
    @overload
    async def matches_by_team_id(self, **params: Unpack[OpenligadbMatchesByTeamIdStreamParams]) -> BinaryIO: ...
    @overload
    async def matches_by_team_id(self, **params: Unpack[OpenligadbMatchesByTeamIdTextResponseParams]) -> str: ...
    @overload
    async def matches_by_team_id(self, **params: Unpack[OpenligadbMatchesByTeamIdDefaultParams]) -> OpenligadbMatchesByTeamIdResponse: ...
    @overload
    async def next_match(self, **params: Unpack[OpenligadbNextMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def next_match(self, **params: Unpack[OpenligadbNextMatchTextResponseParams]) -> str: ...
    @overload
    async def next_match(self, **params: Unpack[OpenligadbNextMatchDefaultParams]) -> OpenligadbNextMatchResponse: ...
    @overload
    async def next_team_match(self, **params: Unpack[OpenligadbNextTeamMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def next_team_match(self, **params: Unpack[OpenligadbNextTeamMatchTextResponseParams]) -> str: ...
    @overload
    async def next_team_match(self, **params: Unpack[OpenligadbNextTeamMatchDefaultParams]) -> OpenligadbNextTeamMatchResponse: ...
    @overload
    async def result_infos(self, **params: Unpack[OpenligadbResultInfosStreamParams]) -> BinaryIO: ...
    @overload
    async def result_infos(self, **params: Unpack[OpenligadbResultInfosTextResponseParams]) -> str: ...
    @overload
    async def result_infos(self, **params: Unpack[OpenligadbResultInfosDefaultParams]) -> OpenligadbResultInfosResponse: ...
    @overload
    async def result_types(self, **params: Unpack[OpenligadbResultTypesStreamParams]) -> BinaryIO: ...
    @overload
    async def result_types(self, **params: Unpack[OpenligadbResultTypesTextResponseParams]) -> str: ...
    @overload
    async def result_types(self, **params: Unpack[OpenligadbResultTypesDefaultParams]) -> OpenligadbResultTypesResponse: ...
    @overload
    async def sports(self, **params: Unpack[OpenligadbSportsStreamParams]) -> BinaryIO: ...
    @overload
    async def sports(self, **params: Unpack[OpenligadbSportsTextResponseParams]) -> str: ...
    @overload
    async def sports(self, **params: Unpack[OpenligadbSportsDefaultParams]) -> OpenligadbSportsResponse: ...
    @overload
    async def table(self, **params: Unpack[OpenligadbTableStreamParams]) -> BinaryIO: ...
    @overload
    async def table(self, **params: Unpack[OpenligadbTableTextResponseParams]) -> str: ...
    @overload
    async def table(self, **params: Unpack[OpenligadbTableDefaultParams]) -> OpenligadbTableResponse: ...
    @overload
    async def team_pair_matches(self, **params: Unpack[OpenligadbTeamPairMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_pair_matches(self, **params: Unpack[OpenligadbTeamPairMatchesTextResponseParams]) -> str: ...
    @overload
    async def team_pair_matches(self, **params: Unpack[OpenligadbTeamPairMatchesDefaultParams]) -> OpenligadbTeamPairMatchesResponse: ...
    @overload
    async def teams(self, **params: Unpack[OpenligadbTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def teams(self, **params: Unpack[OpenligadbTeamsTextResponseParams]) -> str: ...
    @overload
    async def teams(self, **params: Unpack[OpenligadbTeamsDefaultParams]) -> OpenligadbTeamsResponse: ...

class _AsyncOpenligadbGroup:
    @overload
    async def current_group(self, **params: Unpack[OpenligadbCurrentGroupStreamParams]) -> BinaryIO: ...
    @overload
    async def current_group(self, **params: Unpack[OpenligadbCurrentGroupTextResponseParams]) -> str: ...
    @overload
    async def current_group(self, **params: Unpack[OpenligadbCurrentGroupDefaultParams]) -> OpenligadbCurrentGroupResponse: ...
    @overload
    async def current_matchday(self, **params: Unpack[OpenligadbCurrentMatchdayStreamParams]) -> BinaryIO: ...
    @overload
    async def current_matchday(self, **params: Unpack[OpenligadbCurrentMatchdayTextResponseParams]) -> str: ...
    @overload
    async def current_matchday(self, **params: Unpack[OpenligadbCurrentMatchdayDefaultParams]) -> OpenligadbCurrentMatchdayResponse: ...
    @overload
    async def goal_getters(self, **params: Unpack[OpenligadbGoalGettersStreamParams]) -> BinaryIO: ...
    @overload
    async def goal_getters(self, **params: Unpack[OpenligadbGoalGettersTextResponseParams]) -> str: ...
    @overload
    async def goal_getters(self, **params: Unpack[OpenligadbGoalGettersDefaultParams]) -> OpenligadbGoalGettersResponse: ...
    @overload
    async def groups(self, **params: Unpack[OpenligadbGroupsStreamParams]) -> BinaryIO: ...
    @overload
    async def groups(self, **params: Unpack[OpenligadbGroupsTextResponseParams]) -> str: ...
    @overload
    async def groups(self, **params: Unpack[OpenligadbGroupsDefaultParams]) -> OpenligadbGroupsResponse: ...
    @overload
    async def last_changed(self, **params: Unpack[OpenligadbLastChangedStreamParams]) -> BinaryIO: ...
    @overload
    async def last_changed(self, **params: Unpack[OpenligadbLastChangedTextResponseParams]) -> str: ...
    @overload
    async def last_changed(self, **params: Unpack[OpenligadbLastChangedDefaultParams]) -> OpenligadbLastChangedResponse: ...
    @overload
    async def last_match(self, **params: Unpack[OpenligadbLastMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def last_match(self, **params: Unpack[OpenligadbLastMatchTextResponseParams]) -> str: ...
    @overload
    async def last_match(self, **params: Unpack[OpenligadbLastMatchDefaultParams]) -> OpenligadbLastMatchResponse: ...
    @overload
    async def last_team_match(self, **params: Unpack[OpenligadbLastTeamMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def last_team_match(self, **params: Unpack[OpenligadbLastTeamMatchTextResponseParams]) -> str: ...
    @overload
    async def last_team_match(self, **params: Unpack[OpenligadbLastTeamMatchDefaultParams]) -> OpenligadbLastTeamMatchResponse: ...
    @overload
    async def league_team_matches(self, **params: Unpack[OpenligadbLeagueTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def league_team_matches(self, **params: Unpack[OpenligadbLeagueTeamMatchesTextResponseParams]) -> str: ...
    @overload
    async def league_team_matches(self, **params: Unpack[OpenligadbLeagueTeamMatchesDefaultParams]) -> OpenligadbLeagueTeamMatchesResponse: ...
    @overload
    async def leagues(self, **params: Unpack[OpenligadbLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    async def leagues(self, **params: Unpack[OpenligadbLeaguesTextResponseParams]) -> str: ...
    @overload
    async def leagues(self, **params: Unpack[OpenligadbLeaguesDefaultParams]) -> OpenligadbLeaguesResponse: ...
    @overload
    async def match(self, **params: Unpack[OpenligadbMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[OpenligadbMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[OpenligadbMatchDefaultParams]) -> OpenligadbMatchResponse: ...
    @overload
    async def matchday_matches(self, **params: Unpack[OpenligadbMatchdayMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def matchday_matches(self, **params: Unpack[OpenligadbMatchdayMatchesTextResponseParams]) -> str: ...
    @overload
    async def matchday_matches(self, **params: Unpack[OpenligadbMatchdayMatchesDefaultParams]) -> OpenligadbMatchdayMatchesResponse: ...
    @overload
    async def league_matches(self, **params: Unpack[OpenligadbLeagueMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def league_matches(self, **params: Unpack[OpenligadbLeagueMatchesTextResponseParams]) -> str: ...
    @overload
    async def league_matches(self, **params: Unpack[OpenligadbLeagueMatchesDefaultParams]) -> OpenligadbLeagueMatchesResponse: ...
    @overload
    async def matches_by_team(self, **params: Unpack[OpenligadbMatchesByTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def matches_by_team(self, **params: Unpack[OpenligadbMatchesByTeamTextResponseParams]) -> str: ...
    @overload
    async def matches_by_team(self, **params: Unpack[OpenligadbMatchesByTeamDefaultParams]) -> OpenligadbMatchesByTeamResponse: ...
    @overload
    async def matches_by_team_id(self, **params: Unpack[OpenligadbMatchesByTeamIdStreamParams]) -> BinaryIO: ...
    @overload
    async def matches_by_team_id(self, **params: Unpack[OpenligadbMatchesByTeamIdTextResponseParams]) -> str: ...
    @overload
    async def matches_by_team_id(self, **params: Unpack[OpenligadbMatchesByTeamIdDefaultParams]) -> OpenligadbMatchesByTeamIdResponse: ...
    @overload
    async def next_match(self, **params: Unpack[OpenligadbNextMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def next_match(self, **params: Unpack[OpenligadbNextMatchTextResponseParams]) -> str: ...
    @overload
    async def next_match(self, **params: Unpack[OpenligadbNextMatchDefaultParams]) -> OpenligadbNextMatchResponse: ...
    @overload
    async def next_team_match(self, **params: Unpack[OpenligadbNextTeamMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def next_team_match(self, **params: Unpack[OpenligadbNextTeamMatchTextResponseParams]) -> str: ...
    @overload
    async def next_team_match(self, **params: Unpack[OpenligadbNextTeamMatchDefaultParams]) -> OpenligadbNextTeamMatchResponse: ...
    @overload
    async def result_infos(self, **params: Unpack[OpenligadbResultInfosStreamParams]) -> BinaryIO: ...
    @overload
    async def result_infos(self, **params: Unpack[OpenligadbResultInfosTextResponseParams]) -> str: ...
    @overload
    async def result_infos(self, **params: Unpack[OpenligadbResultInfosDefaultParams]) -> OpenligadbResultInfosResponse: ...
    @overload
    async def result_types(self, **params: Unpack[OpenligadbResultTypesStreamParams]) -> BinaryIO: ...
    @overload
    async def result_types(self, **params: Unpack[OpenligadbResultTypesTextResponseParams]) -> str: ...
    @overload
    async def result_types(self, **params: Unpack[OpenligadbResultTypesDefaultParams]) -> OpenligadbResultTypesResponse: ...
    @overload
    async def sports(self, **params: Unpack[OpenligadbSportsStreamParams]) -> BinaryIO: ...
    @overload
    async def sports(self, **params: Unpack[OpenligadbSportsTextResponseParams]) -> str: ...
    @overload
    async def sports(self, **params: Unpack[OpenligadbSportsDefaultParams]) -> OpenligadbSportsResponse: ...
    @overload
    async def table(self, **params: Unpack[OpenligadbTableStreamParams]) -> BinaryIO: ...
    @overload
    async def table(self, **params: Unpack[OpenligadbTableTextResponseParams]) -> str: ...
    @overload
    async def table(self, **params: Unpack[OpenligadbTableDefaultParams]) -> OpenligadbTableResponse: ...
    @overload
    async def team_pair_matches(self, **params: Unpack[OpenligadbTeamPairMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_pair_matches(self, **params: Unpack[OpenligadbTeamPairMatchesTextResponseParams]) -> str: ...
    @overload
    async def team_pair_matches(self, **params: Unpack[OpenligadbTeamPairMatchesDefaultParams]) -> OpenligadbTeamPairMatchesResponse: ...
    @overload
    async def teams(self, **params: Unpack[OpenligadbTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def teams(self, **params: Unpack[OpenligadbTeamsTextResponseParams]) -> str: ...
    @overload
    async def teams(self, **params: Unpack[OpenligadbTeamsDefaultParams]) -> OpenligadbTeamsResponse: ...

OpenligadbCurrentGroupDefaultParams = TypedDict('OpenligadbCurrentGroupDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbCurrentGroupTextResponseParams = TypedDict('OpenligadbCurrentGroupTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbCurrentGroupStreamParams = TypedDict('OpenligadbCurrentGroupStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbCurrentMatchdayDefaultParams = TypedDict('OpenligadbCurrentMatchdayDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbCurrentMatchdayTextResponseParams = TypedDict('OpenligadbCurrentMatchdayTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbCurrentMatchdayStreamParams = TypedDict('OpenligadbCurrentMatchdayStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbGoalGettersDefaultParams = TypedDict('OpenligadbGoalGettersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbGoalGettersTextResponseParams = TypedDict('OpenligadbGoalGettersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbGoalGettersStreamParams = TypedDict('OpenligadbGoalGettersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbGroupsDefaultParams = TypedDict('OpenligadbGroupsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbGroupsTextResponseParams = TypedDict('OpenligadbGroupsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbGroupsStreamParams = TypedDict('OpenligadbGroupsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbLastChangedDefaultParams = TypedDict('OpenligadbLastChangedDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_shortcut': Required[str],
    'season': Required[int],
    'group_order_id': Required[int],
}, total=False)

OpenligadbLastChangedTextResponseParams = TypedDict('OpenligadbLastChangedTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_shortcut': Required[str],
    'season': Required[int],
    'group_order_id': Required[int],
}, total=False)

OpenligadbLastChangedStreamParams = TypedDict('OpenligadbLastChangedStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_shortcut': Required[str],
    'season': Required[int],
    'group_order_id': Required[int],
}, total=False)

OpenligadbLastMatchDefaultParams = TypedDict('OpenligadbLastMatchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbLastMatchTextResponseParams = TypedDict('OpenligadbLastMatchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbLastMatchStreamParams = TypedDict('OpenligadbLastMatchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbLastTeamMatchDefaultParams = TypedDict('OpenligadbLastTeamMatchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': Required[int],
    'team_id': Required[int],
}, total=False)

OpenligadbLastTeamMatchTextResponseParams = TypedDict('OpenligadbLastTeamMatchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': Required[int],
    'team_id': Required[int],
}, total=False)

OpenligadbLastTeamMatchStreamParams = TypedDict('OpenligadbLastTeamMatchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': Required[int],
    'team_id': Required[int],
}, total=False)

OpenligadbLeagueTeamMatchesDefaultParams = TypedDict('OpenligadbLeagueTeamMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_shortcut': Required[str],
    'season': Required[int],
    'team_filter': Required[str],
}, total=False)

OpenligadbLeagueTeamMatchesTextResponseParams = TypedDict('OpenligadbLeagueTeamMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_shortcut': Required[str],
    'season': Required[int],
    'team_filter': Required[str],
}, total=False)

OpenligadbLeagueTeamMatchesStreamParams = TypedDict('OpenligadbLeagueTeamMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_shortcut': Required[str],
    'season': Required[int],
    'team_filter': Required[str],
}, total=False)

OpenligadbLeaguesDefaultParams = TypedDict('OpenligadbLeaguesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'season': NotRequired[int],
}, total=False)

OpenligadbLeaguesTextResponseParams = TypedDict('OpenligadbLeaguesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'season': NotRequired[int],
}, total=False)

OpenligadbLeaguesStreamParams = TypedDict('OpenligadbLeaguesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'season': NotRequired[int],
}, total=False)

OpenligadbMatchDefaultParams = TypedDict('OpenligadbMatchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'match_id': Required[int],
}, total=False)

OpenligadbMatchTextResponseParams = TypedDict('OpenligadbMatchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'match_id': Required[int],
}, total=False)

OpenligadbMatchStreamParams = TypedDict('OpenligadbMatchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'match_id': Required[int],
}, total=False)

OpenligadbMatchdayMatchesDefaultParams = TypedDict('OpenligadbMatchdayMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_shortcut': Required[str],
    'season': Required[int],
    'group_order_id': Required[int],
}, total=False)

OpenligadbMatchdayMatchesTextResponseParams = TypedDict('OpenligadbMatchdayMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_shortcut': Required[str],
    'season': Required[int],
    'group_order_id': Required[int],
}, total=False)

OpenligadbMatchdayMatchesStreamParams = TypedDict('OpenligadbMatchdayMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_shortcut': Required[str],
    'season': Required[int],
    'group_order_id': Required[int],
}, total=False)

OpenligadbLeagueMatchesDefaultParams = TypedDict('OpenligadbLeagueMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbLeagueMatchesTextResponseParams = TypedDict('OpenligadbLeagueMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbLeagueMatchesStreamParams = TypedDict('OpenligadbLeagueMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbMatchesByTeamDefaultParams = TypedDict('OpenligadbMatchesByTeamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_filter': Required[str],
    'weeks_past': Required[int],
    'weeks_future': Required[int],
}, total=False)

OpenligadbMatchesByTeamTextResponseParams = TypedDict('OpenligadbMatchesByTeamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_filter': Required[str],
    'weeks_past': Required[int],
    'weeks_future': Required[int],
}, total=False)

OpenligadbMatchesByTeamStreamParams = TypedDict('OpenligadbMatchesByTeamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_filter': Required[str],
    'weeks_past': Required[int],
    'weeks_future': Required[int],
}, total=False)

OpenligadbMatchesByTeamIdDefaultParams = TypedDict('OpenligadbMatchesByTeamIdDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[int],
    'weeks_past': Required[int],
    'weeks_future': Required[int],
}, total=False)

OpenligadbMatchesByTeamIdTextResponseParams = TypedDict('OpenligadbMatchesByTeamIdTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[int],
    'weeks_past': Required[int],
    'weeks_future': Required[int],
}, total=False)

OpenligadbMatchesByTeamIdStreamParams = TypedDict('OpenligadbMatchesByTeamIdStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[int],
    'weeks_past': Required[int],
    'weeks_future': Required[int],
}, total=False)

OpenligadbNextMatchDefaultParams = TypedDict('OpenligadbNextMatchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbNextMatchTextResponseParams = TypedDict('OpenligadbNextMatchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbNextMatchStreamParams = TypedDict('OpenligadbNextMatchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_shortcut': Required[str],
}, total=False)

OpenligadbNextTeamMatchDefaultParams = TypedDict('OpenligadbNextTeamMatchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': Required[int],
    'team_id': Required[int],
}, total=False)

OpenligadbNextTeamMatchTextResponseParams = TypedDict('OpenligadbNextTeamMatchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': Required[int],
    'team_id': Required[int],
}, total=False)

OpenligadbNextTeamMatchStreamParams = TypedDict('OpenligadbNextTeamMatchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': Required[int],
    'team_id': Required[int],
}, total=False)

OpenligadbResultInfosDefaultParams = TypedDict('OpenligadbResultInfosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': Required[int],
}, total=False)

OpenligadbResultInfosTextResponseParams = TypedDict('OpenligadbResultInfosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': Required[int],
}, total=False)

OpenligadbResultInfosStreamParams = TypedDict('OpenligadbResultInfosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': Required[int],
}, total=False)

OpenligadbResultTypesDefaultParams = TypedDict('OpenligadbResultTypesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

OpenligadbResultTypesTextResponseParams = TypedDict('OpenligadbResultTypesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

OpenligadbResultTypesStreamParams = TypedDict('OpenligadbResultTypesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

OpenligadbSportsDefaultParams = TypedDict('OpenligadbSportsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

OpenligadbSportsTextResponseParams = TypedDict('OpenligadbSportsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

OpenligadbSportsStreamParams = TypedDict('OpenligadbSportsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

OpenligadbTableDefaultParams = TypedDict('OpenligadbTableDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbTableTextResponseParams = TypedDict('OpenligadbTableTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbTableStreamParams = TypedDict('OpenligadbTableStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbTeamPairMatchesDefaultParams = TypedDict('OpenligadbTeamPairMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id_1': Required[int],
    'team_id_2': Required[int],
}, total=False)

OpenligadbTeamPairMatchesTextResponseParams = TypedDict('OpenligadbTeamPairMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id_1': Required[int],
    'team_id_2': Required[int],
}, total=False)

OpenligadbTeamPairMatchesStreamParams = TypedDict('OpenligadbTeamPairMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id_1': Required[int],
    'team_id_2': Required[int],
}, total=False)

OpenligadbTeamsDefaultParams = TypedDict('OpenligadbTeamsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbTeamsTextResponseParams = TypedDict('OpenligadbTeamsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)

OpenligadbTeamsStreamParams = TypedDict('OpenligadbTeamsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_shortcut': Required[str],
    'season': Required[int],
}, total=False)
