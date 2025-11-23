SELECT 
    *
FROM maestro_medico_clinica 
WHERE
    (CAST(:nombre_doctor AS TEXT) IS NULL OR LOWER(unaccent(nombre_doctor)) LIKE '%' || LOWER(unaccent(CAST(:nombre_doctor AS TEXT))) || '%')
    AND (CAST(:especialidad_nombre AS text) IS NULL OR especialidad_homologada = CAST(:especialidad_nombre AS text))
    AND (CAST(:clinica_nombre AS text) IS NULL OR LOWER(unaccent(nombre_clinica)) = LOWER(unaccent(CAST(:clinica_nombre AS text))) )
    AND (CAST(:distrito AS TEXT) IS NULL OR LOWER(unaccent(distrito)) LIKE '%' || LOWER(unaccent(CAST(:distrito AS TEXT))) || '%')
    AND (CAST(:dia AS TEXT) IS NULL OR dia_atencion = CAST(:dia AS TEXT))
    AND (CAST(:tipo_atencion AS TEXT) IS NULL OR tipo_atencion = CAST(:tipo_atencion AS TEXT))
ORDER BY 
    (hora_inicio IS NULL) ASC,
    calificacion ASC limit 20;
