##Lexical Analyzer




                
input_file = "omer1.txt"
output_file = "omer2.txt"





class Preprocessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def remove_blank_lines(self):
        #Remove blank lines from the file
        with open(self.input_file, 'r') as file:
            non_blank_lines = []
            for line in file:
                if line.strip():
                    non_blank_lines.append(line)

            

        with open(self.output_file, 'w') as file:
            file.writelines(non_blank_lines)

    def remove_imports_annotations(self):
        """Remove import statements and annotations."""
        with open(self.output_file, 'r') as file:
            
            lines = file.readlines()

        modified_lines = []
        for line in lines:
            stripped_line = line.strip()
            if not stripped_line.startswith(('import', '@')):
                modified_lines.append(line)

        with open(self.output_file, 'w') as file:
            file.writelines(modified_lines) 

    def remove_comments_statements(self):
        """Remove comment lines from the file."""
        with open(self.output_file, 'r') as file:
            lines = file.readlines()

        modified_lines = []
        for line in lines:
            stripped_line = line.strip()
            if not (stripped_line.startswith('#') or stripped_line.startswith('"""')):
                modified_lines.append(line)


        with open(self.output_file, 'w') as file:
            file.writelines(modified_lines)

    def preprocess_file(self):
        """Run all preprocessing steps and display the output."""
        self.remove_blank_lines()
        self.remove_comments_statements()
        self.remove_imports_annotations()

        print(f"Processed file saved to {self.output_file}\n")

        with open(self.output_file, 'r') as file:
            data = file.read()
            print(data)

# Usage
input_file = "omer1.txt"
output_file = "omer2.txt"

processor = Preprocessor(input_file, output_file)
processor.preprocess_file()

print()
class Processor:
    def __init__(self, input_file, output_file):
        # Correctly assign the input and output file names
        self.input_file = input_file
        self.output_file = output_file
    def break_data(self):
        with open(self.input_file, 'r') as input_file:
            
            buffer = []
            while True:
                char = input_file.read(1)
                
                if not char:
                    
                    break
                if char== "\n":
                    buffer.append(";")
                if char != '\n':
                    
                    buffer.append(char)

            #buffer.append(";")
            buffer.append('$')

        
        with open(self.output_file, 'w') as output_file:
            output_file.write(''.join(buffer))

        
        with open(self.output_file, 'r') as output_file:
            
            data = output_file.read()
            print(data) 
        
        
    
        

        


input_file = "omer2.txt"
output_file = "omer3.txt"

processor = Processor(input_file, output_file)
processor.break_data()
print()

class LexicalAnalysis:

    def generator(self, input_file, output_file):
        with open(input_file, 'r') as file:
            content = file.read()

        # Define keywords, operators, and punctuators
        keywords = set(["and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except",
                        "False", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "None", 
                        "nonlocal", "not", "or", "pass", "raise", "return", "True", "try", "while", "with", "yield"])
        operators = set(["+", "-", "*", "/", "%", "=", "==", "!=", "<", ">", "<=", ">=", "and", "or", "not", "in", "is"])
        punctuators = set(["{", "}", "[", "]", "(", ")", ",", ";", ":", "."])

        # Splitting the content into words and symbols
        lexemes = []
        word = ''
        for char in content:
            if char.isalpha() or char.isdigit() or char in ['_', '.']:
                word += char
            else:
                if word:
                    lexemes.append(word)
                    word = ''
                if char in operators or char in punctuators:
                    lexemes.append(char)

        self.write_lexemes_to_file(lexemes, output_file)

    def write_lexemes_to_file(self, lexemes, output_file):
        with open(output_file, 'w') as file:
            for lexeme in lexemes:
                file.write("Lexeme: " + lexeme + '\n')

        with open(output_file, 'r') as file:
            data = file.read()
            print("task3 output is: \n" + data)


input_file3 = "omer3.txt"
output_file3 = "omer4.txt"
lexical_analysis = LexicalAnalysis()
lexical_analysis.generator(input_file3, output_file3)

