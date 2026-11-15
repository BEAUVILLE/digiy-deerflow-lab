import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { confrontation } from './confrontation_agents.mjs';
const fixture=JSON.parse(fs.readFileSync(new URL('./deux_sorties_SYNTHETIQUES.json',import.meta.url),'utf8'));
const clone=()=>structuredClone(fixture);
test('deux avis conformes ne permettent pas validation sans preuve independante',()=>{
  const d=clone();
  d.sorties.forEach(a=>a.observations.forEach(o=>o.statut='conforme'));
  const r=confrontation(d);
  assert.equal(r.avis.verdict,'a_verifier');
  assert.equal(r.preuves_verifiees_independamment,false);
  assert.equal(r.decisions.fusionner,false);
  assert.equal(r.decisions.validation_du_maitre_requise,true);
});
test('deux noms de modele declares ne prouvent pas deux executions IA',()=>{
  const d=clone();
  d.sorties[0].type_execution='modele_externe_non_verifie';
  d.sorties[0].modele='modele-a-declare';
  d.sorties[1].type_execution='modele_externe_non_verifie';
  d.sorties[1].modele='modele-b-declare';
  const r=confrontation(d);
  assert.equal(r.realite_agents_ia_prouvee,false);
  assert.equal(r.preuves_verifiees_independamment,false);
});
test('accord sans reserve ne supprime jamais le blocage de publication',()=>{
  const d=clone();
  d.sorties.forEach(a=>a.observations.forEach(o=>o.statut='conforme'));
  const r=confrontation(d);
  assert.equal(r.decisions.publier,false);
  assert.equal(r.decisions.contacter,false);
  assert.equal(r.decisions.payer,false);
});
