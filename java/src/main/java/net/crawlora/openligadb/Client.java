package net.crawlora.openligadb;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the OpenLigaDB endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 22;
    public static final List<String> OPERATION_IDS = List.of(
            "openligadb-current-group",
            "openligadb-current-matchday",
            "openligadb-goal-getters",
            "openligadb-groups",
            "openligadb-last-changed",
            "openligadb-last-match",
            "openligadb-last-team-match",
            "openligadb-league-matches",
            "openligadb-league-team-matches",
            "openligadb-leagues",
            "openligadb-match",
            "openligadb-matchday-matches",
            "openligadb-matches-by-team",
            "openligadb-matches-by-team-id",
            "openligadb-next-match",
            "openligadb-next-team-match",
            "openligadb-result-infos",
            "openligadb-result-types",
            "openligadb-sports",
            "openligadb-table",
            "openligadb-team-pair-matches",
            "openligadb-teams"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("openligadb-current-group", new Operation("openligadb-current-group", "GET", "/openligadb/current-group", Map.ofEntries(Map.entry("league_shortcut", new Param("league_shortcut", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-current-matchday", new Operation("openligadb-current-matchday", "GET", "/openligadb/current-matchday", Map.ofEntries(Map.entry("league_shortcut", new Param("league_shortcut", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-goal-getters", new Operation("openligadb-goal-getters", "GET", "/openligadb/goal-getters", Map.ofEntries(Map.entry("league_shortcut", new Param("league_shortcut", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-groups", new Operation("openligadb-groups", "GET", "/openligadb/groups", Map.ofEntries(Map.entry("league_shortcut", new Param("league_shortcut", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-last-changed", new Operation("openligadb-last-changed", "GET", "/openligadb/last-changed", Map.ofEntries(Map.entry("league_shortcut", new Param("league_shortcut", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "integer", List.of(), "csv")), Map.entry("group_order_id", new Param("group_order_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-last-match", new Operation("openligadb-last-match", "GET", "/openligadb/last-match", Map.ofEntries(Map.entry("league_shortcut", new Param("league_shortcut", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-last-team-match", new Operation("openligadb-last-team-match", "GET", "/openligadb/last-team-match", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", true, "integer", List.of(), "csv")), Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-league-team-matches", new Operation("openligadb-league-team-matches", "GET", "/openligadb/league-team-matches", Map.ofEntries(Map.entry("league_shortcut", new Param("league_shortcut", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "integer", List.of(), "csv")), Map.entry("team_filter", new Param("team_filter", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-leagues", new Operation("openligadb-leagues", "GET", "/openligadb/leagues", Map.ofEntries(Map.entry("season", new Param("season", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-match", new Operation("openligadb-match", "GET", "/openligadb/match", Map.ofEntries(Map.entry("match_id", new Param("match_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-matchday-matches", new Operation("openligadb-matchday-matches", "GET", "/openligadb/matchday-matches", Map.ofEntries(Map.entry("league_shortcut", new Param("league_shortcut", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "integer", List.of(), "csv")), Map.entry("group_order_id", new Param("group_order_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-league-matches", new Operation("openligadb-league-matches", "GET", "/openligadb/matches", Map.ofEntries(Map.entry("league_shortcut", new Param("league_shortcut", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-matches-by-team", new Operation("openligadb-matches-by-team", "GET", "/openligadb/matches-by-team", Map.ofEntries(Map.entry("team_filter", new Param("team_filter", "query", true, "string", List.of(), "csv")), Map.entry("weeks_past", new Param("weeks_past", "query", true, "integer", List.of(), "csv")), Map.entry("weeks_future", new Param("weeks_future", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-matches-by-team-id", new Operation("openligadb-matches-by-team-id", "GET", "/openligadb/matches-by-team-id", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv")), Map.entry("weeks_past", new Param("weeks_past", "query", true, "integer", List.of(), "csv")), Map.entry("weeks_future", new Param("weeks_future", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-next-match", new Operation("openligadb-next-match", "GET", "/openligadb/next-match", Map.ofEntries(Map.entry("league_shortcut", new Param("league_shortcut", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-next-team-match", new Operation("openligadb-next-team-match", "GET", "/openligadb/next-team-match", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", true, "integer", List.of(), "csv")), Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-result-infos", new Operation("openligadb-result-infos", "GET", "/openligadb/result-infos", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-result-types", new Operation("openligadb-result-types", "GET", "/openligadb/result-types", Map.of(), List.of("application/json")));
        operations.put("openligadb-sports", new Operation("openligadb-sports", "GET", "/openligadb/sports", Map.of(), List.of("application/json")));
        operations.put("openligadb-table", new Operation("openligadb-table", "GET", "/openligadb/table", Map.ofEntries(Map.entry("league_shortcut", new Param("league_shortcut", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-team-pair-matches", new Operation("openligadb-team-pair-matches", "GET", "/openligadb/team-pair-matches", Map.ofEntries(Map.entry("team_id_1", new Param("team_id_1", "query", true, "integer", List.of(), "csv")), Map.entry("team_id_2", new Param("team_id_2", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("openligadb-teams", new Operation("openligadb-teams", "GET", "/openligadb/teams", Map.ofEntries(Map.entry("league_shortcut", new Param("league_shortcut", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown OpenLigaDB operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object currentGroup(Map<String, ?> params) { return request("openligadb-current-group", params); }
    public Object currentMatchday(Map<String, ?> params) { return request("openligadb-current-matchday", params); }
    public Object goalGetters(Map<String, ?> params) { return request("openligadb-goal-getters", params); }
    public Object groups(Map<String, ?> params) { return request("openligadb-groups", params); }
    public Object lastChanged(Map<String, ?> params) { return request("openligadb-last-changed", params); }
    public Object lastMatch(Map<String, ?> params) { return request("openligadb-last-match", params); }
    public Object lastTeamMatch(Map<String, ?> params) { return request("openligadb-last-team-match", params); }
    public Object leagueTeamMatches(Map<String, ?> params) { return request("openligadb-league-team-matches", params); }
    public Object leagues(Map<String, ?> params) { return request("openligadb-leagues", params); }
    public Object match(Map<String, ?> params) { return request("openligadb-match", params); }
    public Object matchdayMatches(Map<String, ?> params) { return request("openligadb-matchday-matches", params); }
    public Object leagueMatches(Map<String, ?> params) { return request("openligadb-league-matches", params); }
    public Object matchesByTeam(Map<String, ?> params) { return request("openligadb-matches-by-team", params); }
    public Object matchesByTeamId(Map<String, ?> params) { return request("openligadb-matches-by-team-id", params); }
    public Object nextMatch(Map<String, ?> params) { return request("openligadb-next-match", params); }
    public Object nextTeamMatch(Map<String, ?> params) { return request("openligadb-next-team-match", params); }
    public Object resultInfos(Map<String, ?> params) { return request("openligadb-result-infos", params); }
    public Object resultTypes(Map<String, ?> params) { return request("openligadb-result-types", params); }
    public Object sports(Map<String, ?> params) { return request("openligadb-sports", params); }
    public Object table(Map<String, ?> params) { return request("openligadb-table", params); }
    public Object teamPairMatches(Map<String, ?> params) { return request("openligadb-team-pair-matches", params); }
    public Object teams(Map<String, ?> params) { return request("openligadb-teams", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
