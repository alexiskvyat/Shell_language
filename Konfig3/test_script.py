import unittest
from main import parse_xml, xml_to_uky  # Импортируем необходимые функции из основного файла


class TestXmlToUky(unittest.TestCase):

    def test_simple_config(self):
        """Тест для простого конфигурационного XML."""
        xml = "<config><key>value</key></config>"
        root = parse_xml(xml)
        output = xml_to_uky(root)
        expected = "dict(\n  key = value,\n)"
        self.assertEqual(output, expected)

    def test_nested_config(self):
        """Тест для вложенного конфигурационного XML."""
        xml = "<config><nested><key>value</key></nested></config>"
        root = parse_xml(xml)
        output = xml_to_uky(root)
        expected = "dict(\n  nested = dict(\n    key = value,\n  ),\n)"
        self.assertEqual(output, expected)

    def test_multiple_keys(self):
        """Тест для XML с несколькими ключами."""
        xml = "<config><key1>value1</key1><key2>value2</key2></config>"
        root = parse_xml(xml)
        output = xml_to_uky(root)
        expected = "dict(\n  key1 = value1,\n  key2 = value2,\n)"
        self.assertEqual(output, expected)

    def test_empty_element(self):
        """Тест для пустого элемента в XML."""
        xml = "<config><key1></key1></config>"
        root = parse_xml(xml)
        output = xml_to_uky(root)
        expected = "dict(\n  key1 = ,\n)"
        self.assertEqual(output, expected)

    def test_syntax_error(self):
        """Тест для некорректного XML (ошибка парсинга)."""
        xml = "<config><key>value</key>"
        with self.assertRaises(ValueError) as context:
            parse_xml(xml)
        self.assertIn("Ошибка синтаксиса XML", str(context.exception))

    def test_complex_structure(self):
        """Тест для сложной структуры XML."""
        xml = """
        <config>
            <key1>value1</key1>
            <nested>
                <key2>value2</key2>
                <inner>
                    <key3>value3</key3>
                </inner>
            </nested>
        </config>
        """
        root = parse_xml(xml)
        output = xml_to_uky(root)
        expected = (
            "dict(\n"
            "  key1 = value1,\n"
            "  nested = dict(\n"
            "    key2 = value2,\n"
            "    inner = dict(\n"
            "      key3 = value3,\n"
            "    ),\n"
            "  ),\n"
            ")"
        )
        self.assertEqual(output, expected)

    def test_empty_xml(self):
        """Тест для пустого XML (без элементов)."""
        xml = "<config></config>"
        root = parse_xml(xml)
        output = xml_to_uky(root)
        expected = ""
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
