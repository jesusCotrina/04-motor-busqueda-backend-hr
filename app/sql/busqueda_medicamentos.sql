SELECT *
FROM medicamento m
JOIN medicamento_especialidad me ON m.medicamento_id = me.medicamento_id
WHERE me.especialidad_id = ANY(:especialidad_ids);