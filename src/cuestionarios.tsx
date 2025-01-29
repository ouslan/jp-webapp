import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';

function Cuestionarios() {
  const navigate = useNavigate();

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Cuestionarios</h1>

      {/* Buttons using useNavigate */}
      <button onClick={() => navigate('/')}>Ir a Inicio</button>
      <button onClick={() => navigate('/proyectos')}>Ir a Proyectos</button>
      <button onClick={() => navigate('/colaboradores')}>Ir a Colaboradores</button>

      <div>
        
        <h2>Construcción</h2>

          {/* Link to Form JP_541 */}
          <div style={{ marginTop: '20px' }}>
            <Link to="/JP-541">Encuesta sobre el Valor de la Inversión en Obras de Construcción</Link>
          </div>

        <h2>Balanza de Pagos Quaterly</h2>

          {/* Links to quaterly BP Forms */}
          <div style={{ marginTop: '20px' }}>
            <Link to="/JP-304">JP-304</Link></div>
    
          <div style={{ marginTop: '20px' }}>
            <Link to="/JP-361-qtr">JP-361-qtr</Link></div>
          

          <div style={{ marginTop: '20px' }}>
            <Link to="/JP-362-qtr">JP-362-qtr</Link></div>

          <div style={{ marginTop: '20px' }}>
            <Link to="/JP-363-qtr">JP-363-qtr</Link></div>

          <div style={{ marginTop: '20px' }}>
            <Link to="/JP-364-qtr">JP-364-qtr</Link></div>

          <div style={{ marginTop: '20px' }}>
            <Link to="/JP-375-qtr">JP-375-qtr</Link></div>

          <div style={{ marginTop: '20px' }}>
            <Link to="/JP-529-qtr">JP-529-qtr</Link></div>

          <div style={{ marginTop: '20px' }}>
            <Link to="/JP-536-2-qtr">JP-536-2-qtr</Link></div>
          
          <div style={{ marginTop: '20px' }}>
            <Link to="/JP-544-qtr">JP-544-qtr</Link></div>

          <h2>Ingreso Neto Quaterly</h2>

          {/* Links to quaterly BP Forms */}

          <div style={{ marginTop: '20px' }}>
            <Link to="/IP-110-qtr">IP-110-qtr</Link></div>

          <div style={{ marginTop: '20px' }}>
            <Link to="/IP-210-qtr">IP-210-qtr</Link></div>

          <div style={{ marginTop: '20px' }}>
            <Link to="/IP-220-qtr">IP-220-qtr</Link></div>

          <div style={{ marginTop: '20px' }}>
            <Link to="/IP-230-qtr">IP-230-qtr</Link></div>


      </div>

    </div>

  );
}

export default Cuestionarios;