const fs = require('fs');
const path = require('path');
const { marked } = require('marked');

// Get CLI arguments
const [,, inputFile, outputFile] = process.argv;

if (!inputFile || !outputFile) {
  console.error("❌ Usage: node convert.js input.md output.html");
  process.exit(1);
}

// Read Markdown file
fs.readFile(inputFile, 'utf8', (err, data) => {
  if (err) {
    console.error("❌ Error reading file:", err.message);
    return;
  }

  // Convert Markdown to HTML
  const htmlContent = marked(data);

  // Write HTML to output file
  fs.writeFile(outputFile, htmlContent, (err) => {
    if (err) {
      console.error("❌ Error writing file:", err.message);
      return;
    }
    console.log(`✅ Converted '${inputFile}' to '${outputFile}' successfully.`);
  });
});
