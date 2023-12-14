if __name__ == "__main__":
    # Library.
    from lib.system import get_terminal_arguments
    from lib.files import read_xml_file
    from lib.validations import isNumber

    # Models.cr
    from lib import exceptions as Exceptions
    from typing import Union
    import xml.etree.ElementTree as ElementTreeObject
    from lib.constants import PrototypeLanguageJobs


    # Variables.
    arguments = get_terminal_arguments()

    # Argument validation.
    if len(arguments) > 1:
        xml_file_path: str = arguments[0]
        prototype_languge_job: str = arguments[1]

        # Job validation.
        if not isNumber(prototype_languge_job):
            print(prototype_languge_job)
            raise Exceptions.PrototypeLanguageJob.JobNotExists("Ingresa un trabajo valido a realizar.")

        # Read input data.
        xml_file_content: Union[ElementTreeObject.Element, Exception] = read_xml_file(xml_file_path)

        # Validate return of input data.
        if type(xml_file_content) == ElementTreeObject.Element:
            # Validate XML and actions.
            if prototype_languge_job == PrototypeLanguageJobs.CODE_GENERATION:
                pass
            elif prototype_languge_job == PrototypeLanguageJobs.DESIGN_GENERATION:
                pass
            else:
                raise Exceptions.PrototypeLanguageJob.JobNotExists("No se encontro el trabajo a realizar.")
        else:
            raise xml_file_content
    else:
        raise Exceptions.System.Arguments("Debe proporcionar la ruta del archivo XML y el tipo de trabajo a realizar como argumentos.")