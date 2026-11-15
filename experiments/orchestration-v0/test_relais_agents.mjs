import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { coordonnerRelais } from './relais_agents.mjs';
const original=JSON.parse(readFileSync(new URL('./mission_relais_001.json',import.meta.url),'utf8'));
const copie=()=>structuredClone(original);
test('pipeline conclut a_corriger et maintient le blocage',()=>{
 const {mission,faits,paquets}=copie();const r=coordonnerRelais(mission,faits,paquets);
 assert.equal(r.controleur.statut,'a_corriger');assert.equal(r.garde_fous.fusion,false);
 assert.equal(r.garde_fous.validation_maitre_requise,true);
 assert.match(r.execution,/sans_appel_ia/);
});
test('handoff incorrect refuse',()=>{
 const {mission,faits,paquets}=copie();paquets[1].recu_de='maitre';
 assert.throws(()=>coordonnerRelais(mission,faits,paquets),/transmission_non_valide/);
});
test('preuve dun autre role refusee',()=>{
 const {mission,faits,paquets}=copie();paquets[2].preuves=['PR204_ETAT'];
 assert.throws(()=>coordonnerRelais(mission,faits,paquets),/preuve_non_referencee/);
});
test('action ou depense refusee',()=>{
 const a=copie();a.paquets[1].actions_demandees=['publier'];
 assert.throws(()=>coordonnerRelais(a.mission,a.faits,a.paquets),/action_ou_depense_non_autorisee/);
 const b=copie();b.paquets[2].depense_demandee=1;
 assert.throws(()=>coordonnerRelais(b.mission,b.faits,b.paquets),/action_ou_depense_non_autorisee/);
});
test('rapport absent refuse',()=>{
 const {mission,faits,paquets}=copie();
 assert.throws(()=>coordonnerRelais(mission,faits,paquets.slice(0,2)),/mission_incomplete/);
});
test('incertitude ne peut etre cachee',()=>{
 const {mission,faits,paquets}=copie();paquets[1].points_a_verifier=[];
 assert.throws(()=>coordonnerRelais(mission,faits,paquets),/inconnue_non_decrite/);
});
test('absence de validation MAITRE reste bloquante',()=>{
 const {mission,faits,paquets}=copie();mission.validation_maitre=true;
 assert.throws(()=>coordonnerRelais(mission,faits,paquets),/autorisation_non_conforme/);
});
