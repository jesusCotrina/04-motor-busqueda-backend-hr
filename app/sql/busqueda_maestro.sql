SELECT 
    *
FROM maestro_medico_clinica sv
WHERE
    (CAST(:nombre_doctor AS TEXT) IS NULL OR LOWER(unaccent(nombre_doctor)) LIKE '%' || LOWER(unaccent(CAST(:nombre_doctor AS TEXT))) || '%')
    AND (CAST(:especialidad_id AS INTEGER) IS NULL OR id_especialidad = CAST(:especialidad_id AS INTEGER))
    AND (CAST(:clinica_id AS INTEGER) IS NULL OR id_clinica = CAST(:clinica_id AS INTEGER))
    AND (CAST(:distrito AS TEXT) IS NULL OR distrito ILIKE '%' || CAST(:distrito AS TEXT) || '%')
    AND (CAST(:dia AS TEXT) IS NULL OR dia_atencion = CAST(:dia AS TEXT))
    AND (CAST(:tipo_atencion AS TEXT) IS NULL OR tipo_atencion = CAST(:tipo_atencion AS TEXT))
ORDER BY 
    (horario IS NULL) ASC,
    calificacion ASC limit 20;
