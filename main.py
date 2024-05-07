import spacy

# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

known_tables = ['employees', 'department', 'sales']  # Example table names

def parse_query(input_query):
    doc = nlp(input_query)
    intent = None
    table = None

    if any(word in input_query.lower() for word in ["show", "display"]):
        intent = "SELECT"

    for token in doc:
        if token.dep_ == 'pobj' and token.head.text in ['from', 'in']:
            if token.text.lower() not in ['the', 'a', 'an'] and token.text.lower() in known_tables:
                table = token.text
                break

    return intent, table

# Example usage
input_query = "Show me all records from the employee table"
intent, table = parse_query(input_query)
print(f"Intent: {intent}, Table: {table}")
