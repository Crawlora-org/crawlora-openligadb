<?php

declare(strict_types=1);

namespace Crawlora\Openligadb;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'openligadb';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 22;
    public const OPERATION_IDS = ["openligadb-current-group", "openligadb-current-matchday", "openligadb-goal-getters", "openligadb-groups", "openligadb-last-changed", "openligadb-last-match", "openligadb-last-team-match", "openligadb-league-matches", "openligadb-league-team-matches", "openligadb-leagues", "openligadb-match", "openligadb-matchday-matches", "openligadb-matches-by-team", "openligadb-matches-by-team-id", "openligadb-next-match", "openligadb-next-team-match", "openligadb-result-infos", "openligadb-result-types", "openligadb-sports", "openligadb-table", "openligadb-team-pair-matches", "openligadb-teams"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"openligadb-current-group": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-current-group", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}], "path": "/openligadb/current-group", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "openligadb-current-matchday": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-current-matchday", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}], "path": "/openligadb/current-matchday", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "openligadb-goal-getters": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-goal-getters", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}], "path": "/openligadb/goal-getters", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-groups": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-groups", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}], "path": "/openligadb/groups", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-last-changed": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-last-changed", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}, {"description": "Matchday or round id from openligadb-groups", "in": "query", "name": "group_order_id", "required": true, "type": "integer", "x-example": 8}], "path": "/openligadb/last-changed", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}, {"in": "query", "name": "group_order_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-last-match": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-last-match", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}], "path": "/openligadb/last-match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "openligadb-last-team-match": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-last-team-match", "method": "GET", "params": [{"description": "OpenLigaDB league id from openligadb_leagues", "format": "int64", "in": "query", "name": "league_id", "required": true, "type": "integer", "x-example": 4937}, {"description": "OpenLigaDB team id from openligadb_teams", "format": "int64", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 40}], "path": "/openligadb/last-team-match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "integer"}, {"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-league-matches": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-league-matches", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}], "path": "/openligadb/matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-league-team-matches": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-league-team-matches", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}, {"description": "Partial team-name text; numeric-only values are not accepted", "in": "query", "name": "team_filter", "required": true, "type": "string", "x-example": "Bayern"}], "path": "/openligadb/league-team-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}, {"in": "query", "name": "team_filter", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "openligadb-leagues": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-leagues", "method": "GET", "params": [{"description": "Optional season starting year, e.g. 2026 for 2026/27", "in": "query", "name": "season", "type": "integer"}], "path": "/openligadb/leagues", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "season", "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-match": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-match", "method": "GET", "params": [{"description": "OpenLigaDB match id", "format": "int64", "in": "query", "name": "match_id", "required": true, "type": "integer", "x-example": 83224}], "path": "/openligadb/match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-matchday-matches": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-matchday-matches", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}, {"description": "Matchday or round id from openligadb-groups", "in": "query", "name": "group_order_id", "required": true, "type": "integer", "x-example": 8}], "path": "/openligadb/matchday-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}, {"in": "query", "name": "group_order_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-matches-by-team": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-matches-by-team", "method": "GET", "params": [{"description": "Partial team-name fragment", "in": "query", "name": "team_filter", "required": true, "type": "string", "x-example": "Bayern"}, {"description": "Number of weeks before today to include; zero is allowed", "format": "int64", "in": "query", "name": "weeks_past", "required": true, "type": "integer", "x-example": 1}, {"description": "Number of weeks after today to include; zero is allowed", "format": "int64", "in": "query", "name": "weeks_future", "required": true, "type": "integer", "x-example": 1}], "path": "/openligadb/matches-by-team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_filter", "required": true, "type": "string"}, {"in": "query", "name": "weeks_past", "required": true, "type": "integer"}, {"in": "query", "name": "weeks_future", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-matches-by-team-id": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-matches-by-team-id", "method": "GET", "params": [{"description": "OpenLigaDB team id from openligadb_teams", "format": "int64", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 40}, {"description": "Number of weeks before today to include; zero is allowed", "format": "int64", "in": "query", "name": "weeks_past", "required": true, "type": "integer", "x-example": 1}, {"description": "Number of weeks after today to include; zero is allowed", "format": "int64", "in": "query", "name": "weeks_future", "required": true, "type": "integer", "x-example": 1}], "path": "/openligadb/matches-by-team-id", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}, {"in": "query", "name": "weeks_past", "required": true, "type": "integer"}, {"in": "query", "name": "weeks_future", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-next-match": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-next-match", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}], "path": "/openligadb/next-match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "openligadb-next-team-match": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-next-team-match", "method": "GET", "params": [{"description": "OpenLigaDB league id from openligadb_leagues", "format": "int64", "in": "query", "name": "league_id", "required": true, "type": "integer", "x-example": 4937}, {"description": "OpenLigaDB team id from openligadb_teams", "format": "int64", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 40}], "path": "/openligadb/next-team-match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "integer"}, {"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-result-infos": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-result-infos", "method": "GET", "params": [{"description": "OpenLigaDB league id from openligadb-leagues", "format": "int64", "in": "query", "name": "league_id", "required": true, "type": "integer", "x-example": 4937}], "path": "/openligadb/result-infos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-result-types": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-result-types", "method": "GET", "params": [], "path": "/openligadb/result-types", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "openligadb-sports": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-sports", "method": "GET", "params": [], "path": "/openligadb/sports", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "openligadb-table": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-table", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}], "path": "/openligadb/table", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-team-pair-matches": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-team-pair-matches", "method": "GET", "params": [{"description": "First OpenLigaDB team id", "format": "int64", "in": "query", "name": "team_id_1", "required": true, "type": "integer", "x-example": 40}, {"description": "Second OpenLigaDB team id", "format": "int64", "in": "query", "name": "team_id_2", "required": true, "type": "integer", "x-example": 7}], "path": "/openligadb/team-pair-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id_1", "required": true, "type": "integer"}, {"in": "query", "name": "team_id_2", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-teams": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-teams", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}], "path": "/openligadb/teams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-openligadb-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function current_group(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-current-group", $params, $responseType);
    }
    public function current_matchday(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-current-matchday", $params, $responseType);
    }
    public function goal_getters(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-goal-getters", $params, $responseType);
    }
    public function groups(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-groups", $params, $responseType);
    }
    public function last_changed(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-last-changed", $params, $responseType);
    }
    public function last_match(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-last-match", $params, $responseType);
    }
    public function last_team_match(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-last-team-match", $params, $responseType);
    }
    public function league_team_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-league-team-matches", $params, $responseType);
    }
    public function leagues(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-leagues", $params, $responseType);
    }
    public function match(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-match", $params, $responseType);
    }
    public function matchday_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-matchday-matches", $params, $responseType);
    }
    public function league_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-league-matches", $params, $responseType);
    }
    public function matches_by_team(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-matches-by-team", $params, $responseType);
    }
    public function matches_by_team_id(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-matches-by-team-id", $params, $responseType);
    }
    public function next_match(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-next-match", $params, $responseType);
    }
    public function next_team_match(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-next-team-match", $params, $responseType);
    }
    public function result_infos(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-result-infos", $params, $responseType);
    }
    public function result_types(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-result-types", $params, $responseType);
    }
    public function sports(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-sports", $params, $responseType);
    }
    public function table(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-table", $params, $responseType);
    }
    public function team_pair_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-team-pair-matches", $params, $responseType);
    }
    public function teams(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("openligadb-teams", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
