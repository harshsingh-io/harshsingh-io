import os
from dotenv import load_dotenv
from .github_stats import GitHubStats
from .readme_generator import ReadmeGenerator

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get GitHub token from environment
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise ValueError("GitHub token not found. Please set GITHUB_TOKEN environment variable.")
    
    try:
        # Initialize the stats fetcher
        stats_fetcher = GitHubStats(token)
        
        # Fetch the stats
        print("Fetching GitHub stats...")
        stats = stats_fetcher.fetch_user_stats()
        print(f"Found stats for user: {stats['username']}")
        
        # Initialize the README generator
        generator = ReadmeGenerator()
        
        # Generate the stats section
        print("Generating stats section...")
        stats_section = generator.generate_stats_section(stats)
        
        # Update the README
        print("Updating README...")
        changed = generator.update_readme("README.md", stats_section)
        
        if changed:
            print("README updated successfully!")
        else:
            print("No changes needed in README.")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    main() 