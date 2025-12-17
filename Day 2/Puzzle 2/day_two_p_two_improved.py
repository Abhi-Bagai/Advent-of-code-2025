def check_valid_id(product_id):
    product_id = str(product_id)
    product_id_length = len(product_id)
    
    # Early return for invalid cases
    if product_id[0] == '0' or product_id_length <= 1:
        return False
    
    possible_repeat_sizes = set((i + 1) // 2 for i in range(1, product_id_length + 1))
    
    for repeat_size in possible_repeat_sizes:
        base_indices = list(range(0, product_id_length, repeat_size))
        valid_counter = 0
        
        for index in range(0, repeat_size):
            indices = [index + i for i in base_indices]
            
            # Check if any index is out of bounds (>= product_id_length)
            # If so, reset counter and skip this iteration
            if any(i >= product_id_length for i in indices):
                valid_counter = 0
                continue
            
            # Check if all values at these indices are the same
            values_at_indices = [product_id[i] for i in indices]
            
            if len(set(values_at_indices)) == 1 and len(values_at_indices) > 0:
                valid_counter += 1
        
        # Early return if we found a valid pattern
        if valid_counter == repeat_size:
            return True
    
    return False

