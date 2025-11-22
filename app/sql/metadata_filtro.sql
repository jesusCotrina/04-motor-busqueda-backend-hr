
WITH 
e AS (
    SELECT json_agg(json_build_object('id', especialidad_id, 'nombre', nombre)) AS data
    FROM especialidad
),
c AS (
    SELECT json_agg(json_build_object('id', clinica_id, 'nombre', nombre)) AS data
    FROM clinica
),
s AS (
    SELECT json_agg(json_build_object(
        'id', sede_id, 
        'clinica_id', clinica_id, 
        'nombre', nombre_sede,
        'distrito',distrito
    )) AS data
    FROM sede
),
t AS (
    SELECT json_agg(x) AS data
    FROM (
        VALUES ('Virtual'), ('Presencial')
    ) AS v(x)
)
SELECT json_build_object(
    'especialidades', e.data,
    'clinicas', c.data,
    'sedes', s.data,
    'tipos_atencion', t.data
) AS metadata
FROM e, c, s, t;