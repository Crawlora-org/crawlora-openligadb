import { OpenLigaDBClient } from "../src/index.js";

const client = new OpenLigaDBClient({ apiKey: "test-key" });
void client.currentGroup({"league_shortcut": "sample"});
void client.request("openligadb-current-group", {"league_shortcut": "sample"});
const streamResponse: Promise<Response> = client.request("openligadb-current-group", {"league_shortcut": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("openligadb-current-group", {"league_shortcut": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.currentGroup({"league_shortcut": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("openligadb-current-group", {"league_shortcut": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("openligadb-current-group", {"league_shortcut": "sample"}, { responseType: "text" });
void rawText;


void client.leagues();
void client.request("openligadb-leagues");
// @ts-expect-error The selected operation requires its documented params.
void client.currentGroup();
