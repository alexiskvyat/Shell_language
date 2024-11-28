import sys
import xml.etree.ElementTree as ET


def parse_xml(input_data):
    """Парсинг XML строки в дерево элементов."""
    try:
        root = ET.fromstring(input_data)
        return root
    except ET.ParseError as e:
        raise ValueError(f"Ошибка синтаксиса XML: {e}")


def xml_to_uky(element, indent=0):
    """Рекурсивное преобразование XML в УКЯ."""
    result = []
    prefix = " " * indent  # Префикс для текущего уровня вложенности

    if len(element):  # Если элемент имеет вложенные элементы
        result.append(f"{prefix}dict(")
        for child in element:
            if len(child):  # Если вложенные элементы
                value = xml_to_uky(child, indent + 2)
                result.append(f"{prefix}  {child.tag} = {value},")
            else:  # Простые значения
                value = child.text.strip() if child.text and child.text.strip() else ""
                result.append(f"{prefix}  {child.tag} = {value},")
        result.append(f"{prefix})")
    else:  # Элемент без вложенных элементов
        text_value = element.text.strip() if element.text else ""
        return text_value

    # Удаляем лишнюю запятую и пробел после последнего элемента
    return "\n".join(result).strip()


def main():
    """Основной цикл работы программы."""
    input_data = sys.stdin.read()  # Чтение данных из стандартного ввода
    try:
        xml_root = parse_xml(input_data)
        output = xml_to_uky(xml_root)
        print(output)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
