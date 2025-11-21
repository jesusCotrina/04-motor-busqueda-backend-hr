SELECT m.*
FROM medicamento m
JOIN medicamento_especialidad me ON m.medicamento_id = me.medicamento_id
JOIN especialidad e on me.especialidad_id = e.especialidad_id
WHERE e.nombre = ANY(:especialidades_nombre);