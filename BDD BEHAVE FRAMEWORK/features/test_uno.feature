#EJECUTAR ESCRIBIENDO EN LA TERMINAL: behave features

Feature: primer demo

  Background:
    Given abriendo el navegador


  Scenario Outline: corriendo nuestro primer test
      When cargando el nombre del usuario "<usuario>"
      Then cargando su email "<email>"
      Then cargando su direccion1 "<direccion1>"
      Then cargando su direccion2 "<direccion2>"
      Examples:
      | usuario | email | direccion1 | direccion2 |
      | nombre1 | email1@gmail.com | direccion1 | direccion6 |
      | nombre2 | email2@gmail.com | direccion2 | direccion7 |
      | nombre3 | email3@gmail.com | direccion3 | direccion8 |
      | nombre4 | email4@gmail.com | direccion4 | direccion9 |
      | nombre5 | email5@gmail.com | direccion5 | direccion10 |



