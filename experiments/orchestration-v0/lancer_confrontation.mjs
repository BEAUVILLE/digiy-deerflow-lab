import fs from 'node:fs';
import { confrontation } from './confrontation_agents.mjs';
if (process.argv.length!==3){ console.error('Usage: node lancer_confrontation.mjs <dossier.json>');process.exit(2); }
try{ const o=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));console.log(JSON.stringify(confrontation(o),null,2)); }catch(e){console.error('REFUS:',e.message);process.exit(1);}
