#Code below
help("string")

def printing_model_design(unprinted_models,completed_models):
    """Print models moving each item to completed_models"""
    while unprinted_models:
        current_desing = unprinted_models.pop()
        print(f"Printing {current_desing}")
        completed_models.append(current_desing)
        
