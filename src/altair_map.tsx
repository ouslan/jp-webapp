import { useEffect, useState } from "react";
import vegaEmbed from "vega-embed";

const Altair_map = () => {
    const [mapSpec, setMapSpec] = useState<any>(null);

    useEffect(() => {
        async function fetchMap() {
            try {
                const response = await fetch("http://localhost:8000/map/"); // Django API URL -> might have to change
                const data = await response.json();
                setMapSpec(data);
                vegaEmbed("#map", data);
            } catch (error) {
                console.error("Error fetching the map:", error);
            }
        }

        fetchMap();
    }, []);

    return <div id="map"></div>;
};

export default Altair_map;
