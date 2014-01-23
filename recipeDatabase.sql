SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `myRecipes` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci ;
USE `myRecipes` ;

-- -----------------------------------------------------
-- Table `myRecipes`.`recipes`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `myRecipes`.`recipes` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `title` VARCHAR(255) NOT NULL ,
  `image` BLOB NULL ,
  `preptime` INT UNSIGNED NULL ,
  `cooktime` INT UNSIGNED NULL ,
  `yield` TINYINT UNSIGNED NULL ,
  `difficulty` TINYINT UNSIGNED NULL ,
  `link` VARCHAR(255) NULL ,
  `reference` VARCHAR(128) NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `myRecipes`.`ingredients`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `myRecipes`.`ingredients` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `recipe_id` INT UNSIGNED NOT NULL ,
  `wholeNum` TINYINT UNSIGNED NULL ,
  `fractNum` TINYINT UNSIGNED NULL ,
  `unit` VARCHAR(8) NOT NULL ,
  `item` VARCHAR(128) NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `recipeToIngredients_idx` (`recipe_id` ASC) ,
  CONSTRAINT `recipeToIngredients`
    FOREIGN KEY (`recipe_id` )
    REFERENCES `myRecipes`.`recipes` (`id` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `myRecipes`.`instructions`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `myRecipes`.`instructions` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `recipe_id` INT UNSIGNED NOT NULL ,
  `instruction` VARCHAR(1024) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `recipeToInstruct_idx` (`recipe_id` ASC) ,
  CONSTRAINT `recipeToInstruct`
    FOREIGN KEY (`recipe_id` )
    REFERENCES `myRecipes`.`recipes` (`id` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `myRecipes`.`comments`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `myRecipes`.`comments` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `recipe_id` INT UNSIGNED NOT NULL ,
  `comment` VARCHAR(1024) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `recipeToComm_idx` (`recipe_id` ASC) ,
  CONSTRAINT `recipeToComm`
    FOREIGN KEY (`recipe_id` )
    REFERENCES `myRecipes`.`recipes` (`id` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `myRecipes`.`keywords`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `myRecipes`.`keywords` (
  `id` INT UNSIGNED NOT NULL ,
  `ingredient_id` INT UNSIGNED NOT NULL ,
  `keyword` VARCHAR(128) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `ingredient_id_idx` (`ingredient_id` ASC) ,
  CONSTRAINT `ingredient_id`
    FOREIGN KEY (`ingredient_id` )
    REFERENCES `myRecipes`.`ingredients` (`id` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `myRecipes`.`ratings`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `myRecipes`.`ratings` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `recipe_id` INT UNSIGNED NOT NULL ,
  `rating` TINYINT UNSIGNED NULL ,
  `review` VARCHAR(1024) NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `recipeToRating_idx` (`recipe_id` ASC) ,
  CONSTRAINT `recipeToRating`
    FOREIGN KEY (`recipe_id` )
    REFERENCES `myRecipes`.`recipes` (`id` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
