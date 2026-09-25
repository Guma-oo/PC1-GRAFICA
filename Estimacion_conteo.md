# Estimación del flujo de personas provenientes de la puerta 5

**Fecha y hora de observación:** 22 de septiembre de 2026, a las 10:25 a. m.  
**Duración del video:** 5 minutos  
**Personas provenientes de la puerta 5 contadas por el programa:** 26

## Pregunta

**Si el flujo observado continuara durante una hora, ¿cuántas personas provenientes de la puerta 5 pasarían por el cruce entre las 10:25 y las 11:25 a. m.?**

## 1. Estimación mediante regla de tres

Durante los primeros 5 minutos pasaron 26 personas. Si **el mismo ritmo se mantuviera durante toda la hora**, la regla de tres sería:

$$
5\text{ minutos}\longrightarrow26\text{ personas}
$$

$$
60\text{ minutos}\longrightarrow x
$$

$$
x=\frac{26\times60}{5}=\boxed{312\text{ personas}}
$$

Esta es la estimación más sencilla, pero supone que llegan personas al mismo ritmo durante los 60 minutos.

## 2. Estimación con un flujo que disminuye

A las 10:25 a. m. algunas personas podrían estar llegando tarde a clase. Para explorar qué ocurriría si el flujo bajara después, **suponemos que el ritmo de paso se reduce a la mitad cada 30 minutos**. Ese tiempo de reducción es un supuesto; no se obtuvo de los cinco minutos de video.

Representamos el ritmo mediante la función:

$$
\lambda(t)=\lambda_0\,2^{-t/30}
$$

Aquí, $t$ es el número de minutos transcurridos desde las 10:25 a. m. y $\lambda_0$ es el ritmo inicial. En un modelo de llegadas Poisson, el número *esperado* de personas durante un intervalo se calcula integrando esa tasa.

Como observamos **26 personas en los primeros 5 minutos**, usamos ese dato para estimar el total de la hora:

$$
E_{60}=26\,\frac{\int_0^{60}2^{-t/30}\,dt}{\int_0^5 2^{-t/30}\,dt}
$$

La división indica cuántas veces mayor es el flujo esperado de **60 minutos** respecto al de **5 minutos**. También permite cancelar $\lambda_0$, cuyo valor inicial desconocemos. Al resolver las integrales:

$$
E_{60}=26\,\frac{1-2^{-60/30}}{1-2^{-5/30}}
=26\,\frac{0.75}{1-2^{-1/6}}
\approx178.7
$$

**Resultado del modelo: aproximadamente 179 personas provenientes de la puerta 5 pasarían por el cruce entre las 10:25 y las 11:25 a. m.**
