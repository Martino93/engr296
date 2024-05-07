from transformers import T5ForConditionalGeneration, T5Tokenizer

def load_model(model_name="t5-small"):
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

def translate_to_sql(query, tokenizer, model):
    input_text = "translate English to SQL: " + query
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(input_ids)
    sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return sql_query

# Load the model
tokenizer, model = load_model()

# Test the model
natural_language_query = "Show me all records from the employee table"
sql_query = translate_to_sql(natural_language_query, tokenizer, model)
print(f"Generated SQL: {sql_query}")
