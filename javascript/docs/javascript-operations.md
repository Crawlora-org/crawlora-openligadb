# Crawlora OpenLigaDB JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `22`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openligadb | `openligadb.currentGroup` | `openligadb-current-group` | `GET /openligadb/current-group` | `league_shortcut` (query string required) | `ApiKeyAuth` | `OpenligadbCurrentGroupResponse` |  |
| openligadb | `openligadb.currentMatchday` | `openligadb-current-matchday` | `GET /openligadb/current-matchday` | `league_shortcut` (query string required) | `ApiKeyAuth` | `OpenligadbCurrentMatchdayResponse` |  |
| openligadb | `openligadb.goalGetters` | `openligadb-goal-getters` | `GET /openligadb/goal-getters` | `league_shortcut` (query string required)<br>`season` (query number required) | `ApiKeyAuth` | `OpenligadbGoalGettersResponse` |  |
| openligadb | `openligadb.groups` | `openligadb-groups` | `GET /openligadb/groups` | `league_shortcut` (query string required)<br>`season` (query number required) | `ApiKeyAuth` | `OpenligadbGroupsResponse` |  |
| openligadb | `openligadb.lastChanged` | `openligadb-last-changed` | `GET /openligadb/last-changed` | `league_shortcut` (query string required)<br>`season` (query number required)<br>`group_order_id` (query number required) | `ApiKeyAuth` | `OpenligadbLastChangedResponse` |  |
| openligadb | `openligadb.lastMatch` | `openligadb-last-match` | `GET /openligadb/last-match` | `league_shortcut` (query string required) | `ApiKeyAuth` | `OpenligadbLastMatchResponse` |  |
| openligadb | `openligadb.lastTeamMatch` | `openligadb-last-team-match` | `GET /openligadb/last-team-match` | `league_id` (query number required)<br>`team_id` (query number required) | `ApiKeyAuth` | `OpenligadbLastTeamMatchResponse` |  |
| openligadb | `openligadb.leagueTeamMatches` | `openligadb-league-team-matches` | `GET /openligadb/league-team-matches` | `league_shortcut` (query string required)<br>`season` (query number required)<br>`team_filter` (query string required) | `ApiKeyAuth` | `OpenligadbLeagueTeamMatchesResponse` |  |
| openligadb | `openligadb.leagues` | `openligadb-leagues` | `GET /openligadb/leagues` | `season` (query number) | `ApiKeyAuth` | `OpenligadbLeaguesResponse` |  |
| openligadb | `openligadb.match` | `openligadb-match` | `GET /openligadb/match` | `match_id` (query number required) | `ApiKeyAuth` | `OpenligadbMatchResponse` |  |
| openligadb | `openligadb.matchdayMatches` | `openligadb-matchday-matches` | `GET /openligadb/matchday-matches` | `league_shortcut` (query string required)<br>`season` (query number required)<br>`group_order_id` (query number required) | `ApiKeyAuth` | `OpenligadbMatchdayMatchesResponse` |  |
| openligadb | `openligadb.leagueMatches` | `openligadb-league-matches` | `GET /openligadb/matches` | `league_shortcut` (query string required)<br>`season` (query number required) | `ApiKeyAuth` | `OpenligadbLeagueMatchesResponse` |  |
| openligadb | `openligadb.matchesByTeam` | `openligadb-matches-by-team` | `GET /openligadb/matches-by-team` | `team_filter` (query string required)<br>`weeks_past` (query number required)<br>`weeks_future` (query number required) | `ApiKeyAuth` | `OpenligadbMatchesByTeamResponse` |  |
| openligadb | `openligadb.matchesByTeamId` | `openligadb-matches-by-team-id` | `GET /openligadb/matches-by-team-id` | `team_id` (query number required)<br>`weeks_past` (query number required)<br>`weeks_future` (query number required) | `ApiKeyAuth` | `OpenligadbMatchesByTeamIdResponse` |  |
| openligadb | `openligadb.nextMatch` | `openligadb-next-match` | `GET /openligadb/next-match` | `league_shortcut` (query string required) | `ApiKeyAuth` | `OpenligadbNextMatchResponse` |  |
| openligadb | `openligadb.nextTeamMatch` | `openligadb-next-team-match` | `GET /openligadb/next-team-match` | `league_id` (query number required)<br>`team_id` (query number required) | `ApiKeyAuth` | `OpenligadbNextTeamMatchResponse` |  |
| openligadb | `openligadb.resultInfos` | `openligadb-result-infos` | `GET /openligadb/result-infos` | `league_id` (query number required) | `ApiKeyAuth` | `OpenligadbResultInfosResponse` |  |
| openligadb | `openligadb.resultTypes` | `openligadb-result-types` | `GET /openligadb/result-types` | none | `ApiKeyAuth` | `OpenligadbResultTypesResponse` |  |
| openligadb | `openligadb.sports` | `openligadb-sports` | `GET /openligadb/sports` | none | `ApiKeyAuth` | `OpenligadbSportsResponse` |  |
| openligadb | `openligadb.table` | `openligadb-table` | `GET /openligadb/table` | `league_shortcut` (query string required)<br>`season` (query number required) | `ApiKeyAuth` | `OpenligadbTableResponse` |  |
| openligadb | `openligadb.teamPairMatches` | `openligadb-team-pair-matches` | `GET /openligadb/team-pair-matches` | `team_id_1` (query number required)<br>`team_id_2` (query number required) | `ApiKeyAuth` | `OpenligadbTeamPairMatchesResponse` |  |
| openligadb | `openligadb.teams` | `openligadb-teams` | `GET /openligadb/teams` | `league_shortcut` (query string required)<br>`season` (query number required) | `ApiKeyAuth` | `OpenligadbTeamsResponse` |  |
