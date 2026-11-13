import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class OpenLigaDBClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-openligadb-js/0.1.0" });
    this["currentGroup"] = (...args) => this.request("openligadb-current-group", ...args);
    this["currentMatchday"] = (...args) => this.request("openligadb-current-matchday", ...args);
    this["goalGetters"] = (...args) => this.request("openligadb-goal-getters", ...args);
    this["groups"] = (...args) => this.request("openligadb-groups", ...args);
    this["lastChanged"] = (...args) => this.request("openligadb-last-changed", ...args);
    this["lastMatch"] = (...args) => this.request("openligadb-last-match", ...args);
    this["lastTeamMatch"] = (...args) => this.request("openligadb-last-team-match", ...args);
    this["leagueTeamMatches"] = (...args) => this.request("openligadb-league-team-matches", ...args);
    this["leagues"] = (...args) => this.request("openligadb-leagues", ...args);
    this["match"] = (...args) => this.request("openligadb-match", ...args);
    this["matchdayMatches"] = (...args) => this.request("openligadb-matchday-matches", ...args);
    this["leagueMatches"] = (...args) => this.request("openligadb-league-matches", ...args);
    this["matchesByTeam"] = (...args) => this.request("openligadb-matches-by-team", ...args);
    this["matchesByTeamId"] = (...args) => this.request("openligadb-matches-by-team-id", ...args);
    this["nextMatch"] = (...args) => this.request("openligadb-next-match", ...args);
    this["nextTeamMatch"] = (...args) => this.request("openligadb-next-team-match", ...args);
    this["resultInfos"] = (...args) => this.request("openligadb-result-infos", ...args);
    this["resultTypes"] = (...args) => this.request("openligadb-result-types", ...args);
    this["sports"] = (...args) => this.request("openligadb-sports", ...args);
    this["table"] = (...args) => this.request("openligadb-table", ...args);
    this["teamPairMatches"] = (...args) => this.request("openligadb-team-pair-matches", ...args);
    this["teams"] = (...args) => this.request("openligadb-teams", ...args);
  }
}

export { OpenLigaDBClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default OpenLigaDBClient;
