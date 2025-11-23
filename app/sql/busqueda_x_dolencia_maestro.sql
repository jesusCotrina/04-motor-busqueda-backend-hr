SELECT 
    *
FROM maestro_medico_clinica sv
WHERE especialidad_homologada = ANY(:especialidades_nombre) ORDER BY 
    (horario_inicio IS NULL) ASC,
    calificacion ASC
    limit 20;
