import unittest
from extract_markdown_images import *



class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        test_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        result = extract_markdown_images(test_text)

        assert result == expected_result, (
            f"The resulting list of tuples should be {expected_result} but instead reads: [{result}]"
            )

        print(f"\nThis is the result of test_extract_markdown_images: [{result}])")
        print(f"\nThis is the test text that was used: [{test_text}]")
        print("----------------------------------------------------------")

    def test_extract_markdown_images_mixed_content(self):
        test_text = "Here's a ![image](img.jpg) and a [link](url.com)"
        result = extract_markdown_images(test_text)
        expected_result = [("image", "img.jpg")]

        assert result == expected_result, (
            f"The resulting list of tuples should be {expected_result} but instead reads: [{result}]"
            )
        
        print(f"\nThis is the result of test_extract_markdown_images_mixed_content: [{result}])")
        print(f"\nThis is the test text that was used: [{test_text}]")
        print("----------------------------------------------------------")

    def test_extract_markdown_images_empty_values(self):
        test_text = "![](https://img.jpg) and [](https://link.com)"
        result = extract_markdown_images(test_text)
        expected_result = [("", "https://img.jpg")]

        assert result == expected_result, (
            f"The resulting list of tuples should be {expected_result} but instead reads: [{result}]"
            )
        
        print(f"\nThis is the result of test_extract_markdown_images_empty_values: [{result}])")
        print(f"\nThis is the test text that was used: [{test_text}]")
        print("----------------------------------------------------------")

    def test_extract_markdown_images_consecutive_patterns(self):
        test_text = "![img1](url1.jpg)![img2](url2.jpg)"
        result = extract_markdown_images(test_text)
        expected_result = [("img1", "url1.jpg"), ("img2", "url2.jpg")]
        
        assert result == expected_result, (
            f"The resulting list of tuples should be {expected_result} but instead reads: [{result}]"
            )
        
        print(f"\nThis is the result of test_extract_markdown_images_consecutive_patterns: [{result}])")
        print(f"\nThis is the test text that was used: [{test_text}]")
        print("----------------------------------------------------------")


    def test_extract_markdown_images_nested_patterns(self):
        test_text = "![Complex [alt] text](complex(url)here.jpg)"
        with self.assertRaises(Exception) as context:
            result = extract_markdown_images(test_text)

        self.assertEqual(
        str(context.exception),
        "No valid markdown images found"
        )

        print("\n text_extract_markdown_images_nested_patterns successful.")
        print("----------------------------------------------------------")

    def test_extract_markdown_images_no_images(self):
        test_text = "This is text that lacks any images"

        with self.assertRaises(Exception) as context:
            result = extract_markdown_images(test_text)

            print(result)

        self.assertEqual(
            str(context.exception),
            "No valid markdown images found"
        )

        print("\n text_extract_markdown_images_no_images successful.")
        print("----------------------------------------------------------")

