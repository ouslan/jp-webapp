import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';

function Proyectos() {
  const navigate = useNavigate();

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Proyectos</h1>

      {/* Buttons using useNavigate */}
      <button onClick={() => navigate('/')}>Ir a Inicio</button>
      <button onClick={() => navigate('/colaboradores')}>Ir a Colaboradores</button>

      <div>
          <div style={{ marginTop: '20px' }}>
            <Link to="/product_hts">Productos HTS</Link>
          </div>
      </div>
    </div>

  );
}

export default Proyectos;