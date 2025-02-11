import React, { Component, useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Cuestionario_Inovacion_Desarrollo() {

  const CheckboxGroup9 = () => {  
    const [selected, setSelected] = useState<string[]>([]);
    const [otherText, setOtherText] = useState('');
    const options = ["Fondos Propios", "Subvenciones gubernamentales", "Préstamos bancarios", "Inversionistas externos", "Otros: "];
    return(
      <>
        {options.map((option)=>(
          <li key={option}>
            <label>
              <input 
                type="checkbox" 
                value={options} 
                checked={selected.includes(option)} 
                onChange={() => setSelected(prev => prev.includes(option) ? prev.filter(o => o !== option) : [...prev, option])}  
              />
              {option}
            </label>

            {option === "Otros: " && selected.includes("Otros: ") && (
              <input
                type="text"
                placeholder='Especifique...'
                value={otherText}
                onChange={(e) => setOtherText(e.target.value)}
              />
            )}
          </li>
        ))}
      </>
    );
  };

  const CheckboxGroup12 = () => {  
    const [selected, setSelected] = useState<string[]>([]);
    const options = ["Patentes registradas", "Modelos de utilidad", "Diseños industriales", "Software desarollado", "Publicaciones científicas", "Prototipos desarrollados"];
    return(
      <>
        {options.map((option)=>(
          <li key={option}>
            <label>
              <input 
                type="checkbox" 
                value={options} 
                checked={selected.includes(option)} 
                onChange={() => setSelected(prev => prev.includes(option) ? prev.filter(o => o !== option) : [...prev, option])}  
              />
              {option}
            </label>
          </li>
        ))}
      </>
    );
  };

  const CheckboxGroup14 = () => {  
    const [selected, setSelected] = useState<string[]>([]);
    const options = ["Mejora en la calidad de productos/servicios", "Reducción de costos", "Expansión de mercado", "Incremento en ingresos", "Fortalecimiento de la imagen de la empresa"];
    return(
      <>
        {options.map((option)=>(
          <li key={option}>
            <label>
              <input 
                type="checkbox" 
                value={options} 
                checked={selected.includes(option)} 
                onChange={() => setSelected(prev => prev.includes(option) ? prev.filter(o => o !== option) : [...prev, option])}  
              />
              {option}
            </label>
          </li>
        ))}
      </>
    );
  };

  const CheckboxGroup18 = () => {  
    const [selected, setSelected] = useState<string[]>([]);
    const options = ["Universidades", "Centros de investigación", "Otras empresas nacionales", "Otras empresas internacionales", "Organismos gubernamentales"];
    return(
      <>
        {options.map((option)=>(
          <li key={option}>
            <label>
              <input 
                type="checkbox" 
                value={options} 
                checked={selected.includes(option)} 
                onChange={() => setSelected(prev => prev.includes(option) ? prev.filter(o => o !== option) : [...prev, option])}  
              />
              {option}
            </label>
          </li>
        ))}
      </>
    );
  };

  const CheckboxGroup20 = () => {  
    const [selected, setSelected] = useState<string[]>([]);
    const [otherText, setOtherText] = useState('');
    const options = ["Falta de financiamiento", "Falta de personal capacitado", "Incertidumbre en los resultados", "Altos costos de inversión", "Regulaciones gubernamentales", "Otros: "];
    return(
      <ul>
        {options.map((option)=>(
          <li key={option}>
            <label>
              <input 
                type="checkbox" 
                value={options} 
                checked={selected.includes(option)} 
                onChange={() => 
                  setSelected(prev => 
                    prev.includes(option) 
                      ? prev.filter(o => o !== option)
                      : prev.length < 3
                      ? [...prev, option]
                      : prev
                  )
                }  
              />    
              {option}
            </label>
            {option === "Otros: " && selected.includes("Otros: ") && (
              <input
                type="text"
                placeholder='Especifique...'
                value={otherText}
                onChange={(e) => setOtherText(e.target.value)}
              />
            )}
          </li>
        ))}
      </ul>
    );
  };

  const navigate = useNavigate();
  return (
    
    <div style={{ position: 'absolute', top: '0', left: '0', padding: '10px', fontFamily: 'Arial, sans-serif' }}>
      <h2>CUESTIONARIO DE MEDICIÓN DE I+D EN ACTIVOS INTANGIBLES</h2>
      <h3>I. Información General de la Empresa</h3>
      <ol>
        <li> {/* 1 */}
          <label hmtl-For='company-name'>Nombre de la empresa: </label>
          <input type='text' id='company-name' placeholder="Texto aqui..." /> 
        </li>
        <li> {/* 2 */}
          <label hmtl-For='ein'>Numero EIN: </label>
          <input type='text' id='ein' placeholder="Texto aqui..." /> 
        </li>
        <li> {/* 3 */}
          <label hmtl-For='naics'>Código NAICS de la empresa: </label>
          <input type='text' id='naics' placeholder="Texto aqui..." /> 
        </li>
        <li> {/* 4 */}
          <label hmtl-For='company-size'>Tamaño de la empresa: </label>
          <select id='company-size' name='company-size'>
            <option value='micro'>Micro (1-10 empleados)</option>
            <option value='small'>Pequeña (11-50 empleados)</option>
            <option value='medium'>Mediana (51-250 empleados)</option>
            <option value='large'>Grande (Más de 250 empleados)</option>   
          </select>
        </li>
        <li> {/* 5 */}
          <label hmtl-For='i_and_d'>Su empresa realiza actividades de I+D? </label>
          <select id='i_and_d' name='i_and_d'>
            <option value='yes'>Sí </option>
            <option value='no'>No (si su respuesta es no, finalice el cuestionario)</option>
          </select>
        </li>
        <li> {/* 6 */}
          <label hmtl-For='year'>Año de referencia: </label>
          <input type='year' id='year' placeholder="Texto aqui..." /> 
        </li>
      </ol>
      <hr></hr>{/*------------------------------------------------------------------------------------------------------------------------------------*/}
      <h3>II. Gastos en I+D</h3>
      <ol start={7}>
        <li> {/* 7 */}
          ¿Cuánto invirtió su empresa en I+D en el año de referencia? 
          <span style={{fontStyle: "italic"}}>(En moneda local)</span>
          <div style={{ marginLeft: "20px"}}>
          <label hmtl-For='total-investment'>Total: </label>
          <input type='text' id='total-investment' placeholder="Texto aqui..." /> 
          </div>
        </li>
        <li> {/* 8 */}
          Desglose de los gastos de I=D:
          <ol type='A'>
            <li>
              <label hmtl-For='personnel-expenses'>Gastos de personal en actividades de I+D: </label>
              <input type='text' id='personnel-expenses' placeholder="Texto aqui..." /> 
            </li>
            <li>
              <label hmtl-For='equipment-software'>Compra de equipos y software para I+D: </label>
              <input type='text' id='equipment-software' placeholder="Texto aqui..." /> 
            </li>
            <li>
              <label hmtl-For='external-consulting'>Contratación de servicios de consultoría externa en I+D: </label>
              <input type='text' id='external-consulting' placeholder="Texto aqui..." /> 
            </li>
            <li>
              <label hmtl-For='materials-supplies'>Materiales y suministros para I+D: </label>
              <input type='text' id='materials-supplies' placeholder="Texto aqui..." /> 
            </li>
            <li>
              <label hmtl-For='related-expenses'>Otros gastos relacionados con I+D: </label>
              <span style={{fontStyle: "italic"}}>(Especifique)</span>
              <input type='text' id='related-expenses' placeholder="Texto aqui..." /> 
            </li>
          </ol>
        </li>
          
        <li> {/* 9 */}
          <label hmtl-For='funding'>¿Como se financia la I+D en su empresa? </label>
          <span style={{fontStyle: "italic"}}>(Puede seleccionar varias opciones)</span>
          <ul>
            <CheckboxGroup9/>
          </ul>
        </li>
      </ol>
      <hr></hr>{/*------------------------------------------------------------------------------------------------------------------------------------*/}
      <h3>III. Recursos Humanos en I+D</h3>
      <ol start={10}>
        <li> {/* 10 */}
          ¿Cuántos empleados participaron en actividades de I+D durante el año de referencia?
          <div style={{ marginLeft: "20px"}}>
            <label hmtl-For='total-employees'>Total: </label>
            <input type='text' id='total-employees' placeholder="Texto aqui..." /> 
            <br/>
            <label hmtl-For='researchers'>De los cuales son investigadores: </label>
            <input type='text' id='researchers' placeholder="Texto aqui..." /> 
            <br/>
            <label hmtl-For='technical-staff'>Personal técnico: </label>
            <input type='text' id='technical-staff' placeholder="Texto aqui..." /> 
            <br/>
            <label hmtl-For='support-staff'>Personal de apoyo: </label>
            <input type='text' id='support-staff' placeholder="Texto aqui..." /> 
          </div>
        </li>
        <li> {/* 11 */}
          <label hmtl-For='specializzed-training'>¿El personal de I+D tiene formación especializada? </label>
          <select id='specializzed-training' name='specializzed-training'>
            <option value='yes'>Sí</option>
            <option value='no'>No</option>
            <option value='partially'>Parcialmente</option>
          </select>
        </li>
      </ol>
      <hr></hr>{/*------------------------------------------------------------------------------------------------------------------------------------*/}
      <h3>IV. Resultados de la I+D</h3>
      <ol start={12}>
        <li> {/* 12 */}
          <label hmtl-For='results'>¿Su empresa ha desarollado alguno de los siguientes resultados a partir de la I+D realizada? </label>
          <span style={{fontStyle: "italic"}}>(Marque las opciones que correspondan)</span>
          <ul>
            <CheckboxGroup12/>
          </ul>
        </li>
        <li> {/* 13 */}
          <label hmtl-For='patent-requests'>¿Cuántas solicitudes de patente ha presentado en los ultimos 3 años? </label>
          <select id='patent-requests' name='patent-requests'>
            <option value='none'>Ninguna</option>
            <option value='1-3'>1-3</option>
            <option value='4-10'>4-10</option>
            <option value='10-more'>Más de 10</option>   
          </select>
        </li>
        <li> {/* 14 */}
          <label hmtl-For='impact'>¿Cuál ha sido el impacto de la I+D en su empresa? </label>
          <span style={{fontStyle: "italic"}}>(Marque las opciones que correspondan)</span>
          <ul>
            <CheckboxGroup14/>
          </ul>
        </li>
      </ol>
      <hr></hr>{/*------------------------------------------------------------------------------------------------------------------------------------*/}
      <h3>V. Gestión de la I+D</h3>
      <ol start={15}>
      <li> {/* 15 */}
        <label hmtl-For='department'>¿Su empresa tiene un departamento o unidad dedicada a la I+D? </label>
        <select id='department' name='department'>
          <option value='yes'>Sí</option>
          <option value='no'>No</option>
          </select>
      </li>
      <li> {/* 16 */}
        <label hmtl-For='records'>¿Se lleva un registro contable separado para los gastos de I+D? </label>
        <select id='records' name='records'>
          <option value='yes'>Sí</option>
          <option value='no'>No</option>
          </select>
      </li>
      <li> {/* 17 */}
        <label hmtl-For='strategy'>¿La empresa cuenta con una estrategia formal de I+D? </label>
        <select id='strategy' name='strategy'>
          <option value='yes'>Sí</option>
          <option value='no'>No</option>
          </select>
      </li>
      </ol>
      <hr></hr>{/*------------------------------------------------------------------------------------------------------------------------------------*/}
      <h3>VI. Colaboraciones en I+D</h3>
      <ol start={18}>
        <li> {/* 18 */}
          <label hmtl-For='entities'>¿Su empresa colabora con alguna de las siguientes entidades en actividades de I+D? </label>
          <span style={{fontStyle: "italic"}}>(Puede seleccionar varias opciones)</span>
          <ul>
            <CheckboxGroup18/>
          </ul>
        </li>
        <li> {/* 19 */}
          <label hmtl-For='patent-requests'>¿Qué tipo de colaboración realiza principalmente? </label>
            <select id='patent-requests' name='patent-requests'>
              <option value='PlaceHolder'>Financiamiento conjunto</option>
              <option value='PlaceHolder'>Transferencia de tecnología</option>
              <option value='PlaceHolder'>Proyectos de innovación compartidos</option>
              <option value='PlaceHolder'>Acceso a infraestructura/laboratorios</option>   
            </select>
        </li>
      </ol>
      <hr></hr>{/*------------------------------------------------------------------------------------------------------------------------------------*/}
      <h3>VII. Perspectivas y desafíos en I+D</h3>
      <ol start={20}>
        <li> {/* 20 */}
          <label hmtl-For='entities'>¿Su empresa colabora con alguna de las siguientes entidades en actividades de I+D? </label>
          <span style={{fontStyle: "italic"}}>(Seleccione las 3 principales)</span>
          <ul>
            <CheckboxGroup20/>
          </ul>
        </li>
        <li> {/* 21 */}
        <label hmtl-For='increase'>¿Tiene planes de aumentar su inversión en I+D en los proximos 3 años? </label>
        <select id='increase' name='increase'>
          <option value='yes'>Sí</option>
          <option value='no'>No</option>
          <option value='maybe'>No está seguro</option>
          </select>
      </li>
      </ol>
      <hr></hr>{/*------------------------------------------------------------------------------------------------------------------------------------*/}
      <h3>VIII. Información adicional</h3>
      <ol start={21}>
      <li> {/* 21 */}
          <label hmtl-For='extra-details'>¿Desea proporcionar algún comentario adicional sobre la actividades de I+D en su empresa? </label>
          <input type='text' id='extra-details' placeholder="Texto aqui..." /> 
        </li>
      </ol>
      <hr></hr>{/*------------------------------------------------------------------------------------------------------------------------------------*/}
    </div>
  );
}

export default Cuestionario_Inovacion_Desarrollo;