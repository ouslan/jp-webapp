import { Routes, Route } from 'react-router-dom';
import Home from './home'; //  Home component
import Cuestionarios from './cuestionarios'; //  Cuestionarios component
import Proyectos from './proyectos'; //  Cuestionarios component
import Colaboradores from './colaboradores'; //  Cuestionarios component
import JP_541 from  './Forms/yearly/construccion/JP-541';
import JP_304 from  './Forms/quaterly/balanza_de_pagos/JP-304';
import JP_361_qtr from  './Forms/quaterly/balanza_de_pagos/JP-361-qtr';
import JP_362_qtr from  './Forms/quaterly/balanza_de_pagos/JP-362-qtr';
import JP_363_qtr from  './Forms/quaterly/balanza_de_pagos/JP-363-qtr';
import JP_364_qtr from  './Forms/quaterly/balanza_de_pagos/JP-364-qtr';
import JP_375_qtr from  './Forms/quaterly/balanza_de_pagos/JP-375-qtr';
import JP_529_qtr from  './Forms/quaterly/balanza_de_pagos/JP-529-qtr';
import JP_536_2_qtr from  './Forms/quaterly/balanza_de_pagos/JP-536-2-qtr';
import JP_544_qtr from  './Forms/quaterly/balanza_de_pagos/JP-544-qtr';

import IP_110_qtr from  './Forms/quaterly/ingreso_neto/IP-110-qtr';
import IP_210_qtr from  './Forms/quaterly/ingreso_neto/IP-210-qtr';
import IP_220_qtr from  './Forms/quaterly/ingreso_neto/IP-220-qtr';
import IP_230_qtr from  './Forms/quaterly/ingreso_neto/IP-230-qtr';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/cuestionarios" element={<Cuestionarios />} />
      <Route path="/proyectos" element={<Proyectos />} />
      <Route path="/colaboradores" element={<Colaboradores />} />
      <Route path="/JP-541" element={<JP_541 />} />
      <Route path="/JP-304" element={<JP_304 />} />
      <Route path="/JP-361-qtr" element={<JP_361_qtr />} />
      <Route path="/JP-362-qtr" element={<JP_362_qtr />} />
      <Route path="/JP-363-qtr" element={<JP_363_qtr />} />
      <Route path="/JP-364-qtr" element={<JP_364_qtr />} />
      <Route path="/JP-375-qtr" element={<JP_375_qtr />} />
      <Route path="/JP-529-qtr" element={<JP_529_qtr />} />
      <Route path="/JP-536-2-qtr" element={<JP_536_2_qtr />} />
      <Route path="/JP-544-qtr" element={<JP_544_qtr />} />

      <Route path="/IP-110-qtr" element={<IP_110_qtr />} />
      <Route path="/IP-210-qtr" element={<IP_210_qtr />} />
      <Route path="/IP-220-qtr" element={<IP_220_qtr />} />
      <Route path="/IP-230-qtr" element={<IP_230_qtr />} />


    </Routes>
  );
}

export default App;
