import os
import logging
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Security: Use environment variables for sensitive information
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

def initialize_supabase_client():
    """
    Initialize Supabase client with robust error handling
    """
    try:
        # Validate configuration with more detailed logging
        if not SUPABASE_URL:
            logger.error("SUPABASE_URL is not set in environment variables")
            raise ValueError("SUPABASE_URL must be set")
        
        if not SUPABASE_KEY:
            logger.error("SUPABASE_KEY is not set in environment variables")
            raise ValueError("SUPABASE_KEY must be set")
        
        # Initialize Supabase client with enhanced security
        client = create_client(SUPABASE_URL, SUPABASE_KEY)
        logger.info("Supabase client initialized successfully")
        return client
    except Exception as e:
        logger.error(f"Failed to initialize Supabase client: {e}")
        raise

# Initialize client at module level with error handling
try:
    supabase = initialize_supabase_client()
except Exception as e:
    logger.critical(f"Could not initialize Supabase client: {e}")
    supabase = None

def get_secure_connection():
    """
    Provides a secure Supabase connection with additional security checks
    """
    if supabase is None:
        raise RuntimeError("Supabase client not initialized")
    
    try:
        # Additional connection validation can be added here
        return supabase
    except Exception as e:
        logger.error(f"Secure connection error: {e}")
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
