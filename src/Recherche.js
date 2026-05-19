import './Recherche.css';

function Recherche({ valeur, onChange }) {
  return (
    <div className="recherche">
      <input
        type="text"
        className="recherche-input"
        placeholder="Rechercher une ligne (depart, arrivee)..."
        value={valeur}
        onChange={e => onChange(e.target.value)}
      />
      <input
        type="button"
        value="Effacer"
        onClick={() => onChange("")}
        style={{
          background: "#000000b8",
          fontSize: "1rem",
          fontWeight: 600,
          color: "white",
          marginTop: "10px",
          marginLeft: "5px",
          padding: "5px 10px",
          borderRadius: "5px",
        }}
      />
    </div>
  );
}

export default Recherche;