import React from 'react';
import { Route, useNavigate } from 'react-router-dom';

import Product_hts from './Proyects/product_hts';

function Proyectos() {
  const navigate = useNavigate();

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif', color: 'black' }}>
      <h1>Proyectos</h1>

      <button onClick={() => navigate('/')}>Ir a Inicio</button>
      <button onClick={() => navigate('/cuestionarios')}>Ir a Cuestionarios</button>
      <button onClick={() => navigate('/colaboradores')}>Ir a Colaboradores</button>

      <Route path="/products_hts" element={<Product_hts />} />

    </div>
  );
}

export default Proyectos;