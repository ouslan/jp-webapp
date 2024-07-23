-- MASTER TABLE --
CREATE TABLE Forms {
  id INTEGER,
  name TEXT NOT NULL,
  PRIMARY KEY (id)
}


-- CONSTRUCTION --
CREATE TABLE JP_541 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}


--BALANZA DE PAGOS --
CREATE TABLE JP_304 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_361 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_362 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_363 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_364 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_375 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_383 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_529 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_536_2 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_544 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_544_1 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_547 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}


--INGRESO NETO --
CREATE TABLE IP_110 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_210 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_220 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_230 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_310 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_310b {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_420 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_440 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_440g {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_480 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_480a {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_490 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_510 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_520 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_520a {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_520s {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_530 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540J {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540P {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540S {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540a {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540v {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_610 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_620 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_710 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_720 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_810 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_560_63110 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_560_63111 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_560_63210 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_560_2 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}