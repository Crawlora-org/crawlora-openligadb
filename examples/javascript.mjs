import { OpenLigaDBClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new OpenLigaDBClient({ apiKey });

  const leagues = await client.leagues({ season: 2026 });
  console.log("leagues", leagues);
  const sports = await client.sports({  });
  console.log("sports", sports);
  const resultTypes = await client.resultTypes({  });
  console.log("resultTypes", resultTypes);
