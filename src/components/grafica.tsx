import { useEffect, useRef } from "react";
import vegaEmbed from "vega-embed";
import chartSpec from "../graphics/chart.json";


const Grafica = () => {
    const chartRef = useRef(null);

    useEffect(() => {
      if (chartRef.current) {
        vegaEmbed(chartRef.current, chartSpec).catch(console.error);
      }
    }, []);
    
    
    return (<div ref={chartRef}></div>);
}


export default Grafica;