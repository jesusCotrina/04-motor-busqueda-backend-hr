SELECT *
FROM medicamentos
WHERE des_especialidad = ANY(:especialidades_nombre) limit 20;