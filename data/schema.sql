# noinspection SqlNoDataSourceInspectionForFile

GRANT ALL PRIVILEGES ON nyctransit.* TO 'nyctransit'@'localhost' IDENTIFIED BY 'nyctransit';

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

CREATE TABLE `nyc_transit`.`entrance_station_routes` (
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

CREATE TABLE `nyc_transit`.`stations_lines` (
  `line_id` INT NOT NULL,
  `line` VARCHAR(5) NOT NULL,
  `station_id` INT NOT NULL,
  PRIMARY KEY (`line_id`));

-- parse_station_lines_geojson
CREATE TABLE `nyc_transit`.`station_lines` (
  `line_id` INT NOT NULL,
  `url` VARCHAR(100) NOT NULL,
  `symbol` VARCHAR(5) NOT NULL,
  `name` VARCHAR(5) NOT NULL,
  PRIMARY KEY (`line_id`));

CREATE TABLE `nyc_transit`.`station_line_segments` (
  `line_segment_id` INT NOT NULL,
  `line_id` INT NOT NULL,
  `segment_id` VARCHAR(10) NOT NULL,
  `object_id` VARCHAR(10) NOT NULL,
  `length` DECIMAL(15,9) NOT NULL,
  PRIMARY KEY (`line_segment_id`));

CREATE TABLE `nyc_transit`.`station_line_segment_points` (
  `point_id` INT NOT NULL,
  `line_segment_id` INT NOT NULL,
  `latitude` DECIMAL(11,8) NOT NULL,
  `longitude` DECIMAL(11,8) NOT NULL,
  `sequence` INT NOT NULL,
  PRIMARY KEY (`point_id`));

-- parse_mta_feed_gtfs.py (trip_updates)
CREATE TABLE `nyc_transit`.`trip_updates` (
  `update_id` INT NOT NULL,
  `timestamp` TIMESTAMP NOT NULL,
  `delay` INT NOT NULL,
  `vehicle_id` VARCHAR(10) NOT NULL,
  `trip_id` INT NOT NULL,
  `start_date` DATE NOT NULL,
  `route_id` INT NOT NULL,
  `direction_id` TINYINT(1) NOT NULL,
  PRIMARY KEY (`update_id`));

CREATE TABLE `nyc_transit`.`stop_time_updates` (
  `stop_time_update_id` INT NOT NULL,
  `update_id` INT NOT NULL,
  `stop_sequence` TINYINT(1) NOT NULL,
  `stop_id` INT NOT NULL,
  `arrival` DATETIME NOT NULL,
  `departure` DATETIME NOT NULL,
  PRIMARY KEY (`stop_time_update_id`));

-- parse_mta_feed_gtfs.py (vehicles)
CREATE TABLE `nyc_transit`.`vehicles` (
  `vehicle_id` VARCHAR(10) NOT NULL,
  `stop_id` INT NOT NULL,
  `timestamp` TIMESTAMP NOT NULL,
  `latitude` DECIMAL(11,8) NOT NULL,
  `longitude` DECIMAL(11,8) NOT NULL,
  `bearing` DECIMAL(7,4) NOT NULL,
  `trip_id` INT NOT NULL,
  `start_date` DATETIME NOT NULL,
  `route_id` INT NOT NULL,
  `direction_id` TINYINT(1) NOT NULL,
  PRIMARY KEY (`vehicle_id`));

-- parse_mta_feed_gtfs.py (alerts)
CREATE TABLE `nyc_transit`.`alerts` (
  `alert_id` INT NOT NULL,
  `cause` VARCHAR(100) NOT NULL,
  `effect` VARCHAR(100) NOT NULL,
  `header` VARCHAR(100) NOT NULL,
  `description` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`alert_id`));

CREATE TABLE `nyc_transit`.`alert_entities` (
  `alert_entity_id` INT NOT NULL,
  `alert_id` INT NOT NULL,
  `agency_id` VARCHAR(10) NOT NULL,
  `route_id` INT NOT NULL,
  `direction_id` INT NOT NULL,
  PRIMARY KEY (`alert_entity_id`));

CREATE TABLE `nyc_transit`.`alert_periods` (
  `alert_period_id` INT NOT NULL,
  `alert_id` INT NOT NULL,
  `start` DATETIME NOT NULL,
  `end` DATETIME NOT NULL,
  PRIMARY KEY (`alert_period_id`));

-- parse_lirr_gtfs and parse_transit_folder
CREATE TABLE `nyc_transit`.`stops` (
  `stop_id` INT NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `description` VARCHAR(100) NOT NULL,
  `latitude` DECIMAL(11,8) NOT NULL,
  `longitude` DECIMAL(11,8) NOT NULL,
  PRIMARY KEY (`stop_id`));

CREATE TABLE `nyc_transit`.`routes` (
  `route_id` INT NOT NULL,
  `agency_id` VARCHAR(15) NOT NULL,
  `short_name` VARCHAR(50) NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `description` VARCHAR(500) NOT NULL,
  `url` VARCHAR(100) NOT NULL,
  `color` VARCHAR(10) NOT NULL,
  `text_color` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`route_id`));

CREATE TABLE `nyc_transit`.`trips` (
  `trip_id` INT NOT NULL,
  `route_id` INT NOT NULL,
  `service_id` VARCHAR(15) NOT NULL,
  `trip_headsign` VARCHAR(50) NOT NULL,
  `direction` VARCHAR(5) NOT NULL,
  `block_id` INT NOT NULL,
  `shape_id` INT NOT NULL,
  PRIMARY KEY (`trip_id`));

CREATE TABLE `nyc_transit`.`shapes` (
  `shape_id` INT NOT NULL,
  `latitude` DECIMAL(11, 8) NOT NULL,
  `longitude` DECIMAL(11, 8) NOT NULL,
  `sequence` INT NOT NULL,
  `distance` DECIMAL(12,6) NOT NULL,
  PRIMARY KEY (`shape_id`));

CREATE TABLE `nyc_transit`.`stop_times` (
  `stop_time_id` INT NOT NULL,
  `trip_id` INT NOT NULL,
  `arrival` DATETIME NOT NULL,
  `departure` DATETIME NOT NULL,
  `stop_id` INT NOT NULL,
  `sequence` INT NOT NULL,
  `pickup_type` VARCHAR(20) NOT NULL,
  `drop_off_type` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`stop_time_id`));

CREATE TABLE `nyc_transit`.`exception_dates` (
  `exception_date_id` INT NOT NULL,
  `service_id` VARCHAR(20) NOT NULL,
  `exception_date` DATE NOT NULL,
  `type` TINYINT(1) NOT NULL,
  PRIMARY KEY (`exception_date_id`));

CREATE TABLE `nyc_transit`.`service_dates` (
  `service_date_id` INT NOT NULL,
  `service_id` VARCHAR(20) NOT NULL,
  `monday` VARCHAR(20) NOT NULL,
  `tuesday` VARCHAR(20) NOT NULL,
  `wednesday` VARCHAR(20) NOT NULL,
  `thursday` VARCHAR(20) NOT NULL,
  `friday` VARCHAR(20) NOT NULL,
  `saturday` VARCHAR(20) NOT NULL,
  `sunday` VARCHAR(20) NOT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE NOT NULL,
  PRIMARY KEY (`service_date_id`));