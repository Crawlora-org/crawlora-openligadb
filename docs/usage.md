# OpenLigaDB API endpoint reference and client usage

This reference lists all 22 public OpenLigaDB API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/openligadb`, `crawlora-openligadb`, and `crawlora-openligadb` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape OpenLigaDB locally; Crawlora is independent from and not endorsed by OpenLigaDB or its owners.

The package tracks the public API contract revision `sha256:9929d8853c9011b8932375f44643bbc8a523ddc87ae517a17e2f4ffde3fcbfb2` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `openligadb`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `currentGroup` | `current_group` | `openligadb.current_group` | `GET /openligadb/current-group` | `league_shortcut` (query, required) | Get the current league matchday |
| `currentMatchday` | `current_matchday` | `openligadb.current_matchday` | `GET /openligadb/current-matchday` | `league_shortcut` (query, required) | Get current matchday fixtures and results |
| `goalGetters` | `goal_getters` | `openligadb.goal_getters` | `GET /openligadb/goal-getters` | `league_shortcut` (query, required), `season` (query, required) | List league season goal-getters |
| `groups` | `groups` | `openligadb.groups` | `GET /openligadb/groups` | `league_shortcut` (query, required), `season` (query, required) | List league matchdays and rounds |
| `lastChanged` | `last_changed` | `openligadb.last_changed` | `GET /openligadb/last-changed` | `league_shortcut` (query, required), `season` (query, required), `group_order_id` (query, required) | Get a matchday's last update time |
| `lastMatch` | `last_match` | `openligadb.last_match` | `GET /openligadb/last-match` | `league_shortcut` (query, required) | Get a league's last match |
| `lastTeamMatch` | `last_team_match` | `openligadb.last_team_match` | `GET /openligadb/last-team-match` | `league_id` (query, required), `team_id` (query, required) | Get a team's last match in a league |
| `leagueMatches` | `league_matches` | `openligadb.league_matches` | `GET /openligadb/matches` | `league_shortcut` (query, required), `season` (query, required) | List a league season's matches |
| `leagues` | `leagues` | `openligadb.leagues` | `GET /openligadb/leagues` | `season` (query, optional) | List OpenLigaDB league seasons |
| `leagueTeamMatches` | `league_team_matches` | `openligadb.league_team_matches` | `GET /openligadb/league-team-matches` | `league_shortcut` (query, required), `season` (query, required), `team_filter` (query, required) | Find a team's matches in one league season |
| `match` | `match` | `openligadb.match_` | `GET /openligadb/match` | `match_id` (query, required) | Get one OpenLigaDB match |
| `matchdayMatches` | `matchday_matches` | `openligadb.matchday_matches` | `GET /openligadb/matchday-matches` | `league_shortcut` (query, required), `season` (query, required), `group_order_id` (query, required) | List one league matchday |
| `matchesByTeam` | `matches_by_team` | `openligadb.matches_by_team` | `GET /openligadb/matches-by-team` | `team_filter` (query, required), `weeks_past` (query, required), `weeks_future` (query, required) | Find recent and upcoming matches by team name |
| `matchesByTeamId` | `matches_by_team_id` | `openligadb.matches_by_team_id` | `GET /openligadb/matches-by-team-id` | `team_id` (query, required), `weeks_past` (query, required), `weeks_future` (query, required) | Find recent and upcoming matches by team id |
| `nextMatch` | `next_match` | `openligadb.next_match` | `GET /openligadb/next-match` | `league_shortcut` (query, required) | Get a league's next match |
| `nextTeamMatch` | `next_team_match` | `openligadb.next_team_match` | `GET /openligadb/next-team-match` | `league_id` (query, required), `team_id` (query, required) | Get a team's next match in a league |
| `resultInfos` | `result_infos` | `openligadb.result_infos` | `GET /openligadb/result-infos` | `league_id` (query, required) | List result types configured for a league |
| `resultTypes` | `result_types` | `openligadb.result_types` | `GET /openligadb/result-types` | — | List global result types |
| `sports` | `sports` | `openligadb.sports` | `GET /openligadb/sports` | — | List OpenLigaDB sports |
| `table` | `table` | `openligadb.table` | `GET /openligadb/table` | `league_shortcut` (query, required), `season` (query, required) | Get a league season's table |
| `teamPairMatches` | `team_pair_matches` | `openligadb.team_pair_matches` | `GET /openligadb/team-pair-matches` | `team_id_1` (query, required), `team_id_2` (query, required) | List matches between two teams |
| `teams` | `teams` | `openligadb.teams` | `GET /openligadb/teams` | `league_shortcut` (query, required), `season` (query, required) | List teams in a league season |

## Client forms

- JavaScript: import `OpenLigaDBClient` (also exported as `Client`) from `@crawlora-org/openligadb`; use `new OpenLigaDBClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `OpenLigaDBClient` (also exported as `Client`) from `crawlora_openligadb`; use `with OpenLigaDBClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncOpenLigaDBClient`, used with `async with` and `await`.
- Rust: add `crawlora-openligadb` with Cargo; import `Client` and the generated operation parameter struct, then call `client.openligadb.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-openligadb/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
