import json


from transformers import pipeline
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

with open("category.json" , "r") as file:
  product_tree = json.loads(file.read())


def calculator(values , price,product_condition , cleaning_frequency):
        
        
        appliance_factor = values.get("appliance_type_factor", 1.0)
        size_factor = values.get("size_factor", 1.0)
        selected_product_price_factor = price / 100.0  # Assuming the product price is in dollars
        price = (
            + 20 * appliance_factor * size_factor * product_condition
        ) * cleaning_frequency * selected_product_price_factor
        return price


def categorize_content(product_tree, sequence, address=""):
    labels = list(product_tree.keys())
    hypothesis_template = 'This text is about {}.'
    prediction = classifier(sequence, labels, hypothesis_template=hypothesis_template, multi_class=True)
    best_match = prediction["labels"][0]
    address += f">{best_match}"

    if not product_tree[best_match].get("name"):
        return categorize_content(product_tree[best_match], sequence, address)
    else:
        return [address, product_tree[best_match]]

sequence = "a dog shed"
addr , values = categorize_content(product_tree , sequence)
print(values)