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
        
        <h2 style={{ textAlign: 'center'}}>Construcción</h2>

          {/* Link to Form JP_541 */}
          <div style={{ marginTop: '20px', textAlign: 'center'}}>
            <Link to="/JP-541">Encuesta sobre el Valor de la Inversión en Obras de Construcción</Link>
          </div>

        
        <h2 style={{ textAlign: 'center'}}>Balanza de Pagos</h2>

          {/* Links to yearly BP Forms */}

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-304">JP-304 Relación de Aportaciones Federales</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-361">JP-361 Transactions in Puerto Rico of External Insurance Companies</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-362">JP-362 Transacciones con el Exterior para la Balanza de Pagos de Puerto Rico</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-363">JP-363 Investment in Securities of the Central Government</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-364">JP-364 Información sobre Compañías de Seguros de Puerto Rico</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
          <Link to="/JP-375"> Encuesta sobre el Valor Pendiente de Pago de Hipotecas sobre Viviendas</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-383">JP-383 Informe Mensual de los Pagos de Asistencia y Reducción de Intereses en Hipotecas FHA</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
          <Link to="/JP-529">JP-529 Relación de Aportaciones y Donativos Federales Recibidos</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
          <Link to="/JP-536-2">JP-536.2 Información para el Producto Bruto</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-544">JP-544 Información para la Balanza de Pagos</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-544-1">JP-544.1 Instrucciones</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-544-2">JP-544.2 Relación de Aportaciones Federales Recibidas - Universidades y Colegios</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-547">JP-547 Federal Government Agency Transactions in Puerto Rico</Link></div>

          {/* Links to Quarterly BP Forms */}

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-361-qtr">JP-361 Transactions in Puerto Rico of External Insurance Companies (Quarterly)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-362-qtr">JP-362 Transacciones con el Exterior para la Balanza de Puerto Rico (Quarterly)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-363-qtr">JP-363 Investment in Securities of the Central Goverment (Quarterly)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-364-qtr">JP-364 Información sobre Compañías de Seguros de Puerto Rico (Quarterly)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-375-qtr">JP-375 Encuesta sobre el Valor Pendiente de Pago de Hipotecas sobre Viviendas (Quarterly)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-529-qtr">JP-529 Relación de Aportaciones y Donativos Federales Recibidos (Quarterly)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-536-2-qtr">JP-536.2 Información para el Producto Bruto (Quarterly)</Link></div>
          
          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-544-qtr">JP-544 Información para la Balanza de Pagos (Quarterly)</Link></div>

        <h2 style={{ textAlign: 'center'}}>Ingreso Neto</h2>

          {/* Links to Quarterly IP Forms */}

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-110">IP-110 Agricultura (Agriculture)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-210">IP-210 Minería (Mining)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-220">IP-220 Utilidades (Utilities)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-230">IP-230 Construcción (Construction)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-310">IP-310 Manufactura (Manufacture)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-310b">IP-310b Manufactura de Bebidas (Beverage Manufacturing)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-420">IP-420 Comercio al Por Mayor (Wholesalers)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-440">IP-440 Comercio al Detal (Retail Trade)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-440g">IP-440g Estaciones De Gasolina (Gas Stations)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-480">IP-480 Transportación (Transportation)</Link></div>

            <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-480a">IP-480a Transportación Aérea (Air Transportation)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-490">IP-490 Correos y Mensajeros (Couriers and Messengers)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-510">IP-510 Informática (Information)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-520">IP-520 Finanzas y Seguros (Finance and Insurance)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-520a">IP-520a Agencias, Corretajes y Otros Seguros Relacionados (Agencies, Brokerages, and Related Insurance)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-520s">IP-520s Empresas Aseguradoras y Actividades Relacionadas (Insurance Carriers and Related Activities)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-530">IP-530 Inmobiliaria y Arrendamientos (Real Estate and Rental)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-540">IP-540 Servicios Profesionales, Científicos y Ténicos (Professional, Scientific, and Technical Services)</Link></div> 
            
          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-540J">IP-540J Administración de Empresas (Business Administration)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-540P">IP-540P Organización de Viajes y Servicios de Reservación (Travel Arrangement and Reservation Services)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-540S">IP-540S Servicios Administrativos y de Apoyo</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-540a">IP-540a Publicidad y Servicios Relacionados (Advertising and Related Services)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-540v">IP-540v Veterinarios y Otros Servicios para Animales (Veterinarians and Other Services for Animals)</Link></div>
          
          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-610">IP-610 Servicios de Educación (Education Services)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-620">IP-620 Servicios de Salud (Health Care Services)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-710">IP-710 Arte, Entretenimiento y Recreación (Art, Entertainment, and Recreation)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-720">IP-720 Alojamiento y Servicios de Comida (Accommodation and Food Services)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-810">IP-810 Otros Servicios (Other Services)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-560-63110">JP-560-63110 Seguros Domésticos de Vida</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-560-63111">JP-560-63111 Organizaciones de Servicios de Salud</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-560-63210">JP-560-63210 Seguros Domésticos de Propiedad y Contingencia</Link></div>
            
          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/JP-560-2">JP-560.2 Preliminar (Preliminary)</Link></div>

          {/* Links to Quarterly IP Forms */}

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-110-qtr">IP-110 Agricultura (Agriculture) (Quarterly)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-210-qtr">IP-210 Minería (Mining) (Quarterly)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-220-qtr">IP-220 Utilidades (Utilities) (Quarterly)</Link></div>

          <div style={{ marginTop: '20px' ,  textAlign: 'center'}}>
            <Link to="/IP-230-qtr">IP-230 Construcción (Construction) (Quarterly)</Link></div>

      </div>

    </div>

  );
}

export default Cuestionarios;