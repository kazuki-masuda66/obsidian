import sys
import os

def extract_text_from_pdf(pdf_path):
    try:
        import PyPDF2
        
        result = []
        result.append(f"=== PDF File: {os.path.basename(pdf_path)} ===")
        result.append("")
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            total_pages = len(pdf_reader.pages)
            
            result.append(f"Total Pages: {total_pages}")
            result.append("")
            
            for page_num in range(total_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                
                if text.strip():
                    result.append(f"--- Page {page_num + 1} ---")
                    result.append(text)
                    result.append("")
        
        return "\n".join(result)
    except ImportError:
        return "Error: PyPDF2 library is not installed. Please install it using: pip install PyPDF2"
    except Exception as e:
        import traceback
        return f"Error extracting text from PDF: {e}\n{traceback.format_exc()}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    result = extract_text_from_pdf(file_path)
    
    # Ensure output is encoded in UTF-8 to handle special characters
    sys.stdout.buffer.write(result.encode('utf-8', errors='replace'))


