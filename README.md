# OpenLigaDB clients for Crawlora

Official Crawlora client packages for the hosted OpenLigaDB API. Access 22 API endpoints covering sports and league discovery, fixtures, match results, standings, scorers, and team match history from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape OpenLigaDB locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by OpenLigaDB or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/openligadb`](javascript/README.md)
- Python: [`crawlora-openligadb`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-openligadb`](go.mod)
- Ruby: [`crawlora-openligadb`](ruby/README.md)
- Java: [`net.crawlora:crawlora-openligadb:0.1.0`](java/README.md)
- PHP: [`crawlora/openligadb`](php/README.md)
- Rust: [`crawlora-openligadb`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=openligadb-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=openligadb-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=openligadb-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 22 selected public OpenLigaDB API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
