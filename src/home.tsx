import { useNavigate } from 'react-router-dom';

function Home() {
  const navigate = useNavigate();

  return (
    <div>
      <h1>Home Page</h1>
      <button onClick={() => navigate('/cuestionarios')}>Ir a Cuestionarios</button>
      <button onClick={() => navigate('/proyectos')}>Ir a Proyectos</button>
      <button onClick={() => navigate('/colaboradores')}>Ir a Colaboradores</button>
    </div>
  );
}

export default Home;
