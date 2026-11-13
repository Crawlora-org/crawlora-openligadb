import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class OpenLigaDBClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  currentGroup(params: OperationParamsMap["openligadb-current-group"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  currentMatchday(params: OperationParamsMap["openligadb-current-matchday"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  goalGetters(params: OperationParamsMap["openligadb-goal-getters"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  groups(params: OperationParamsMap["openligadb-groups"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  lastChanged(params: OperationParamsMap["openligadb-last-changed"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  lastMatch(params: OperationParamsMap["openligadb-last-match"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  lastTeamMatch(params: OperationParamsMap["openligadb-last-team-match"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  leagueTeamMatches(params: OperationParamsMap["openligadb-league-team-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  leagues(params?: OperationParamsMap["openligadb-leagues"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  match(params: OperationParamsMap["openligadb-match"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchdayMatches(params: OperationParamsMap["openligadb-matchday-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  leagueMatches(params: OperationParamsMap["openligadb-league-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchesByTeam(params: OperationParamsMap["openligadb-matches-by-team"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchesByTeamId(params: OperationParamsMap["openligadb-matches-by-team-id"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  nextMatch(params: OperationParamsMap["openligadb-next-match"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  nextTeamMatch(params: OperationParamsMap["openligadb-next-team-match"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  resultInfos(params: OperationParamsMap["openligadb-result-infos"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  resultTypes(params?: OperationParamsMap["openligadb-result-types"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sports(params?: OperationParamsMap["openligadb-sports"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  table(params: OperationParamsMap["openligadb-table"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamPairMatches(params: OperationParamsMap["openligadb-team-pair-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teams(params: OperationParamsMap["openligadb-teams"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  currentGroup(params: OperationParamsMap["openligadb-current-group"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  currentMatchday(params: OperationParamsMap["openligadb-current-matchday"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  goalGetters(params: OperationParamsMap["openligadb-goal-getters"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  groups(params: OperationParamsMap["openligadb-groups"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  lastChanged(params: OperationParamsMap["openligadb-last-changed"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  lastMatch(params: OperationParamsMap["openligadb-last-match"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  lastTeamMatch(params: OperationParamsMap["openligadb-last-team-match"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  leagueTeamMatches(params: OperationParamsMap["openligadb-league-team-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  leagues(params?: OperationParamsMap["openligadb-leagues"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  match(params: OperationParamsMap["openligadb-match"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchdayMatches(params: OperationParamsMap["openligadb-matchday-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  leagueMatches(params: OperationParamsMap["openligadb-league-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchesByTeam(params: OperationParamsMap["openligadb-matches-by-team"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchesByTeamId(params: OperationParamsMap["openligadb-matches-by-team-id"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  nextMatch(params: OperationParamsMap["openligadb-next-match"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  nextTeamMatch(params: OperationParamsMap["openligadb-next-team-match"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  resultInfos(params: OperationParamsMap["openligadb-result-infos"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  resultTypes(params?: OperationParamsMap["openligadb-result-types"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sports(params?: OperationParamsMap["openligadb-sports"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  table(params: OperationParamsMap["openligadb-table"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamPairMatches(params: OperationParamsMap["openligadb-team-pair-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teams(params: OperationParamsMap["openligadb-teams"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  currentGroup(...args: OperationRequestArgs<"openligadb-current-group">): Promise<OperationResponseMap["openligadb-current-group"]>;
  currentMatchday(...args: OperationRequestArgs<"openligadb-current-matchday">): Promise<OperationResponseMap["openligadb-current-matchday"]>;
  goalGetters(...args: OperationRequestArgs<"openligadb-goal-getters">): Promise<OperationResponseMap["openligadb-goal-getters"]>;
  groups(...args: OperationRequestArgs<"openligadb-groups">): Promise<OperationResponseMap["openligadb-groups"]>;
  lastChanged(...args: OperationRequestArgs<"openligadb-last-changed">): Promise<OperationResponseMap["openligadb-last-changed"]>;
  lastMatch(...args: OperationRequestArgs<"openligadb-last-match">): Promise<OperationResponseMap["openligadb-last-match"]>;
  lastTeamMatch(...args: OperationRequestArgs<"openligadb-last-team-match">): Promise<OperationResponseMap["openligadb-last-team-match"]>;
  leagueTeamMatches(...args: OperationRequestArgs<"openligadb-league-team-matches">): Promise<OperationResponseMap["openligadb-league-team-matches"]>;
  leagues(...args: OperationRequestArgs<"openligadb-leagues">): Promise<OperationResponseMap["openligadb-leagues"]>;
  match(...args: OperationRequestArgs<"openligadb-match">): Promise<OperationResponseMap["openligadb-match"]>;
  matchdayMatches(...args: OperationRequestArgs<"openligadb-matchday-matches">): Promise<OperationResponseMap["openligadb-matchday-matches"]>;
  leagueMatches(...args: OperationRequestArgs<"openligadb-league-matches">): Promise<OperationResponseMap["openligadb-league-matches"]>;
  matchesByTeam(...args: OperationRequestArgs<"openligadb-matches-by-team">): Promise<OperationResponseMap["openligadb-matches-by-team"]>;
  matchesByTeamId(...args: OperationRequestArgs<"openligadb-matches-by-team-id">): Promise<OperationResponseMap["openligadb-matches-by-team-id"]>;
  nextMatch(...args: OperationRequestArgs<"openligadb-next-match">): Promise<OperationResponseMap["openligadb-next-match"]>;
  nextTeamMatch(...args: OperationRequestArgs<"openligadb-next-team-match">): Promise<OperationResponseMap["openligadb-next-team-match"]>;
  resultInfos(...args: OperationRequestArgs<"openligadb-result-infos">): Promise<OperationResponseMap["openligadb-result-infos"]>;
  resultTypes(...args: OperationRequestArgs<"openligadb-result-types">): Promise<OperationResponseMap["openligadb-result-types"]>;
  sports(...args: OperationRequestArgs<"openligadb-sports">): Promise<OperationResponseMap["openligadb-sports"]>;
  table(...args: OperationRequestArgs<"openligadb-table">): Promise<OperationResponseMap["openligadb-table"]>;
  teamPairMatches(...args: OperationRequestArgs<"openligadb-team-pair-matches">): Promise<OperationResponseMap["openligadb-team-pair-matches"]>;
  teams(...args: OperationRequestArgs<"openligadb-teams">): Promise<OperationResponseMap["openligadb-teams"]>;
}
export { OpenLigaDBClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default OpenLigaDBClient;
