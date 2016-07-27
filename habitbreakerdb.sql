-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema habitbreakerdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema habitbreakerdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `habitbreakerdb` ;
USE `habitbreakerdb` ;

-- -----------------------------------------------------
-- Table `habitbreakerdb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `habitbreakerdb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `phone_number` INT NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `habitbreakerdb`.`habits`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `habitbreakerdb`.`habits` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `amount` FLOAT NULL,
  `habit_name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `holder_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_habits_users1_idx` (`holder_id` ASC),
  CONSTRAINT `fk_habits_users1`
    FOREIGN KEY (`holder_id`)
    REFERENCES `habitbreakerdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `habitbreakerdb`.`violations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `habitbreakerdb`.`violations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `habit_id` INT NOT NULL,
  `helper_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_violations_habits1_idx` (`habit_id` ASC),
  INDEX `fk_violations_users1_idx` (`helper_id` ASC),
  CONSTRAINT `fk_violations_habits1`
    FOREIGN KEY (`habit_id`)
    REFERENCES `habitbreakerdb`.`habits` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_violations_users1`
    FOREIGN KEY (`helper_id`)
    REFERENCES `habitbreakerdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `habitbreakerdb`.`helpers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `habitbreakerdb`.`helpers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `habit_id` INT NOT NULL,
  `helper_id` INT NOT NULL,
  INDEX `fk_users_has_helpers_habits1_idx` (`habit_id` ASC),
  INDEX `fk_helpers_users1_idx` (`helper_id` ASC),
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_users_has_helpers_habits1`
    FOREIGN KEY (`habit_id`)
    REFERENCES `habitbreakerdb`.`habits` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_helpers_users1`
    FOREIGN KEY (`helper_id`)
    REFERENCES `habitbreakerdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
