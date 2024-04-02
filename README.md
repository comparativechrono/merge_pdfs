# PDF Merger App

This repository contains a simple yet powerful tool for merging multiple PDF files into a single PDF document. Built with Streamlit, the app provides a user-friendly interface for selecting and merging PDFs directly from your browser. Now you no longer need to pay to merge PDF files!

## Features

- **Easy Upload**: Drag and drop your PDF files into the uploader.
- **Instant Merge**: Merge your selected PDFs with a single click.
- **Download**: Download the merged PDF to your device.

## Contents

- `merge_pdfs.ipynb`: A Jupyter notebook containing the original script for merging PDF files.
- `requirements.txt`: Lists all the dependencies required to run the Streamlit app.
- `streamlit_app.py`: The Streamlit app script, providing a GUI for the PDF merger functionality.

## Online Usage

For those who prefer not to install anything, the PDF Merger app is available online. You can access and use the app through any web browser:

[Access the PDF Merger App](https://mergepdfs.streamlit.app/)

### How to Use the Online App

1. **Open the App**: Click on the link above to open the PDF Merger app in your browser.

2. **Upload PDFs**: Use the 'Choose PDF files' button to select the PDF files you want to merge. You can select multiple files by holding down the 'Ctrl' (or 'Command' on Mac) key while clicking on the files.

3. **Merge**: Once all your files are uploaded, the app will automatically merge them into a single PDF document.

4. **Download**: Click on the 'Download Merged PDF' button to save the merged document to your device.

This online version provides a convenient way to quickly merge PDFs without the need to run any code locally. It's especially useful for those on devices where installing software is not feasible.


## Local Installation and Usage

### Installation

1. Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/comparativechrono/merge_pdfs.git
   ```
   
2. Navigate into the cloned repository:
   ```bash
   cd merge_pdfs
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Local usage

To run the Streamlit app locally, execute the following command in your terminal:

```bash
streamlit run streamlit_app.py
```

This will start the Streamlit server, and you should see a URL in your terminal that you can visit in your web browser to access the app.

## Dependencies

- PyPDF2==3.0.1: Used for the core functionality of merging PDF files.
- Streamlit: Provides the web interface for uploading and merging PDFs.

## Contributing

Contributions to improve the PDF Merger app are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).
