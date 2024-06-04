document.addEventListener("DOMContentLoaded", function () {
    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(dropdown => {
        const select = dropdown.querySelector('.select');
        const caret = dropdown.querySelector('.caret');
        const menu = dropdown.querySelector('.menu');
        const options = dropdown.querySelectorAll('.menu li');
        const selected = dropdown.querySelector('.selected');

        select.addEventListener('click', () => {
            menu.classList.toggle('menu-open');
            caret.classList.toggle('caret-rotate');
        });

        options.forEach(option => {
            option.addEventListener('click', () => {
                selected.innerText = option.innerText;
                menu.classList.remove('menu-open');
                caret.classList.remove('caret-rotate');
                options.forEach(option => {
                    option.classList.remove('active');
                });
                option.classList.add('active');
            });
        });
    });

    document.addEventListener('click', function (event) {
        const dropdowns = document.querySelectorAll('.dropdown');
        dropdowns.forEach(dropdown => {
            if (!dropdown.contains(event.target)) {
                const menu = dropdown.querySelector('.menu');
                const caret = dropdown.querySelector('.caret');
                menu.classList.remove('menu-open');
                caret.classList.remove('caret-rotate');
            }
        });
    });
});

function toggleBurgerMenu() {
    const burgerMenu = document.querySelector('.burger_menu');
    burgerMenu.classList.toggle('burger_menu-open');
}

document.addEventListener("DOMContentLoaded", function () {
    const burgerOptions = document.querySelectorAll('.burger_menu li');

    burgerOptions.forEach(option => {
        option.addEventListener('click', () => {
            const burgerMenu = document.querySelector('.burger_menu');
            burgerMenu.classList.remove('burger_menu-open');
        });
    });

    document.addEventListener('click', function (event) {
        const burger = document.querySelector('.burger');
        const burgerMenu = document.querySelector('.burger_menu');
        if (!burger.contains(event.target) && !burgerMenu.contains(event.target)) {
            burgerMenu.classList.remove('burger_menu-open');
        }
    });
});    

