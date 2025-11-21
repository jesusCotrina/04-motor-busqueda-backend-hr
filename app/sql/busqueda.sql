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
    (:nombre_doctor IS NULL OR m.nombre_completo ILIKE '%' || :nombre_doctor || '%')
    AND (:especialidad_id IS NULL OR e.especialidad_id = :especialidad_id)
    AND (:clinica_id IS NULL OR c.clinica_id = :clinica_id)
    AND (:distrito IS NULL OR s.distrito ILIKE '%' || :distrito || '%')
    AND (:dia IS NUL OR sv.dia_atencion = :dia)
    AND (:tipo_atencion IS NULL OR sv.modalidad = :tipo_atencion)
    ORDER BY m.nombre_completo ASC;
