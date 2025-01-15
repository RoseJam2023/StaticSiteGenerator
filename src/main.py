from textnode import *
def main():
    test_enum = TextType.CODE
    test_node = TextNode("This is a text node", test_enum, "https://www.boot.dev")

    print(test_node)

if __name__ == "__main__":
    main()