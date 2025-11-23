SELECT 
    m.medico_id,
    m.nombre_completo AS nombre_doctor,
    m.cmp_numero,
    m.validado_cmp,
    m.url_imagen,
    m.calificacion,
    e.especialidad_id,
    e.nombre AS nombre_especialidad,
    c.clinica_id,
    c.nombre AS nombre_clinica,
    c.url_logo,
    s.sede_id,
    s.nombre_sede,
    s.distrito,
    sv.dia,
    sv.hora_inicio,
    sv.hora_fin,
    sv.modalidad AS tipo_atencion

FROM servicio sv
JOIN medico m ON m.medico_id = sv.medico_id
JOIN clinica c ON c.clinica_id = sv.clinica_id
JOIN sede s ON s.sede_id = sv.sede_id
LEFT JOIN medico_especialidad me ON me.medico_id = m.medico_id
LEFT JOIN especialidad e ON e.especialidad_id = me.especialidad_id
WHERE
    (CAST(:nombre_doctor AS TEXT) IS NULL OR m.nombre_completo ILIKE '%' || CAST(:nombre_doctor AS TEXT) || '%')
    AND (CAST(:especialidad_nombre AS text) IS NULL OR e.nombre = CAST(:especialidad_nombre AS text))
    AND (CAST(:clinica_nombre AS text) IS NULL OR c.nombre = CAST(:clinica_nombre AS text))
    AND (CAST(:distrito AS TEXT) IS NULL OR s.distrito ILIKE '%' || CAST(:distrito AS TEXT) || '%')
    AND (CAST(:dia AS TEXT) IS NULL OR sv.dia = CAST(:dia AS TEXT))
    AND (CAST(:tipo_atencion AS TEXT) IS NULL OR sv.modalidad = CAST(:tipo_atencion AS TEXT))
ORDER BY m.calificacion ASC;
