// DIGIY V0.2 : analyse de paquets ; aucune API, aucune action externe.


function verifierDossier(d){
 if(!d||typeof d!=="object"||Array.isArray(d)||d.mission_id!=="DIGIY-ORCH-001"||d.mode!=="lecture_seule"||d.budget_supplementaire!==0||!Array.isArray(d.autorisations)||d.autorisations.length)throw Error("Mission non autorisee");
 if(!Array.isArray(d.sujets)||d.sujets.length<1||new Set(d.sujets).size!==d.sujets.length||d.sujets.some(x=>typeof x!=="string"||!/^[A-Z_0-9]+$/.test(x)))throw Error("Sujets invalides");
 if(!d.sources||typeof d.sources!=="object"||Array.isArray(d.sources)||!Object.keys(d.sources).length)throw Error("Catalogue absent");
 for(const [k,v] of Object.entries(d.sources)){
  if(!/^[A-Z_0-9]+$/.test(k)||!v||typeof v.url!=="string"||!v.url.startsWith("https://github.com/BEAUVILLE/"))throw Error("Source non autorisee");
 }
 if(!Array.isArray(d.sorties)||d.sorties.length!==2)throw Error("Deux sorties distinctes requises");
 const identites=new Set(),runs=new Set(),statuses=["conforme","a_corriger","inconnu"];
 for(const a of d.sorties){
  if(!a||typeof a!=="object"||typeof a.agent_id!=="string"||typeof a.run_id!=="string"||a.agent_id.length<3||a.run_id.length<6)throw Error("Identite manquante");
  if(identites.has(a.agent_id)||runs.has(a.run_id))throw Error("Sessions non distinctes");
  identites.add(a.agent_id);runs.add(a.run_id);
  if(!["simulation_test","modele_externe_non_verifie"].includes(a.type_execution))throw Error("Origine non supportee");
  if(a.type_execution==="simulation_test"&&a.modele!==null)throw Error("Simulation ne doit pas pretendre etre un modele");
  if(a.type_execution==="modele_externe_non_verifie"&&(typeof a.modele!=="string"||a.modele.length<3))throw Error("Modele non declare");
  if(!Array.isArray(a.actions_demandees)||a.actions_demandees.length||a.cout_demande!==0)throw Error("Actions ou depenses interdites");
  if(!Array.isArray(a.observations)||a.observations.length!==d.sujets.length)throw Error("Couverture incomplete");
  const notes=new Set();
  for(const o of a.observations){
   if(!o||!d.sujets.includes(o.sujet)||notes.has(o.sujet)||!statuses.includes(o.statut)||!Array.isArray(o.preuve_ids)||!o.preuve_ids.length||o.preuve_ids.some(id=>!Object.hasOwn(d.sources,id))||typeof o.note!=="string"||o.note.trim().length<10||o.note.length>800)throw Error("Observation invalide");
   notes.add(o.sujet);
  }
 }
 return true;
}

function confrontation(d){
 verifierDossier(d);
 const synthese=d.sujets.map(sujet=>{
  const a=d.sorties[0].observations.find(o=>o.sujet===sujet);
  const b=d.sorties[1].observations.find(o=>o.sujet===sujet);
  const status=a.statut===b.statut?a.statut:"discordance";
  return {sujet,verdict:status,statuts_des_deux:[a.statut,b.statut],preuves_declares:[...new Set([...a.preuve_ids,...b.preuve_ids])],validation_independante_des_preuves:false};
 });
 const conflict=synthese.some(x=>x.verdict==="discordance"),corr=synthese.some(x=>x.verdict==="a_corriger"),unk=synthese.some(x=>x.verdict==="inconnu");
 const verdict=conflict?"a_arbitrer":corr?"a_corriger":"a_verifier"; // Sans preuves independantes, aucune conformite definitive.
 const simulation=d.sorties.some(x=>x.type_execution==="simulation_test");
 return {
  mission_id:d.mission_id,execution:simulation?"essai_sur_sorties_synthetiques":"sorties_modele_fournies_non_authentifiees",
  avis:{verdict,sujets:synthese},preuves_verifiees_independamment:false,realite_agents_ia_prouvee:false,
  avertissement:simulation?"Les paquets sont fictifs : aucun agent IA externe n'a ete execute.":"Les declarations de provenance de modeles ne prouvent ni independance ni execution reelle.",
  decisions:{publier:false,fusionner:false,payer:false,contacter:false,validation_du_maitre_requise:true}
 };
}

export { confrontation, verifierDossier };

