# InlineGPT

https://user-images.githubusercontent.com/79325116/229753626-0cc23047-23ea-4e00-b25a-64f4d69d540e.mp4

InlineGPT is a versatile and user-friendly Python project that enables users to access the power of GPT directly from their cursor. The project is designed with ease-of-use in mind, allowing users to simply run the program and enter their OpenAI API key to get started. InlineGPT is compatible with major operating systems such as Windows, macOS, and Linux.

## Features


- Intuitive GUI for easy configuration of API key and trigger
- Direct use of GPT within the active window
- Customizable trigger key (default: CMD for macOS, Ctrl_Left for Linux and Windows)
- Inline response from the GPT engine, enhancing the user experience

## Getting Started

### Pre-built binaries

The easiest way to start using InlineGPT is to download the pre-built binaries from the `ready-to-use` folder for your operating system. Unzip the archive and run the `main` executable to start the program.

### Building from source

If you prefer to build the project from source, follow these steps:

1. Create a virtual environment and activate it.

```bash
python -m venv venv
source venv/bin/activate  # For Linux and macOS
venv\Scripts\activate     # For Windows
```

2. Install the required packages.

```bash
pip install -r requirement.txt 
```

3. Compile the executables using PyInstaller.

```bash
pyinstaller run_client.py --onefile
pyinstaller main.py --onefile
```
4. Get api key https://elephas.app/blog/how-to-create-openai-api-keys-cl5c4f21d281431po7k8fgyol0

5. Run the `main` executable to start the program.



## Usage

1. Start the `main` program to open the GUI.
2. Configure the OpenAI API key and trigger according to your preference.
3. In any text field, type `GPT: <Prompt> <Trigger Press>` to start the engine.
4. The GPT engine will provide an inline response at the cursor location.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Any contributions to improve the project are welcome. Please feel free to open an issue or submit a pull request.

## Acknowledgments

- [OpenAI](https://openai.com) for providing the GPT API.
