from typing import Union
import xml.etree.ElementTree as ElementTreeObject


def read_xml_file(file_path: str) -> Union[ElementTreeObject.Element, Exception]:
    """
    This function returns a ElementTreeObject like this:
    <Element "root" at 0x7f50fb49dc20>
    or Exception with traceback.
    """
    try:
        return ElementTreeObject.parse(file_path).getroot()
    except ElementTreeObject.ParseError:
        return ElementTreeObject.ParseError("Error al analizar el archivo XML, checa si el formato es correcto.")
    except FileNotFoundError:
        return FileNotFoundError("No se encontro la ruta del archivo.")
    except Exception as unknown_exception:
        return Exception(f"Unknown exception ocurred. {str(unknown_exception)}")
