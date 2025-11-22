SELECT *
FROM medicamento m
JOIN medicamento_especialidad me ON m.medicamento_id = me.medicamento_id
WHERE (CAST(:especialidad_ids AS INTEGER) IS NULL OR me.especialidad_id = CAST(:especialidad_ids AS INTEGER))