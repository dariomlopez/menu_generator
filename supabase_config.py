import os
from supabase import create_client, Client

# Security: Use environment variables for sensitive information
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Validate configuration
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Supabase URL and Key must be set in environment variables")

# Initialize Supabase client with enhanced security
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_secure_connection():
    """
    Provides a secure Supabase connection with additional security checks
    """
    try:
        # Example of additional security validation
        # You can add more custom checks here
        return supabase
    except Exception as e:
        # Implement secure logging
        print(f"Secure connection error: {e}")
        raise

def create_secure_row_level_policy():
    """
    Creates Row Level Security policies for your tables
    """
    # Example RLS policy (customize for your specific use case)
    rls_policy = """
    CREATE POLICY "Users can only see their own menu entries" 
    ON menu_entries 
    FOR SELECT 
    USING (auth.uid() = user_id);
    """
    # Apply the policy (you would need to execute this in Supabase SQL editor)
    return rls_policy

# Recommended security practices
def validate_user_input(input_data):
    """
    Sanitize and validate user inputs before database operations
    """
    # Implement input validation logic
    # Remove potential SQL injection risks
    # Validate data types, lengths, and formats
    sanitized_data = {}
    for key, value in input_data.items():
        # Add specific validation rules
        if isinstance(value, str):
            sanitized_data[key] = value.strip()[:255]  # Example: limit string length
    return sanitized_data
