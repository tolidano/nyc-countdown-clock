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

-- parse_station_entrances
CREATE TABLE `nyc_transit`.`entrance_stations` (
  `id` INT NOT NULL,
  `division` VARCHAR(45) NOT NULL,
  `line` VARCHAR(45) NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `latitude` DECIMAL(11,8) NOT NULL,
  `longitude` DECIMAL(11,8) NOT NULL,
  `free_crossover` TINYINT(1) NOT NULL,
  PRIMARY KEY (`id`));

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
