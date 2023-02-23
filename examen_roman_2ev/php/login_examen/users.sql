DROP TABLE IF EXISTS grupos;

CREATE TABLE `grupos` (
  `id`          INT NOT NULL AUTO_INCREMENT,
  `nombre`      varchar(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

INSERT INTO grupos (nombre) VALUES (
  'admin'
);

INSERT INTO grupos (nombre) VALUES (
  'profesionales'
);

INSERT INTO grupos (nombre) VALUES (
  'lusers'
);


DROP TABLE IF EXISTS usuarios;

CREATE TABLE `usuarios` (
  `id`          INT NOT NULL AUTO_INCREMENT,
  `nombre`      varchar(255) NOT NULL ,
  `secreto`     varchar(255) NOT NULL ,
  `id_grupo`    INT NOT NULL,
  CONSTRAINT fk_id_grupo FOREIGN KEY (id_grupo) REFERENCES grupos(id),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;


-- Todas las contraseñas son 'estudia+'

INSERT INTO usuarios (nombre, secreto, id_grupo) VALUES (
  'admin', '$2y$10$5vhosYTR4WfzKMgGr19FIu4N7I9M83M04tX5N/LPB6Gg8E1b2HpVO', 1
);

INSERT INTO usuarios (nombre, secreto, id_grupo) VALUES (
  'paco', '$2y$10$.VScxsmCBCogy8JYycuhCug/bKbXqmUsGzbwc2Xwct/y7IDvOOqhy', 2
);

INSERT INTO usuarios (nombre, secreto, id_grupo) VALUES (
  'andrea', '$2y$10$ctsD9t2Sw0.aZPMjJzmp7eXJHPwMZdH9nrubHQGWSAFWPddlMm9FO', 2
);

INSERT INTO usuarios (nombre, secreto, id_grupo) VALUES (
  'pepe', '$2y$10$ExrJaK0zzGhWpQDcCnPz4OriynCav0TG2PkzcoBceu4NQzCo7v31C', 3
);

INSERT INTO usuarios (nombre, secreto, id_grupo) VALUES (
  'popa', '$2y$10$znJMwisBPLwg1BgpaYF/vObsYYhxsJ/rrfF4r.2aoRtmDPvnVvWAW', 3
);
