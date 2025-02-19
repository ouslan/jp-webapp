import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import "../styles/product_hts.css";

const ProductHTS: React.FC = () => {
  const navigate = useNavigate();
  const [frequency, setFrequency] = useState('yearly');
  const [htsCode, setHtsCode] = useState('');
  const [tradeType, setTradeType] = useState('imports');

  const htsCodes = ['1234', '5678', '91011']; // Simulated data, replace with API call if needed

  const handleFrequencyChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setFrequency(e.target.value);
  };

  const handleHtsCodeChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setHtsCode(e.target.value);
  };

  const handleTradeTypeChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setTradeType(e.target.value);
  };

  return (
    <div className="container">
      {/* Burger Menu */}
      <div className="burger" onClick={() => console.log('Toggle menu')}> {/* Implement menu toggle */}
        <span></span>
        <span></span>
        <span></span>
      </div>
      {/* <ul className="burger_menu">
        <li><a href="/">Inicio</a></li>
        <li><a href="/centro-de-datos-macroeconomicos/">Centro de Datos Macroeconómicos</a></li>
        <li><a href="/ciclos-economicos/">Ciclos Económicos</a></li>
        <li><a href="/indicadores-mensuales/">Indicadores Mensuales</a></li>
        <li><a href="/datos-demograficos/">Datos Demográficos</a></li>
      </ul> */}

      <main>
        <section>
          <h1>Productos HTS</h1>
          <p>
          El Sistema Armonizado de Designación y Codificación de Mercancías (HTS, por sus siglas en inglés) 
          es utilizado en Puerto Rico para clasificar los productos que ingresan y salen del país. Este sistema, 
          basado en estándares internacionales, facilita el comercio y asegura que los productos sean gravados 
          correctamente de acuerdo con su tipo. En esta sección, encontrarás información detallada sobre los 
          productos HTS, sus códigos correspondientes y las tasas aplicables en el comercio exterior. Además, 
          se incluyen reportes y estadísticas que reflejan las transacciones comerciales de Puerto Rico, contribuyendo 
          a la planificación económica y fiscal del país.
          </p>
        </section>

        <form id="hts-form">
          <div className="graph_container">
            <h1 id="graph_title">HTS Data</h1>
            <section id="buttons">
              <section id="dropdowns">
                <label htmlFor="frequency">Frecuencia:</label>
                <select name="frequency" id="frequency" value={frequency} onChange={handleFrequencyChange}>
                  <option value="yearly">Yearly</option>
                  <option value="monthly">Monthly</option>
                  <option value="qrt">Quarterly</option>
                  <option value="fiscal">Fiscal</option>
                </select>
              </section>
              <section id="dropdowns">
                <label htmlFor="hts_code">HTS Code:</label>
                <select name="hts_code" id="hts_code" value={htsCode} onChange={handleHtsCodeChange}>
                  {htsCodes.map((code) => (
                    <option key={code} value={code}>{code}</option>
                  ))}
                </select>
              </section>
              <section id="dropdowns">
                <label htmlFor="trade_type">Trade Type:</label>
                <select name="trade_type" id="trade_type" value={tradeType} onChange={handleTradeTypeChange}>
                  <option value="imports">Imports</option>
                  <option value="exports">Exports</option>
                </select>
              </section>
              <button id="submit" type="submit">Submit</button>
            </section>
          </div>

          <div className="download_container">
            <a href="https://api.econlabs.net/files/trade/jp/?types=hts&agg=yearly&agr=false&group=false" className="button">Descargar Datos Anuales</a>
            <a href="https://api.econlabs.net/files/trade/jp/?types=hts&agg=qrt&agr=false&group=false" className="button">Descargar Datos Trimestrales</a>
            <a href="https://api.econlabs.net/files/trade/jp/?types=hts&agg=monthly&agr=false&group=false" className="button">Descargar Datos Mensuales</a>
          </div>
        </form>
      </main>
    </div>
  );
};

export default ProductHTS;
