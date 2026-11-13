# Crawlora OpenLigaDB Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `22`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openligadb | `openligadb.current_group` | `openligadb-current-group` | `GET /openligadb/current-group` | `league_shortcut` (query String required) | `ApiKeyAuth` | `OpenligadbCurrentGroupResponse` |  |
| openligadb | `openligadb.current_matchday` | `openligadb-current-matchday` | `GET /openligadb/current-matchday` | `league_shortcut` (query String required) | `ApiKeyAuth` | `OpenligadbCurrentMatchdayResponse` |  |
| openligadb | `openligadb.goal_getters` | `openligadb-goal-getters` | `GET /openligadb/goal-getters` | `league_shortcut` (query String required)<br>`season` (query i64 required) | `ApiKeyAuth` | `OpenligadbGoalGettersResponse` |  |
| openligadb | `openligadb.groups` | `openligadb-groups` | `GET /openligadb/groups` | `league_shortcut` (query String required)<br>`season` (query i64 required) | `ApiKeyAuth` | `OpenligadbGroupsResponse` |  |
| openligadb | `openligadb.last_changed` | `openligadb-last-changed` | `GET /openligadb/last-changed` | `league_shortcut` (query String required)<br>`season` (query i64 required)<br>`group_order_id` (query i64 required) | `ApiKeyAuth` | `OpenligadbLastChangedResponse` |  |
| openligadb | `openligadb.last_match` | `openligadb-last-match` | `GET /openligadb/last-match` | `league_shortcut` (query String required) | `ApiKeyAuth` | `OpenligadbLastMatchResponse` |  |
| openligadb | `openligadb.last_team_match` | `openligadb-last-team-match` | `GET /openligadb/last-team-match` | `league_id` (query i64 required)<br>`team_id` (query i64 required) | `ApiKeyAuth` | `OpenligadbLastTeamMatchResponse` |  |
| openligadb | `openligadb.league_team_matches` | `openligadb-league-team-matches` | `GET /openligadb/league-team-matches` | `league_shortcut` (query String required)<br>`season` (query i64 required)<br>`team_filter` (query String required) | `ApiKeyAuth` | `OpenligadbLeagueTeamMatchesResponse` |  |
| openligadb | `openligadb.leagues` | `openligadb-leagues` | `GET /openligadb/leagues` | `season` (query i64) | `ApiKeyAuth` | `OpenligadbLeaguesResponse` |  |
| openligadb | `openligadb.match_` | `openligadb-match` | `GET /openligadb/match` | `match_id` (query i64 required) | `ApiKeyAuth` | `OpenligadbMatchResponse` |  |
| openligadb | `openligadb.matchday_matches` | `openligadb-matchday-matches` | `GET /openligadb/matchday-matches` | `league_shortcut` (query String required)<br>`season` (query i64 required)<br>`group_order_id` (query i64 required) | `ApiKeyAuth` | `OpenligadbMatchdayMatchesResponse` |  |
| openligadb | `openligadb.league_matches` | `openligadb-league-matches` | `GET /openligadb/matches` | `league_shortcut` (query String required)<br>`season` (query i64 required) | `ApiKeyAuth` | `OpenligadbLeagueMatchesResponse` |  |
| openligadb | `openligadb.matches_by_team` | `openligadb-matches-by-team` | `GET /openligadb/matches-by-team` | `team_filter` (query String required)<br>`weeks_past` (query i64 required)<br>`weeks_future` (query i64 required) | `ApiKeyAuth` | `OpenligadbMatchesByTeamResponse` |  |
| openligadb | `openligadb.matches_by_team_id` | `openligadb-matches-by-team-id` | `GET /openligadb/matches-by-team-id` | `team_id` (query i64 required)<br>`weeks_past` (query i64 required)<br>`weeks_future` (query i64 required) | `ApiKeyAuth` | `OpenligadbMatchesByTeamIdResponse` |  |
| openligadb | `openligadb.next_match` | `openligadb-next-match` | `GET /openligadb/next-match` | `league_shortcut` (query String required) | `ApiKeyAuth` | `OpenligadbNextMatchResponse` |  |
| openligadb | `openligadb.next_team_match` | `openligadb-next-team-match` | `GET /openligadb/next-team-match` | `league_id` (query i64 required)<br>`team_id` (query i64 required) | `ApiKeyAuth` | `OpenligadbNextTeamMatchResponse` |  |
| openligadb | `openligadb.result_infos` | `openligadb-result-infos` | `GET /openligadb/result-infos` | `league_id` (query i64 required) | `ApiKeyAuth` | `OpenligadbResultInfosResponse` |  |
| openligadb | `openligadb.result_types` | `openligadb-result-types` | `GET /openligadb/result-types` | none | `ApiKeyAuth` | `OpenligadbResultTypesResponse` |  |
| openligadb | `openligadb.sports` | `openligadb-sports` | `GET /openligadb/sports` | none | `ApiKeyAuth` | `OpenligadbSportsResponse` |  |
| openligadb | `openligadb.table` | `openligadb-table` | `GET /openligadb/table` | `league_shortcut` (query String required)<br>`season` (query i64 required) | `ApiKeyAuth` | `OpenligadbTableResponse` |  |
| openligadb | `openligadb.team_pair_matches` | `openligadb-team-pair-matches` | `GET /openligadb/team-pair-matches` | `team_id_1` (query i64 required)<br>`team_id_2` (query i64 required) | `ApiKeyAuth` | `OpenligadbTeamPairMatchesResponse` |  |
| openligadb | `openligadb.teams` | `openligadb-teams` | `GET /openligadb/teams` | `league_shortcut` (query String required)<br>`season` (query i64 required) | `ApiKeyAuth` | `OpenligadbTeamsResponse` |  |
