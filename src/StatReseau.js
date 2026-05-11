import './StatReseau.css';

function StatReseau({ lignes }) {
  const totalLignes = lignes.length;
  const totalArrets = lignes.reduce((somme, ligne) => somme + ligne.arrets, 0);
  const ligneMax = lignes.reduce((max, ligne) => 
    (ligne.arrets > max.arrets) ? ligne : max, lignes[0]
  );

  return (
    <div className='affich'>
      <div>
        <strong>Total Lignes :</strong> {totalLignes}
      </div>
      <div>
        <strong>Total Arrêts :</strong> {totalArrets}
      </div>
      <div>
        <strong>Ligne avec le plus d'arrêts:</strong>
        Ligne {ligneMax.numero} ({ligneMax.arrets} arrêts)
      </div>
    </div>
  );
}

export default StatReseau;