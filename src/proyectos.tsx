import React from "react";
import { Routes, Route, useNavigate } from "react-router-dom";
import ProductHts from "./Proyects/product_hts"; // Importa el componente correctamente

function Proyectos() {
  const navigate = useNavigate();

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif", color: "black" }}>
      <h1>Proyectos</h1>
      <button onClick={() => navigate("/")}>Ir a Inicio</button>
      <button onClick={() => navigate("/cuestionarios")}>Ir a Cuestionarios</button>
      <button onClick={() => navigate("/colaboradores")}>Ir a Colaboradores</button>
      <button onClick={() => navigate("/proyectos/products_hts")}>Ir a Productos HTS</button>

      {/* Definir las rutas dentro de Proyectos */}
      <Routes>
        <Route path="products_hts" element={<ProductHts />} />
      </Routes>
    </div>
  );
}

export default Proyectos;
