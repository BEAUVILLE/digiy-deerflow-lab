// Utilisation locale : node run_relais.mjs mission_relais_001.json
import { readFileSync } from 'node:fs';
import { coordonnerRelais } from './relais_agents.mjs';
if (process.argv.length !== 3) { console.error('Usage: node run_relais.mjs <mission.json>'); process.exit(2); }
try {
  const {mission,faits,paquets} = JSON.parse(readFileSync(process.argv[2],'utf8'));
  console.log(JSON.stringify(coordonnerRelais(mission,faits,paquets),null,2));
} catch (err) { console.error('REFUS:',err.message);process.exit(1); }
