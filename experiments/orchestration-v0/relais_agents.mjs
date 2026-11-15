// DIGIY V0.1 - aucun appel IA ni action externe.
const ROLES = ["eclaireur","technique","langues"];
const ETATS = ["conforme","a_corriger","impossible_a_verifier"];


function validerMission(mission){
  if(!mission||typeof mission!=="object"||Array.isArray(mission)) throw Error("mission_invalide");
  if(mission.mission_id!=="DIGIY-ORCH-001"||mission.type!=="lecture_seule") throw Error("mission_hors_perimetre");
  if(!Array.isArray(mission.actions_autorisees)||mission.actions_autorisees.length!==0) throw Error("actions_interdites");
  if(mission.cout_supplementaire_autorise!==0||mission.validation_maitre!==false) throw Error("autorisation_non_conforme");
}

function validerPaquet(paquet,index,mission,faits){
  if(!paquet||typeof paquet!=="object"||Array.isArray(paquet)) throw Error("paquet_invalide");
  const champs=["mission_id","role","recu_de","statut","preuves","points_a_verifier","actions_demandees","depense_demandee"];
  if(Object.keys(paquet).some(k=>!champs.includes(k))||champs.some(k=>!Object.hasOwn(paquet,k))) throw Error("schema_de_paquet_invalide");
  const attendu=ROLES[index];
  if(paquet.mission_id!==mission.mission_id||paquet.role!==attendu) throw Error("mission_ou_role_incoherent");
  if(paquet.recu_de!==(index===0?"maitre":ROLES[index-1])) throw Error("transmission_non_valide");
  if(!ETATS.includes(paquet.statut)) throw Error("statut_inconnu");
  if(!Array.isArray(paquet.actions_demandees)||paquet.actions_demandees.length||paquet.depense_demandee!==0)throw Error("action_ou_depense_non_autorisee");
  if(!Array.isArray(paquet.preuves)||!Array.isArray(paquet.points_a_verifier))throw Error("preuves_ou_manquants_invalides");
  if(paquet.preuves.some(id=>typeof id!=="string"||!Object.hasOwn(faits,id)||faits[id].role!==attendu))throw Error("preuve_non_referencee_ou_hors_role");
  if(paquet.points_a_verifier.some(s=>typeof s!=="string"||!s.trim()||s.length>300)) throw Error("manquants_invalides");
  if(paquet.statut!=="impossible_a_verifier"&&paquet.preuves.length===0) throw Error("conclusion_sans_preuve");
  if(paquet.statut==="impossible_a_verifier"&&paquet.points_a_verifier.length===0) throw Error("inconnue_non_decrite");
  return {role:paquet.role,statut:paquet.statut,recu_de:paquet.recu_de,preuves:paquet.preuves,points_a_verifier:paquet.points_a_verifier};
}

function coordonnerRelais(mission,faits,paquets){
  validerMission(mission);
  if(!faits||typeof faits!=="object"||Array.isArray(faits)||!Array.isArray(paquets)||paquets.length!==ROLES.length)throw Error("mission_incomplete");
  for(const [id,fait] of Object.entries(faits)){
    if(!/^[A-Z0-9_]{4,60}$/.test(id)||!fait||typeof fait!=="object"||!ROLES.includes(fait.role)||typeof fait.source!=="string"||!/^https:\/\/github\.com\/BEAUVILLE\//.test(fait.source)) throw Error("catalogue_faits_invalide");
  }
  const rapports=paquets.map((p,i)=>validerPaquet(p,i,mission,faits));
  const statuts=rapports.map(p=>p.statut);
  const verdict=statuts.includes("a_corriger")?"a_corriger":statuts.includes("impossible_a_verifier")?"impossible_a_verifier":"conforme";
  return {mission_id:mission.mission_id,execution:"protocole_de_relais_sur_paquets_fournis_sans_appel_ia",rapports,controleur:{statut:verdict,synthese:"Le rapport ne vaut pas validation des faits ni autorisation d agir."},garde_fous:{publication:false,fusion:false,modification_production:false,envoi_whatsapp:false,depense:false,validation_maitre_requise:true}};
}

export { coordonnerRelais };

