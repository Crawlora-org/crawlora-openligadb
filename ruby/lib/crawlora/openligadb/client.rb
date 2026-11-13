require "json"
require "net/http"
require "uri"

module Crawlora
  module Openligadb
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"openligadb-current-group": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-current-group", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}], "path": "/openligadb/current-group", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "openligadb-current-matchday": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-current-matchday", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}], "path": "/openligadb/current-matchday", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "openligadb-goal-getters": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-goal-getters", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}], "path": "/openligadb/goal-getters", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-groups": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-groups", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}], "path": "/openligadb/groups", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-last-changed": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-last-changed", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}, {"description": "Matchday or round id from openligadb-groups", "in": "query", "name": "group_order_id", "required": true, "type": "integer", "x-example": 8}], "path": "/openligadb/last-changed", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}, {"in": "query", "name": "group_order_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-last-match": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-last-match", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}], "path": "/openligadb/last-match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "openligadb-last-team-match": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-last-team-match", "method": "GET", "params": [{"description": "OpenLigaDB league id from openligadb_leagues", "format": "int64", "in": "query", "name": "league_id", "required": true, "type": "integer", "x-example": 4937}, {"description": "OpenLigaDB team id from openligadb_teams", "format": "int64", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 40}], "path": "/openligadb/last-team-match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "integer"}, {"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-league-matches": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-league-matches", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}], "path": "/openligadb/matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-league-team-matches": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-league-team-matches", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}, {"description": "Partial team-name text; numeric-only values are not accepted", "in": "query", "name": "team_filter", "required": true, "type": "string", "x-example": "Bayern"}], "path": "/openligadb/league-team-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}, {"in": "query", "name": "team_filter", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "openligadb-leagues": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-leagues", "method": "GET", "params": [{"description": "Optional season starting year, e.g. 2026 for 2026/27", "in": "query", "name": "season", "type": "integer"}], "path": "/openligadb/leagues", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "season", "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-match": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-match", "method": "GET", "params": [{"description": "OpenLigaDB match id", "format": "int64", "in": "query", "name": "match_id", "required": true, "type": "integer", "x-example": 83224}], "path": "/openligadb/match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-matchday-matches": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-matchday-matches", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}, {"description": "Matchday or round id from openligadb-groups", "in": "query", "name": "group_order_id", "required": true, "type": "integer", "x-example": 8}], "path": "/openligadb/matchday-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}, {"in": "query", "name": "group_order_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-matches-by-team": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-matches-by-team", "method": "GET", "params": [{"description": "Partial team-name fragment", "in": "query", "name": "team_filter", "required": true, "type": "string", "x-example": "Bayern"}, {"description": "Number of weeks before today to include; zero is allowed", "format": "int64", "in": "query", "name": "weeks_past", "required": true, "type": "integer", "x-example": 1}, {"description": "Number of weeks after today to include; zero is allowed", "format": "int64", "in": "query", "name": "weeks_future", "required": true, "type": "integer", "x-example": 1}], "path": "/openligadb/matches-by-team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_filter", "required": true, "type": "string"}, {"in": "query", "name": "weeks_past", "required": true, "type": "integer"}, {"in": "query", "name": "weeks_future", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-matches-by-team-id": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-matches-by-team-id", "method": "GET", "params": [{"description": "OpenLigaDB team id from openligadb_teams", "format": "int64", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 40}, {"description": "Number of weeks before today to include; zero is allowed", "format": "int64", "in": "query", "name": "weeks_past", "required": true, "type": "integer", "x-example": 1}, {"description": "Number of weeks after today to include; zero is allowed", "format": "int64", "in": "query", "name": "weeks_future", "required": true, "type": "integer", "x-example": 1}], "path": "/openligadb/matches-by-team-id", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}, {"in": "query", "name": "weeks_past", "required": true, "type": "integer"}, {"in": "query", "name": "weeks_future", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-next-match": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-next-match", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}], "path": "/openligadb/next-match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "openligadb-next-team-match": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-next-team-match", "method": "GET", "params": [{"description": "OpenLigaDB league id from openligadb_leagues", "format": "int64", "in": "query", "name": "league_id", "required": true, "type": "integer", "x-example": 4937}, {"description": "OpenLigaDB team id from openligadb_teams", "format": "int64", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 40}], "path": "/openligadb/next-team-match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "integer"}, {"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-result-infos": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-result-infos", "method": "GET", "params": [{"description": "OpenLigaDB league id from openligadb-leagues", "format": "int64", "in": "query", "name": "league_id", "required": true, "type": "integer", "x-example": 4937}], "path": "/openligadb/result-infos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-result-types": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-result-types", "method": "GET", "params": [], "path": "/openligadb/result-types", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "openligadb-sports": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-sports", "method": "GET", "params": [], "path": "/openligadb/sports", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "openligadb-table": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-table", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}], "path": "/openligadb/table", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-team-pair-matches": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-team-pair-matches", "method": "GET", "params": [{"description": "First OpenLigaDB team id", "format": "int64", "in": "query", "name": "team_id_1", "required": true, "type": "integer", "x-example": 40}, {"description": "Second OpenLigaDB team id", "format": "int64", "in": "query", "name": "team_id_2", "required": true, "type": "integer", "x-example": 7}], "path": "/openligadb/team-pair-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id_1", "required": true, "type": "integer"}, {"in": "query", "name": "team_id_2", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "openligadb-teams": {"bodyParam": null, "bodyRequired": false, "id": "openligadb-teams", "method": "GET", "params": [{"description": "Exact shortcut from openligadb-leagues", "in": "query", "name": "league_shortcut", "required": true, "type": "string", "x-example": "bl1"}, {"description": "Season starting year", "in": "query", "name": "season", "required": true, "type": "integer", "x-example": 2026}], "path": "/openligadb/teams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_shortcut", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["openligadb-current-group", "openligadb-current-matchday", "openligadb-goal-getters", "openligadb-groups", "openligadb-last-changed", "openligadb-last-match", "openligadb-last-team-match", "openligadb-league-matches", "openligadb-league-team-matches", "openligadb-leagues", "openligadb-match", "openligadb-matchday-matches", "openligadb-matches-by-team", "openligadb-matches-by-team-id", "openligadb-next-match", "openligadb-next-team-match", "openligadb-result-infos", "openligadb-result-types", "openligadb-sports", "openligadb-table", "openligadb-team-pair-matches", "openligadb-teams"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-openligadb-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('current_group') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-current-group', params, response_type: response_type)
      end
      define_method('current_matchday') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-current-matchday', params, response_type: response_type)
      end
      define_method('goal_getters') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-goal-getters', params, response_type: response_type)
      end
      define_method('groups') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-groups', params, response_type: response_type)
      end
      define_method('last_changed') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-last-changed', params, response_type: response_type)
      end
      define_method('last_match') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-last-match', params, response_type: response_type)
      end
      define_method('last_team_match') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-last-team-match', params, response_type: response_type)
      end
      define_method('league_team_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-league-team-matches', params, response_type: response_type)
      end
      define_method('leagues') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-leagues', params, response_type: response_type)
      end
      define_method('match') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-match', params, response_type: response_type)
      end
      define_method('matchday_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-matchday-matches', params, response_type: response_type)
      end
      define_method('league_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-league-matches', params, response_type: response_type)
      end
      define_method('matches_by_team') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-matches-by-team', params, response_type: response_type)
      end
      define_method('matches_by_team_id') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-matches-by-team-id', params, response_type: response_type)
      end
      define_method('next_match') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-next-match', params, response_type: response_type)
      end
      define_method('next_team_match') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-next-team-match', params, response_type: response_type)
      end
      define_method('result_infos') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-result-infos', params, response_type: response_type)
      end
      define_method('result_types') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-result-types', params, response_type: response_type)
      end
      define_method('sports') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-sports', params, response_type: response_type)
      end
      define_method('table') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-table', params, response_type: response_type)
      end
      define_method('team_pair_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-team-pair-matches', params, response_type: response_type)
      end
      define_method('teams') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('openligadb-teams', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
