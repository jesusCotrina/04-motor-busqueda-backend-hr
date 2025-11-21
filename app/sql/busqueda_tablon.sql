SELECT *
FROM tablon
WHERE (:nombre_doctor IS NULL OR nombre_completo ILIKE '%' || :nombre_doctor || '%')
  AND (:especialidad_id IS NULL OR especialidad_id = :especialidad_id)
  AND (:clinica_id IS NULL OR clinica_id = :clinica_id)
  AND (:distrito IS NULL OR distrito = :distrito)
  AND (:dia IS NULL OR dia_atencion = :dia)
  AND (:tipo_atencion IS NULL OR modalidad = :tipo_atencion)
ORDER BY nombre_completo;