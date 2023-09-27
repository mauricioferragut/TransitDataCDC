CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    id                  varchar(255) not null,
    latitude            decimal(11,8) not null,
    longitude           decimal(11,8) not null,
    direction_id        int(1) not null,
    occupancy_status    varchar(255) null,
    current_status      varchar(255) null,
    current_stop_sequence int(2) null,
    bearing             int(3) null,
    updated_at          timestamp not null
              

);