document.addEventListener('DOMContentLoaded', function() {
    // Function to handle dropdown changes for a specific block
    function setupDropdown(dropdownClass, descriptionId, graphContainerClass, data) {
        const dropdown = document.querySelector(dropdownClass);
        const select = dropdown.querySelector('.select');
        const menu = dropdown.querySelector('.menu');
        const options = menu.querySelectorAll('li');
        const selectedText = select.querySelector('.selected');
        const description = document.getElementById(descriptionId);
        const graphContainer = document.querySelector(graphContainerClass);

        options.forEach(option => {
            option.addEventListener('click', function() {
                options.forEach(option => option.classList.remove('active'));
                this.classList.add('active');
                selectedText.textContent = this.textContent;
                menu.classList.remove('open');

                const value = this.getAttribute('data-value');
                description.innerHTML = data[value].description;
                graphContainer.innerHTML = data[value].graph;
            });
        });

        document.addEventListener('click', function(e) {
            if (!dropdown.contains(e.target)) {
                menu.classList.remove('open');
            }
        });
    }

    // Data for BLOCK 2
    const dataBlock2 = {
        'grupo-trabajador': {
            description: `
                La Encuesta de Grupo Trabajador Ajustada Estacionalmente, también conocida como Labor Force Survey - Seasonally Adjusted,
                es un instrumento utilizado para medir la fuerza laboral en una determinada área geográfica. Se ajusta estacionalmente para
                eliminar las variaciones predecibles que ocurren regularmente en ciertos momentos del año, como las relacionadas con las
                estaciones o festividades, lo que permite una comparación más precisa del rendimiento laboral a lo largo del tiempo.
                Los datos se presentan en miles de personas y se pueden analizar en años fiscales, años calendario y años de referencia
                para evaluar tendencias y cambios en la fuerza laboral.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        },
        'empleo-total': {
            description: `
                La Encuesta de Grupo Trabajador - Ajustada Estacionalmente, también conocida como Labor Force Survey - Seasonally Adjusted, es 
                una herramienta crucial para analizar la dinámica del empleo en una economía. En esta encuesta, se examina el Empleo Total, 
                expresado en miles de personas. Este dato está ajustado estacionalmente para eliminar las variaciones predecibles debido a factores 
                como las estaciones del año o festividades, lo que proporciona una visión más clara de las tendencias subyacentes en el mercado 
                laboral. Este indicador es esencial para comprender la salud y la dirección del empleo en la economía.
            `,
            graph: '<!-- Graph content for Empleo Total -->'
        },
        'desempleo': {
            description: `
                La Encuesta de Grupo Trabajador - Ajustada Estacionalmente, comúnmente referida como Labor Force Survey - Seasonally Adjusted, 
                es una herramienta fundamental para comprender la dinámica del desempleo en una economía. Este estudio analiza el número de 
                personas desempleadas, expresado en miles. Los datos están ajustados estacionalmente para eliminar las variaciones predecibles 
                debido a factores como las estaciones del año o festividades, lo que proporciona una evaluación más precisa de las tendencias 
                subyacentes en el mercado laboral. Este indicador es crucial para evaluar la salud y la dirección del mercado laboral y la 
                economía en su conjunto.
            `,
            graph: '<!-- Graph content for Desempleo -->'
        },
        'tasa-desempleo': {
            description: `
                La Encuesta de Grupo Trabajador - Ajustada Estacionalmente, también conocida como Labor Force Survey - Seasonally Adjusted, 
                ofrece una visión detallada de la Tasa de Desempleo, expresada en porcentaje. Estos datos son ajustados estacionalmente 
                para eliminar fluctuaciones predecibles relacionadas con factores como las estaciones del año o festividades. Esto permite
                una evaluación más precisa de las tendencias subyacentes en el mercado laboral. La Tasa de Desempleo es un indicador clave 
                que proporciona información sobre la salud general del mercado laboral y la economía, ayudando a guiar políticas y decisiones
                empresariales.
            `,
            graph: '<!-- Graph content for Tasa de Desempleo -->'
        }
    };

    // Data for BLOCK 3
    const dataBlock3 = {
        'poblacion-civil-GT': {
            description: `
                La Encuesta de Grupo Trabajador, o Labor Force Survey, es una herramienta crucial para comprender la dinámica demográfica de 
                la fuerza laboral durante el año fiscal. Este estudio analiza la Población Civil No-Institucional, expresada en miles de 
                personas durante el período fiscal correspondiente. La Población Civil No-Institucional incluye a aquellos que no están en 
                instituciones militares, correccionales o de atención a largo plazo. Esta métrica específica proporciona una visión amplia 
                y detallada de la composición de la fuerza laboral, permitiendo analizar las tendencias y cambios demográficos y laborales 
                de una población determinada. Los datos recopilados son fundamentales para la formulación de políticas y la toma de decisiones 
                estratégicas en el ámbito empresarial y gubernamental.
            `,
            graph: '<!-- Graph content for Población Civil No-Institucional -->'
        },
        'grupo-trabajador-GT': {
            description: `
                La Encuesta de Grupo Trabajador, también conocida como Labor Force Survey, es un instrumento esencial para comprender la 
                dinámica del mercado laboral durante los años fiscales. Este estudio examina el Grupo Trabajador, expresado en miles de 
                personas, durante períodos financieros específicos. El Grupo Trabajador abarca a aquellas personas que están empleadas o 
                activamente buscando empleo durante el año fiscal correspondiente. Esta encuesta proporciona una visión detallada de la 
                fuerza laboral de una población durante el período fiscal, lo que permite analizar la participación y la situación laboral 
                de la comunidad durante ese período. Es una herramienta fundamental para comprender la salud y la dirección del mercado 
                laboral durante el año fiscal y para orientar políticas y decisiones empresariales.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        },
        'empleo-total-GT': {
            description: `
                La Encuesta de Grupo Trabajador es una herramienta fundamental para analizar la dinámica del mercado laboral. Este 
                estudio mide el empleo total, expresado en miles de personas, ofreciendo datos detallados sobre la cantidad de individuos 
                empleados en diferentes sectores económicos. La encuesta abarca a todas las personas que están empleadas o buscan 
                activamente empleo durante el período fiscal correspondiente. Al proporcionar una visión comprensiva de la fuerza 
                laboral, esta encuesta permite evaluar la participación laboral y las condiciones de empleo dentro de una comunidad. 
                La información obtenida es crucial para entender la salud del mercado laboral y para tomar decisiones informadas en 
                políticas públicas y estrategias empresariales.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        },
        'empleo-agricola-GT': {
            description: `
                La Encuesta de Grupo Trabajador, también conocida como Labor Force Survey, es un estudio esencial para entender la 
                estructura del empleo en distintos sectores. Una de sus métricas clave es el Empleo Agrícola, que se expresa en 
                miles de personas durante el período fiscal correspondiente. Esta métrica específica ofrece una visión detallada sobre 
                el número de individuos empleados en el sector agrícola, permitiendo analizar las tendencias y la evolución del empleo 
                en este importante sector económico. Los datos recopilados son fundamentales para formular políticas agrícolas y laborales, 
                así como para tomar decisiones empresariales informadas.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        },
        'empleo-construccion-GT': {
            description: `
                La Encuesta de Grupo Trabajador, o Labor Force Survey, es un estudio clave para analizar el mercado laboral en diferentes 
                sectores. Una de sus métricas destacadas es el Empleo en Construcción, expresado en miles de personas durante el período 
                fiscal correspondiente. Esta métrica proporciona información detallada sobre el número de individuos empleados en el sector 
                de la construcción, permitiendo evaluar las tendencias y cambios en este campo vital. Los datos obtenidos son esenciales 
                para el desarrollo de políticas laborales y económicas, así como para la toma de decisiones estratégicas en el ámbito 
                empresarial y gubernamental.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        },
        'empleo-manufactura-GT': {
            description:`
                La Encuesta de Grupo Trabajador, o Labor Force Survey, es un estudio esencial para evaluar el mercado laboral en diversos 
                sectores. Entre sus métricas clave se encuentra el Empleo en Manufactura, expresado en miles de personas durante el período fiscal 
                correspondiente. Esta métrica específica proporciona información detallada sobre el número de individuos empleados en el sector 
                manufacturero, permitiendo analizar las tendencias y cambios en esta área crítica de la economía. Los datos recopilados son 
                fundamentales para la formulación de políticas industriales y laborales, así como para la toma de decisiones estratégicas en el 
                ámbito empresarial y gubernamental.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        },
        'empleo-comercio-GT': {
            description:`
                La Encuesta de Grupo Trabajador, también conocida como Labor Force Survey, es un instrumento crucial para comprender la 
                dinámica del mercado laboral. Uno de los aspectos que analiza es el Empleo en Comercio, expresado en miles de personas
                durante el período fiscal. Esta métrica proporciona información sobre la cantidad de individuos empleados en el sector 
                comercial, permitiendo un análisis detallado de las tendencias y la evolución del empleo en este ámbito. Los datos 
                recopilados son fundamentales para informar políticas económicas y laborales, así como para la toma de decisiones 
                estratégicas en el ámbito empresarial y gubernamental.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        },
        'empleo-finanzas-GT': {
            description:`
                La Encuesta de Grupo Trabajador, conocida como Labor Force Survey, es un instrumento esencial para comprender la dinámica del 
                mercado laboral. Uno de sus aspectos clave es el Empleo en Finanzas, Seguros y Bienes Raíces, medido en miles de personas durante 
                el período fiscal. Esta métrica ofrece una visión detallada del número de individuos empleados en estos sectores, permitiendo un 
                análisis exhaustivo de las tendencias y cambios en áreas cruciales de la economía. Los datos recopilados son fundamentales para 
                orientar políticas laborales, económicas y de desarrollo, así como para la toma de decisiones estratégicas en empresas y organismos 
                gubernamentales.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        },
        'empleo-transportacion-GT': {
            description:`
                La Encuesta de Grupo Trabajador, o Labor Force Survey, es un estudio vital para comprender el panorama laboral en diversos 
                sectores. Una de sus métricas principales es el Empleo en Transportación, Comunicaciones y Utilidades Públicas, medido 
                en miles de personas durante el período fiscal. Esta métrica ofrece una visión detallada del número de personas empleadas en 
                sectores críticos como el transporte, las comunicaciones y las utilidades públicas. Estos datos son esenciales para comprender 
                la dinámica laboral en estos sectores clave y para informar la formulación de políticas y estrategias empresariales.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        },
        'empleo-servicios-GT':{
            description:`
                La Encuesta de Grupo Trabajador, conocida como Labor Force Survey, es un recurso clave para comprender la dinámica laboral en 
                diversos sectores. Una métrica importante que proporciona es el Empleo en Servicios, expresado en miles de personas durante 
                el período fiscal. Esta cifra ofrece una visión detallada del número de individuos empleados en el sector de servicios, 
                permitiendo analizar las tendencias y la evolución del empleo en esta área crucial de la economía. Los datos recopilados son 
                esenciales para informar políticas laborales y económicas, así como para respaldar decisiones estratégicas tanto en el ámbito 
                empresarial como gubernamental.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        },
        'empleo-administracion-GT': {
            description:`
                La Encuesta de Grupo Trabajador, conocida como Labor Force Survey, es un instrumento crucial para entender el panorama laboral 
                en diferentes sectores. Uno de los indicadores que analiza es el Empleo en Administración Pública, medido en miles de personas 
                durante el período fiscal. Este dato ofrece una visión específica sobre la cantidad de individuos empleados en la administración 
                pública, permitiendo evaluar la dimensión y dinámica de este sector. La información obtenida es fundamental para la formulación 
                de políticas públicas y la toma de decisiones estratégicas tanto en el ámbito gubernamental como en el empresarial.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        },
        'empleo-cuenta-GT': {
            description:`
                La Encuesta de Grupo Trabajador, también conocida como Labor Force Survey, es un instrumento fundamental para comprender 
                la dinámica del mercado laboral. Uno de los aspectos clave que mide es el Empleo por Cuenta Propia, expresado en miles 
                de personas durante el período fiscal. Esta métrica proporciona una visión detallada sobre el número de individuos que 
                trabajan por cuenta propia, lo que incluye empresarios individuales y autónomos. Estos datos son esenciales para entender 
                la estructura del empleo y el espíritu emprendedor en una economía, lo que permite formular políticas laborales y económicas 
                más efectivas.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        },
        'desempleo-GT': {
            description:`
                La Encuesta de Grupo Trabajador, conocida como Labor Force Survey, es un recurso crucial para comprender el mercado laboral. 
                Uno de los indicadores principales que proporciona esta encuesta es el Desempleo, medido en miles de personas durante el período 
                fiscal. Este dato ofrece una visión detallada de la cantidad de personas que están desempleadas durante un período específico, 
                lo que permite analizar las tendencias y la salud general del mercado laboral. La información obtenida es fundamental para informar 
                políticas públicas, estrategias de empleo y toma de decisiones tanto en el ámbito gubernamental como empresarial.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        },
        'tasa-desempleo-GT': {
            description: `
                La Encuesta de Grupo Trabajador, o Labor Force Survey, es un estudio crucial para comprender el mercado laboral. Una de sus 
                métricas más importantes es la Tasa de Desempleo, expresada en porcentaje durante el período fiscal. Esta métrica proporciona 
                una visión clara de la proporción de personas que están desempleadas en relación con la fuerza laboral total. La tasa de 
                desempleo es un indicador clave de la salud económica de un país y es fundamental para la formulación de políticas laborales 
                y económicas. Los datos obtenidos ayudan a los gobiernos, empresas y organizaciones a tomar decisiones informadas sobre empleo 
                y desarrollo económico.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        },
        'tasa-participacion-GT': {
            description: `
                La Encuesta de Grupo Trabajador, o Labor Force Survey, es un instrumento fundamental para comprender el mercado laboral. 
                Uno de los indicadores clave que proporciona esta encuesta es la Tasa de Participación, expresada en porcentaje durante el 
                período fiscal. Esta tasa refleja la proporción de la población en edad de trabajar que está empleada o activamente buscando 
                empleo. Es un indicador crucial para evaluar la dinámica de la fuerza laboral y la participación de la población en la 
                actividad económica. Los datos de la tasa de participación son utilizados para analizar la salud del mercado laboral y 
                orientar políticas públicas y estrategias empresariales.
            `,
            graph: '<!-- Graph content for Grupo Trabajador -->'
        }
    };

    const dataBlock4 = {

    };

    // Setup dropdowns
    setupDropdown('.dropdown-block-2', 'description-block-2', '.graph-container-block-2', dataBlock2);
    setupDropdown('.dropdown-block-3', 'description-block-3', '.graph-container-block-3', dataBlock3);
    setupDropdown('.dropdown-block-4', 'description-block-4', '.graph-container-block-4', dataBlock4);
});