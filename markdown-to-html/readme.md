# 📝 Markdown to HTML Converter

A simple Node.js command-line tool that converts a `.md` (Markdown) file into a clean `.html` file using the [`marked`](https://www.npmjs.com/package/marked) library.

## 📦 Installation

1. Clone or download this repository.
2. Open your terminal in the project folder and run:

```bash
npm install
```

## 🚀 Usage

Make sure you have a Markdown file (e.g., `sample.md`), then run:

```bash
node convert.js sample.md output.html
```

- `sample.md` is your input file
- `output.html` will be the converted output file

## ✅ Example

```bash
node convert.js sample.md result.html
```

This will generate `result.html` in the same directory.

## 🛠 Requirements

- Node.js installed on your system
- A `.md` file to convert

## 📄 Sample Markdown

You can create a basic `sample.md` file like this:

```markdown
# Welcome

This is **bold**, *italic*, and a [link](https://example.com).

## List

- Item 1
- Item 2
```

Run the tool and view the output HTML in your browser.

---

Save this as `README.md` in your project folder, and you're all set ✅

Let me know if you want to add CLI flags or convert this into a global tool!