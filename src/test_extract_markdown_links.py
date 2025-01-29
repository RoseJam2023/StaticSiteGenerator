import unittest
from extract_markdown_links import *



class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        test_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

        expected_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

        result = extract_markdown_links(test_text)

        assert result == expected_result, (
            f"The resulting list of tuples should be {expected_result} but instead reads: [{result}]"
            )
        
        print(f"\nThis is the result of test_extract_markdown_links: [{result}])")
        print(f"\nThis is the test text that was used: [{test_text}]")
        print("----------------------------------------------------------")

    def test_extract_markdown_links_mixed_content(self):
        test_text = "Here's a ![image](img.jpg) and a [link](url.com)"
        result = extract_markdown_links(test_text)
        expected_result = [("link", "url.com")]

        assert result == expected_result, (
            f"The resulting list of tuples should be {expected_result} but instead reads: [{result}]"
            )
        
        print(f"\nThis is the result of test_extract_markdown_links_mixed_content: [{result}])")
        print(f"\nThis is the test text that was used: [{test_text}]")
        print("----------------------------------------------------------")

    def test_extract_markdown_links_empty_values(self):
        test_text = "![](https://img.jpg) and [](https://link.com)"
        result = extract_markdown_links(test_text)
        expected_result = [("", "https://link.com")]

        assert result == expected_result, (
            f"The resulting list of tuples should be {expected_result} but instead reads: [{result}]"
            )
        
        print(f"\nThis is the result of test_extract_markdown_links_empty_values: [{result}])")
        print(f"\nThis is the test text that was used: [{test_text}]")
        print("----------------------------------------------------------")

    def test_extract_markdown_links_consecutive_patterns(self):
        test_text = "[anchor1](url1.com) [anchor2](url2.com)"
        result = extract_markdown_links(test_text)
        expected_result = [("anchor1", "url1.com"), ("anchor2", "url2.com")]
        
        assert result == expected_result, (
            f"The resulting list of tuples should be {expected_result} but instead reads: [{result}]"
            )
        
        print(f"\nThis is the result of test_extract_markdown_links_consecutive_patterns: [{result}])")
        print(f"\nThis is the test text that was used: [{test_text}]")
        print("----------------------------------------------------------")

    def test_extract_markdown_links_nested_patterns(self):
        test_text = "[Complex [anchor] text](complex(url)here.com)"
        with self.assertRaises(Exception) as context:
            result = extract_markdown_links(test_text)

        self.assertEqual(
        str(context.exception),
        "No valid markdown links found"
        )

        print("\n text_extract_markdown_links_nested_patterns successful.")
        print("----------------------------------------------------------")

    def test_extract_markdown_links_no_links(self):
        test_text = "This is text with no URLs at all"
    
        with self.assertRaises(Exception) as context:
            result = extract_markdown_links(test_text)
    
        self.assertEqual(
            str(context.exception),
            "No valid markdown links found"
        )

        print("\n text_extract_markdown_links_no_links successful.")
        print("----------------------------------------------------------")