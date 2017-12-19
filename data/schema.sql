GRANT ALL PRIVILEGES ON nyctransit.* TO 'nyctransit'@'localhost' IDENTIFIED BY 'nyctransit'

-- parse_colors
CREATE TABLE `nyc_transit`.`colors` (
  `id` INT NOT NULL,
  `mode` VARCHAR(20) NOT NULL,
  `line` VARCHAR(20) NOT NULL,
  `branch` VARCHAR(45) NOT NULL,
  `rgb` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`));

-- parse_equipment
CREATE TABLE `nyc_transit`.`equipment` (
  `identifier` VARCHAR(10) NOT NULL,
  `station` VARCHAR(60) NOT NULL,
  `borough` VARCHAR(5) NOT NULL,
  `lines` VARCHAR(20) NOT NULL,
  `type` VARCHAR(5) NOT NULL,
  `ada` VARCHAR(2) NOT NULL,
  `serving` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`identifier`));

-- parse_equipment_status
CREATE TABLE `nyc_transit`.`equipment_status` (
  `id` INT NOT NULL,
  `identifier` VARCHAR(10) NOT NULL,
  `reason` VARCHAR(500) NOT NULL,
  `upcoming` TINYINT(1) NOT NULL,
  `maintenance` TINYINT(1) NOT NULL,
  `outage_date` DATETIME NOT NULL,
  `return_date` DATETIME NOT NULL,
  PRIMARY KEY (`id`));

-- parse_station_complexes
CREATE TABLE `nyc_transit`.`complexes` (
  `complex_id` INT NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`complex_id`));

-- parse_station_entrances and parse_station_entrances_geojson
CREATE TABLE `nyc_transit`.`entrance_stations` (
  `station_id` INT NOT NULL,
  `division` VARCHAR(45) NOT NULL,
  `line` VARCHAR(45) NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `latitude` DECIMAL(11,8) NOT NULL,
  `longitude` DECIMAL(11,8) NOT NULL,
  `free_crossover` TINYINT(1) NOT NULL,
  PRIMARY KEY (`station_id`));

CREATE TABLE `nyc_transit`.`entrace_station_routes` (
  `route_id` INT NOT NULL,
  `route` VARCHAR(45) NOT NULL,
  `station_id` INT NOT NULL,
  PRIMARY KEY (`route_id`));

CREATE TABLE `nyc_transit`.`station_entrances` (
  `entrance_id` INT NOT NULL,
  `station_id` INT NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `entry` TINYINT(1) NOT NULL,
  `exit_only` TINYINT(1) NOT NULL,
  `vending` TINYINT(1) NOT NULL,
  `staffing` VARCHAR(500) NOT NULL,
  `staff_hours` VARCHAR(500) NOT NULL,
  `ada` TINYINT(1) NOT NULL,
  `ada_notes` VARCHAR(500) NOT NULL,
  `north_south` VARCHAR(100) NOT NULL,
  `east_west` VARCHAR(100) NOT NULL,
  `corner` VARCHAR(5) NOT NULL,
  `latitude` DECIMAL(11,8) NOT NULL,
  `longitude` DECIMAL(11,8) NOT NULL,
  `geojson_position` VARCHAR(250) NOT NULL,
  PRIMARY KEY (`entrance_id`));

-- parse_service_status (subway and bus)
CREATE TABLE `nyc_transit`.`situations` (
  `situation_id` INT NOT NULL,
  `creation_time` VARCHAR(25) NOT NULL,
  `situation_number` VARCHAR(10) NOT NULL,
  `start_time` VARCHAR(25) NOT NULL,
  `end_time` VARCHAR(25) NOT NULL,
  `summary` VARCHAR(250) NOT NULL,
  `description` VARCHAR(250) NOT NULL,
  `long_description` VARCHAR(1000) NOT NULL,
  `planned` TINYINT(1) NOT NULL,
  `reason` VARCHAR(50) NOT NULL,
  `source_type` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`situation_id`));

CREATE TABLE `nyc_transit`.`situation_effects` (
  `effect_id` INT NOT NULL,
  `situation_id` INT NOT NULL,
  `line` VARCHAR(10) NOT NULL,
  `direction` TINYINT(1) NOT NULL,
  PRIMARY KEY (`effect_id`));

CREATE TABLE `nyc_transit`.`situation_consequences` (
  `consequence_id` INT NOT NULL,
  `situation_id` INT NOT NULL,
  `condition` VARCHAR(10) NOT NULL,
  `severity` TINYINT(1) NOT NULL,
  PRIMARY KEY (`consequence_id`));

-- parse_stations and parse_stations_geojson
CREATE TABLE `nyc_transit`.`stations` (
  `station_id` INT NOT NULL,
  `complex_id` INT NOT NULL,
  `gtfs_stop_id` VARCHAR(10) NOT NULL,
  `division` VARCHAR(10) NOT NULL,
  `line` VARCHAR(20) NOT NULL,
  `stop_name` VARCHAR(100) NOT NULL,
  `borough` VARCHAR(5) NOT NULL,
  `daytime_routes` VARCHAR(25) NOT NULL,
  `structure` VARCHAR(25) NOT NULL,
  `latitude` DECIMAL(11,8) NOT NULL,
  `longitude` DECIMAL(11,8) NOT NULL,
  `object_id` INT NOT NULL,
  `notes` VARCHAR(250) NOT NULL,
  PRIMARY KEY (`station_id`));

CREATE TABLE `nyc_transit`.`station_lines` (
  `line_id` INT NOT NULL,
  `line` VARCHAR(5) NOT NULL,
  `station_id` INT NOT NULL,
  PRIMARY KEY (`line_id`));
