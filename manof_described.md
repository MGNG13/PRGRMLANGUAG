# INTERPRETER

El interpretador unicamente va a ejecutar las instrucciones en la computadora; como si fuera python pero mas sencillo.

## INTERPRETER KEYWORDS ACTIONS
CREATE -> *Crea.*
RENAME -> *Renombra.*
DELETE -> *Borra.*
REPLACE -> *Reemplaza.*
ADD -> *Agrega.*
EXECUTE -> *Ejecuta / Start*

## INTERPRETER OBJECTS
FILE
    *Examples*
    FILE CREATE -> *filename*
    FILE RENAME -> *filename* -> *newfilename*
    FILE DELETE -> *filename*
    FILE ADD -> *filename* -> *content*
DIRECTORY
    *Examples*
    DIRECTORY CREATE -> *directory_name*
    DIRECTORY RENAME -> *directory_name*
    DIRECTORY DELETE -> *directory_name*
    DIRECTORY ADD -> *subdirectory_name*
SYSTEM
    *Examples*
    SYSTEM EXECUTE -> *command*
CODE
    *Examples*
    CODE CREATE -> *filename* -> { *transpiler_code* }
    CODE ADD -> *filename* -> { *transpiler_code* }

# TRANSPILER

Este transpilador se encarga se transpilar el lenguage 'Manof' a lenguajes soportados.

## KEYWORDS
transpilation_language
    *Example*
    transpilation_language *lang*
function
    *Example*
    function asd() { *transpiler_code* }
    function asd(*datatype*:*identifier*=*default_value*) {}
    function asd(*datatype*:*identifier*=*default_value*) {
        return 
    }
variable
    *Example*
    variable dynamic:*datatype* *identifier* = *value*;
    variable const:*datatype* *identifier* = *value*;
print
    *Example*
    print *identifier*;
    print *function*;
return
    *Example*
    return *function*
    return *identifier*
    return *datatype*

## LANGUAGES
js -> JavaScript
py -> Python
cpp -> C++