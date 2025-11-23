SELECT 
    *
FROM maestro_medico_clinica sv
WHERE especialidad_homologada = ANY(:especialidades_nombre) limit 20;
