
# 📄 **DocuParse**

DocuParse is a high-performance tool for converting PDF documents into clean, structured Markdown files. Designed for speed and accuracy, it extracts and formats content while minimizing errors like hallucinations and repetitions.

---

## 🚀 **Key Features**

- **Multi-Format Support**: Converts PDFs, EPUBs, and MOBIs into Markdown.
- **Accurate Layout Detection**: Utilizes AI models to detect page layouts, columns, and format equations in LaTeX.
- **Enhanced Formatting**: Cleans headers, footers, and artifacts, while preserving code blocks and tables.
- **Multi-Language Support**: Processes documents in various languages, optimized for English, French, Spanish, and more.
- **Cloud-Based Processing**: Leverages Google Colab for GPU-accelerated operations.

---

## 🛠️ **How It Works**

DocuParse is powered by a robust AI pipeline:
1. **Text Extraction**: Extracts text with or without OCR as needed.
2. **Layout Analysis**: Identifies and segments content using advanced AI models.
3. **Content Cleaning**: Applies heuristics to clean and format content blocks.
4. **Post-Processing**: Combines content blocks into a structured Markdown document.

---

## 📂 **Project Structure**

```plaintext
DocuParse/
│
├── scripts/             # Utility scripts for setup and processing
├── data/                # Sample input and output files
├── examples/            # Example documents and Markdown outputs
├── models/              # AI models used for text extraction and layout analysis
└── README.md            # Project documentation
```

---

## 🖥️ **Usage**

### **1. Clone the Repository**

```bash
git clone https://github.com/<your-username>/DocuParse.git
cd DocuParse
```

### **2. Set Up the Environment**

Run DocuParse in Google Colab for GPU-accelerated processing. Install the required Python packages:

```bash
pip install -r requirements.txt
```

### **3. Convert a Single File**

```bash
python convert_single.py /path/to/file.pdf /path/to/output.md --parallel_factor 2 --max_pages 10
```

### **4. Convert Multiple Files**

```bash
python convert.py /path/to/input/folder /path/to/output/folder --workers 10 --max 10
```

---

## 🎨 **Examples**

| **Input (PDF)**                        | **Output (Markdown)**                |
|----------------------------------------|---------------------------------------|
| Textbook: Think Python                 | [View](examples/thinkpython.md)       |
| Scientific Paper: Switch Transformers  | [View](examples/switch_transformers.md) |

---

## 📊 **Performance**

- **Speed**: DocuParse processes documents up to **10x faster** than similar tools.
- **Accuracy**: Minimizes hallucinations and ensures well-structured Markdown outputs.
- **GPU Utilization**: Efficiently leverages GPU resources for parallel processing.

---

## 📜 **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🙌 **Acknowledgments**

This project was made possible by incredible open-source models and datasets, including:
- **Tesseract OCR** for text recognition.
- **HuggingFace Transformers** for layout and content analysis.
- **LaTeX** for equation formatting.

Thank you to the open-source community for their invaluable contributions!