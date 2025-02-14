import React, { useState, useEffect } from "react";
import vegaEmbed from "vega-embed";
import "../css/website.css"; // Adjust path as needed
import "../css/indice.css"; // Adjust path as needed
import hdiRoadMap from "../assets/hdiRoadMap.png";

import logo from "../assets/gobierno_de_puerto_rico.png";

const HumanDevelopmentIndex: React.FC = () => {
  const [menuOpen, setMenuOpen] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Toggle burger menu
  const toggleBurgerMenu = () => {
    setMenuOpen(!menuOpen);
  };

  // Load Vega-Lite JSON from a static file
  useEffect(() => {
    fetch("/graphics/chart.json")
      .then((response) => response.json())
      .then((spec) => {
        <div id="vis"></div>
        vegaEmbed("#vis", spec)
          .then((result) => console.log("Graph rendered!", result.view))
          .catch((error) => console.error("Error rendering graph:", error));
      })
      .catch((error) => {
        setError("Failed to load the chart. Please try again later.");
        console.error("Error fetching chart:", error);
      });
  }, []);

  return (
    <>
      {/* Burger Menu */}
      <div className="container">
        <div className={`burger ${menuOpen ? "open" : ""}`} onClick={toggleBurgerMenu}>
          <span />
          <span />
          <span />
        </div>

        <ul className={`burger_menu ${menuOpen ? "open" : ""}`}>
          <li><a href="/">Home</a></li>
          <li><a href="/centro-de-datos-macroeconomicos/">Centro De Datos Macroeconómicos</a></li>
          <li><a href="/ciclos-economicos/">Ciclos Económicos</a></li>
          <li><a href="/indicadores-mensuales/">Indicadores Mensuales</a></li>
          <li><a href="/datos-demograficos/">Datos Demográficos</a></li>
        </ul>
      </div>

      <h1>Índice de Desarrollo Humano</h1>

      <p className="main_content">
        El Índice de Desarrollo Humano (IDH) es una medida compuesta que evalúa el desarrollo de un país basado en tres dimensiones clave: una vida larga y saludable, el acceso a la educación y un nivel de vida digno. 
        Creado por el Programa de las Naciones Unidas para el Desarrollo (PNUD), su objetivo es proporcionar una visión más integral del desarrollo que va más allá de los indicadores económicos tradicionales como el Producto Interno Bruto (PIB) per cápita.
      </p>

      {/* IDH Explanation */}
      <p className="main_content"><strong>1. Salud:</strong> medida por la <strong>esperanza</strong> de vida al nacer.</p>
      <p className="main_content"><strong>2. Educación:</strong> evaluada por los <strong>años promedio de escolaridad</strong> en adultos y los <strong>años esperados de escolarización</strong> para niños.</p>
      <p className="main_content"><strong>3. Nivel de vida:</strong> representado por el <strong>ingreso nacional bruto (INB) per cápita</strong>, ajustado para reflejar la disminución de la utilidad del ingreso a niveles más altos.</p>

      {/* IDH Hoja de Ruta */}
      <section>
        <div>
          <h2>Hoja de ruta del Índice de Desarrollo Humano</h2>
          <div className="image-container">
            <img src={hdiRoadMap} alt="Hoja de ruta del Índice de Desarrollo Humano" className="responsive-image" />
          </div>
          <p className="image_subtitle">
            <a href="https://hdr.undp.org/data-center/human-development-index#/indicies/HDI" target="_blank" rel="noopener noreferrer">
              Programa de las Naciones Unidas para el Desarrollo (PNUD)
            </a>
          </p>
        </div>
      </section>

      {/* 📊 Vega-Lite Chart Section */}
      <section>
        <div>
          <h2>Gráfica</h2>
          {error ? (
            <p style={{ color: "red" }}>{error}</p>
          ) : (
            <section style={{ display: "flex", justifyContent: "center", alignItems: "center", height: "100vh", width: "100%" }}>
            <div id="vis" style={{ width: "80vw", height: "80vh" }}></div>       {/*  Vega-Lite Chart will render here */}
            </section> )}    

        </div>
      </section>

      {/* Footer (No Changes) */}  
                  {/* ------------------ FOOTER --------------------- */}
        <footer>
          <main>
            <section>
              <h1>Contáctanos</h1>
            </section>
            <section>
              <div className="footer-container">
                <div className="left-container">
                  <h2>Oficiales de Información <br /> (Ley 141-2019)</h2>
                  <p>
                    Sr. Edgardo Vázquez Rivera <br />
                    Secretario Oficina de Secretaría <br />
                    <a href="mailto:Vazquez_e@jp.pr.gov" className="custom-link">Vazquez_e@jp.pr.gov</a> <br />
                    787 723-6200 ext. 16637 <br /><br />
                    Plan. Erika Rivera Felicié <br />
                    Ayudante Especial <br />
                    <a href="mailto:ivera_e1@jp.pr.gov" className="custom-link">ivera_e1@jp.pr.gov</a> <br /><br />
                    Lcda Aida Silver Cintrón <br />
                    Abogada Oficina Asuntos Legales <br />
                    <a href="mailto:Silver_A@jp.pr.gov" className="custom-link">Silver_A@jp.pr.gov</a> <br />
                    787 723-6200 ext. 16016
                  </p>
                  <h2>Oficina de Datos PRITS</h2>
                  <p>
                    Carlos Castillo Domena <br />
                    Director Oficina de Administración Interna <br />
                    <a href="mailto:castillo_r@jp.pr.gov" className="custom-link">castillo_r@jp.pr.gov</a> <br />
                    787 723-6200 ext. 16019 <br /><br />
                    <a href="https://jppr.sharepoint.com/sites/BibliotecaDigital" className="custom-link">BDV (Uso interno)</a>
                  </p>
                </div>
                <div className="right-container">
                  <h2><strong>Dirección Postal</strong></h2>
                  <p>
                    PO Box 4119 <br />
                    San Juan P.R. 00940-1119 <br />
                    Tel: (787) 723-6200 (Cuadro)<br />
                  </p><h2><strong>Dirección Física</strong></h2>
                  <p>
                    Centro Gubernamental<br />
                    Roberto Sánchez Vilella<br />
                    Ave. De Diego, Pda 22, <br />
                    Santurce<br />
                  </p>
                  <p />
                  <section className="maps">
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3784.7501887340845!2d-66.0698374248245!3d18.
                                            449648171336893!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8c036f497801a7b7%3A0x68ace32a0663b72f!2sGov
                                            ernor%20Roberto%20S%C3%A1nchez%20Vilella%20Government%20Center!5e0!3m2!1sen!2sus!4v1717000266481!5m2!1sen!2sus" width={490} height={200} style={{border: 0}} allowFullScreen loading="lazy" referrerPolicy="no-referrer-when-downgrade">
                    </iframe>
                  </section>
                </div>
              </div>
            </section>
          </main>
        </footer>
         {/* ------------------ END OF FOOTER --------------------- */}

    </>
  );
};

export default HumanDevelopmentIndex;





