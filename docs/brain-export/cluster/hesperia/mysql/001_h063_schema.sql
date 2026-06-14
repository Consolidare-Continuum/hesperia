-- H063-34: Hesperia 0.6.3 IRC Teacher ledger (MySQL utf8mb4)
CREATE DATABASE IF NOT EXISTS hesperia
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE hesperia;

CREATE TABLE IF NOT EXISTS hesperia_teacher_run (
  run_id            CHAR(36) PRIMARY KEY,
  correlation_id    VARCHAR(128) NOT NULL,
  lang              CHAR(2) NOT NULL DEFAULT 'ru',
  input_text_ru     MEDIUMTEXT NOT NULL,
  input_kind        VARCHAR(64) NOT NULL DEFAULT 'tfp_scientific_statement',
  engine_envelope   JSON NOT NULL,
  teacher_request   JSON NOT NULL,
  teacher_response  JSON NULL,
  irc_channel       VARCHAR(64) NULL,
  status            ENUM('started','engine_ok','teacher_ok','teacher_fail','stored') NOT NULL,
  hesperia_git_sha  VARCHAR(40) NULL,
  tersagor_git_sha  VARCHAR(40) NULL,
  openai_model      VARCHAR(64) NULL,
  created_at        TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP(3),
  INDEX idx_corr (correlation_id),
  INDEX idx_created (created_at)
);

CREATE TABLE IF NOT EXISTS hesperia_edge_snapshot (
  id                BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  run_id            CHAR(36) NOT NULL,
  source_concept_id VARCHAR(128) NOT NULL,
  target_concept_id VARCHAR(128) NOT NULL,
  relation_type     VARCHAR(64) NOT NULL,
  W_e               DECIMAL(12,6) NOT NULL,
  R_e               DECIMAL(12,6) NULL,
  Q_e               DECIMAL(12,6) NULL,
  C_e               DECIMAL(12,6) NULL,
  D_e               DECIMAL(12,6) NULL,
  K_e               DECIMAL(12,6) NULL,
  phi_sat           DECIMAL(12,6) NULL,
  area_id           VARCHAR(128) NULL,
  family_id         VARCHAR(128) NULL,
  FOREIGN KEY (run_id) REFERENCES hesperia_teacher_run(run_id),
  INDEX idx_run (run_id),
  INDEX idx_edge (source_concept_id, target_concept_id, relation_type)
);

CREATE TABLE IF NOT EXISTS hesperia_activation_snapshot (
  id                BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  run_id            CHAR(36) NOT NULL,
  concept_id        VARCHAR(128) NOT NULL,
  label_ru          VARCHAR(255) NULL,
  area_id           VARCHAR(128) NULL,
  family_id         VARCHAR(128) NULL,
  observed          DECIMAL(12,6) NOT NULL,
  expected          DECIMAL(12,6) NULL,
  residual          DECIMAL(12,6) NULL,
  incident_type     VARCHAR(64) NULL,
  FOREIGN KEY (run_id) REFERENCES hesperia_teacher_run(run_id),
  INDEX idx_run_concept (run_id, concept_id)
);

CREATE TABLE IF NOT EXISTS hesperia_proposal (
  proposal_id       CHAR(36) PRIMARY KEY,
  run_id            CHAR(36) NOT NULL,
  seq               INT NOT NULL,
  action            VARCHAR(32) NOT NULL,
  target_type       ENUM('edge','concept','cd_field','bridge') NOT NULL,
  payload           JSON NOT NULL,
  confidence        DECIMAL(6,4) NULL,
  incident_ref      VARCHAR(128) NULL,
  status            ENUM('pending','accepted','rejected','sandbox_pass','sandbox_fail') DEFAULT 'pending',
  created_at        TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP(3),
  FOREIGN KEY (run_id) REFERENCES hesperia_teacher_run(run_id),
  INDEX idx_run_status (run_id, status)
);

CREATE TABLE IF NOT EXISTS hesperia_reweight_event (
  event_id          CHAR(36) PRIMARY KEY,
  run_id            CHAR(36) NOT NULL,
  proposal_id       CHAR(36) NULL,
  parameter_key     VARCHAR(128) NOT NULL,
  value_before      DECIMAL(12,6) NULL,
  value_after       DECIMAL(12,6) NOT NULL,
  applied           TINYINT(1) NOT NULL DEFAULT 0,
  operator_subject  VARCHAR(255) NULL,
  created_at        TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP(3),
  FOREIGN KEY (run_id) REFERENCES hesperia_teacher_run(run_id),
  FOREIGN KEY (proposal_id) REFERENCES hesperia_proposal(proposal_id)
);
