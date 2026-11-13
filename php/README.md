# Crawlora OpenLigaDB API client for PHP (`crawlora/openligadb`)

This PHP package calls Crawlora's hosted OpenLigaDB API at `https://api.crawlora.net/api/v1`. It exposes 22 endpoints covering sports and league discovery, fixtures, match results, standings, scorers, and team match history. It does not call or scrape OpenLigaDB directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/openligadb
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=openligadb-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=openligadb-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Openligadb\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("openligadb-current-group", ['league_shortcut' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 22 API operations.

## Supported OpenLigaDB API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-openligadb/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=openligadb-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=openligadb-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-openligadb). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-openligadb/blob/main/docs/usage.md).
