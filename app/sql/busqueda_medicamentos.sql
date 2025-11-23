SELECT *
FROM medicamentos 
WHERE (CAST(:especialidad_ids AS INTEGER) IS NULL OR id_especialidad = CAST(:especialidad_ids AS INTEGER)) 
limit 20